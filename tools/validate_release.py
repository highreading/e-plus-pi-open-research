#!/usr/bin/env python3
"""Validate publication structure and hashes; never execute archived research."""
from pathlib import Path
import argparse
import ast
import hashlib
import json
import re
import sys
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / 'RELEASE_MANIFEST.json'
RX_LINK = re.compile(r'(?<!!)\[([^\n]*?)\]\((<[^>]+>|[^\n)]*)\)')
RX_PROTECTED = re.compile(r'```[\s\S]*?```|\\\[[\s\S]*?\\\]|\\\([\s\S]*?\\\)|\$\$[\s\S]*?\$\$|(?<!\$)\$[^\n$]+\$(?!\$)')
RX_HOME = re.compile(r'/(?:Users|home)/[^\s`<>"\']+|[A-Za-z]:[\\/]+(?:Users|Documents and Settings)[\\/][^\s`<>"\']+', re.I)
RX_KEY = re.compile(r'(?<![A-Za-z])sk-(?:proj-|live-|test-)?[A-Za-z0-9_-]{24,}')
RX_UUID = re.compile(r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b')
RX_BEARER = re.compile(r'Bearer\s+(?!\[|REDACTED|REMOVED)[A-Za-z0-9_.-]{20,}')
RX_EMAIL = re.compile(r'(?<![\w])[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}(?![\w])')
RX_URL = re.compile(r'https?://[^\s<>`"\']+')
RX_EXTRA_KEY = re.compile(r'\bgh[pousr]_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{30,}|-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----')
FORBIDDEN_SUFFIXES = {'.sqlite', '.sqlite-wal', '.sqlite-shm', '.pyc', '.zip', '.gz', '.tar', '.png', '.jpg', '.jpeg', '.pdf', '.key', '.pem', '.p12'}
NETWORK_MODULES = {'requests', 'httpx', 'socket', 'aiohttp', 'openai', 'anthropic', 'subprocess', 'keyring', 'websocket', 'websockets'}

def sha256(p):
    h = hashlib.sha256()
    with p.open('rb') as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()

def file_rows():
    return [{'path': str(p.relative_to(ROOT)), 'bytes': p.stat().st_size,
             'sha256': sha256(p)} for p in sorted(ROOT.rglob('*'))
            if p.is_file() and not p.is_symlink() and p != MANIFEST
            and '.git' not in p.relative_to(ROOT).parts]

def local_links(p, s):
    issues = []
    protected = [(m.start(), m.end()) for m in RX_PROTECTED.finditer(s)]
    for m in RX_LINK.finditer(s):
        if any(a <= m.start() < b for a, b in protected):
            continue
        target = m.group(2).strip().strip('<>')
        if not target or target.startswith(('#', 'https://', 'http://', 'mailto:')):
            continue
        if not (target.startswith(('./', '../', '/')) or
                re.search(r'\.(?:md|json|jsonl|py|pdf|tex|bib|txt|html|csv|sha256)(?:#|:|$)', target, re.I) or
                re.fullmatch(r'[A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)*/', target)):
            continue
        target = urllib.parse.unquote(target.split('#', 1)[0])
        q = (p.parent / target).resolve()
        if not q.is_relative_to(ROOT):
            issues.append('local link leaves repository at line ' + str(s.count('\n', 0, m.start()) + 1))
        elif not q.exists():
            issues.append('missing local link at line ' + str(s.count('\n', 0, m.start()) + 1) + ': ' + target)
    return issues

def validate():
    problems = []
    counts = {'files': 0, 'json': 0, 'python': 0, 'markdown': 0}
    for p in sorted(ROOT.rglob('*')):
        rel = p.relative_to(ROOT)
        if '.git' in rel.parts:
            continue
        if p.is_symlink():
            problems.append((str(rel), 'symlink is not allowed'))
            continue
        if not p.is_file():
            continue
        counts['files'] += 1
        if p.name == '.DS_Store' or p.name.startswith('._') or p.suffix.lower() in FORBIDDEN_SUFFIXES or p.name.startswith('.env'):
            problems.append((str(rel), 'private/binary/sidecar format is excluded'))
        if p.stat().st_size >= 50 * 1024 * 1024:
            problems.append((str(rel), 'file exceeds the publication size limit'))
        try:
            s = p.read_text('utf-8')
        except UnicodeError:
            problems.append((str(rel), 'not valid UTF-8 text'))
            continue
        public_urls = [(m.start(), m.end()) for m in RX_URL.finditer(s)]
        for label, rx in [('personal home path', RX_HOME), ('credential shape', RX_KEY),
                          ('session UUID', RX_UUID), ('bearer value', RX_BEARER), ('email identifier', RX_EMAIL),
                          ('additional credential shape', RX_EXTRA_KEY)]:
            for m in rx.finditer(s):
                if label == 'personal home path' and any(a <= m.start() < b for a, b in public_urls):
                    continue  # Public bibliographic URLs may have a /home/ segment.
                problems.append((str(rel), label + ' at line ' + str(s.count('\n', 0, m.start()) + 1)))
        if '\x00' in s:
            problems.append((str(rel), 'NUL byte'))
        if p.suffix == '.md':
            counts['markdown'] += 1
            problems.extend((str(rel), x) for x in local_links(p, s))
        elif p.suffix == '.json':
            counts['json'] += 1
            try:
                json.loads(s)
            except (ValueError, RecursionError):
                problems.append((str(rel), 'invalid JSON'))
        elif p.suffix == '.py':
            counts['python'] += 1
            try:
                tree = ast.parse(s)
            except SyntaxError:
                problems.append((str(rel), 'invalid Python syntax'))
                continue
            modules = set()
            for n in ast.walk(tree):
                if isinstance(n, ast.Import):
                    modules.update(a.name.split('.')[0] for a in n.names)
                elif isinstance(n, ast.ImportFrom):
                    modules.add((n.module or '').split('.')[0])
            if modules & NETWORK_MODULES:
                problems.append((str(rel), 'network/process client import needs explicit review'))
    return counts, problems

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-manifest', action='store_true', help='write fresh public hashes after checks pass')
    args = parser.parse_args()
    counts, problems = validate()
    if problems:
        for path, why in problems:
            print(path + ': ' + why)
        print(json.dumps({'status': 'FAIL', 'counts': counts, 'problems': len(problems)}))
        return 1
    rows = file_rows()
    if args.write_manifest:
        MANIFEST.write_text(json.dumps({'release_prepared': '2026-10-10',
            'research_snapshot': '2026-10-09', 'hash_algorithm': 'SHA-256',
            'scope': 'Sanitized public bytes; the manifest excludes itself. This is not mathematical proof verification.',
            'files': rows}, indent=2) + '\n')
    elif MANIFEST.exists():
        recorded = json.loads(MANIFEST.read_text())['files']
        current = {r['path']: r for r in rows}
        baseline = {r['path']: r for r in recorded}
        if current != baseline:
            changes = sorted(k for k in current.keys() | baseline.keys() if current.get(k) != baseline.get(k))
            for path in changes:
                print(path + ': differs from release manifest')
            print(json.dumps({'status': 'FAIL', 'manifest_changes': len(changes)}))
            return 1
    else:
        print('No release manifest found. Use --write-manifest after reviewing the prepared files.')
        return 1
    print(json.dumps({'status': 'PASS', 'counts': counts,
        'archived_mathematical_programs_executed': 0, 'network_requests': 0,
        'mathematical_proofs_verified': False}, indent=2))
    return 0

if __name__ == '__main__':
    sys.exit(main())
