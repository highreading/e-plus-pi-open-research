> Archived research record. Read the [current proof status](../../../../docs/PROJECT_STATE.md) and [errata](../../../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# A5, turn 13 — A normalized three-state force connection, finite-boundary exponential forcing, and the remaining half-length obstruction

## Executive conclusions

I do **not** prove that A4’s actual half-length observation


$$
P_J\not\equiv0\pmod{2^{a+d+3}}
$$


on every original index, or on a specified infinite original subsequence. Consequently, I do not obtain an unconditional exclusion of the entire binary family, much less an irrationality proof for $e+\pi$.

There is, however, a new connection that removes the large forced norm baseline **before** making any truncation. It is specific to the original force and retains the actual finite contact response.

Write


$$
\mathfrak f_i=\frac{f_i^0}{R}.
$$


I prove:

1. **The entire normalized first force is $2$-integral**, not merely bounded below by a logarithmic loss:
   

$$
\boxed{\mathfrak f_i\in\mathbb Z_2\quad(i\ge0),\qquad
   \mathfrak f_0\in2\mathbb Z_2,\quad
   \mathfrak f_1\in\mathbb Z_2^\times.}
$$



2. It satisfies an explicit **three-state integral recurrence**. On the original family, every aligned block of eight transfer steps is divisible by $2$. In particular,
   

$$
\boxed{
   v_2(\mathfrak f_i)\ge
   \left\lfloor\frac{i+1}{8}\right\rfloor.
   }
   \tag{E1}
$$


   This is a uniform, original-force filtration independent of $s_2(n)$.

3. At precision $2^K$, the normalized force is determined by fewer than $8K$ coordinates and by
   

$$
h=\frac n2=2001b\pmod{2^{3K}}.
$$


   Its parameter input can therefore be obtained by modular exponentiation in $u$, without reading the binary expansion of $b=9^{18+32u}$. This is a **proved compressed periodic interface for the normalized force**, not for the whole producer.

4. The same three-state connection governs the **complete exponential force after the actual finite factorial baseline has been removed**. Its inhomogeneous term is an explicit observation of precisely the two source-polynomial boundary columns $b-1,b$. The second column is a source column, not an additional contact column.

5. With the actual finite Gram response
   

$$
\mathcal B=A^{-T}\mathcal R^T\mathcal R A^{-1},
$$


   the normalized adjoint and norm obey
   

$$
\boxed{
   2^{a+1}w=\mathcal B\mathfrak f,\qquad
   Q=2^{-2a-2}\mathfrak f^T\mathcal B\mathfrak f.
   }
   \tag{E2}
$$


   These formulas give a genuinely paid finite-window connection for the **excess norm valuation**, without using the derangement sum at precision approximately $3n/2$.

The limitation is exact and important:

> The new compressed-period theorem evaluates the normalized forcing and its transfer matrices. It does not evaluate the necessary finite Gram-response entries, nor the boundary-driven exponential observation. Those still contain the actual finite inverse and the physical endpoint.

Thus this turn supplies a normalized source/response connection and a concrete new response lemma to pursue. It does **not** claim a completed low-cost algorithm for the actual adjoint or a nonzero theorem for $P_J$.

No computation was executed. No accepted producer, high-counter, final-gcd calculation, or optional logarithmic zero is proposed for repetition.

---

# 1. Preserved objects and audit scope

Throughout,


$$
\boxed{
b=9^{18+32u},\qquad n=4002b,\qquad u\ge0.
}
$$


The matrix remains exactly $b\times b$:


$$
0\le i,j<b,
$$


and reconstruction retains exactly the rows


$$
0\le j\le b.
$$



Set


$$
h=\frac n2,\qquad
R=2^h\binom nh,\qquad
\Lambda=\frac{(n!)^2}{2^n},
\qquad
W_j=\binom{n+2}{j},
$$




$$
\phi(z)=1-z+\frac{z^2}{2},
\qquad
\lambda_s=s![z^s]\phi(z)^n.
$$



The actual finite objects are


$$
A_{ij}
=
\sum_{s=0}^{n+i}
\lambda_s\binom{n+i}{s}\binom{2n+i-s}{j},
$$




$$
f_i^0
=
\frac{(n+i)!}{n!}
[t^n](1+2t+2t^2)^n(1+t)^i,
$$


and


$$
(\mathcal Rz)_j=W_j(jz_{j-1}-z_j),
\qquad z_{-1}=z_b=0.
$$



Both corrected columns remain


$$
x=\frac{\mathcal RA^{-1}f^0}{2R},
$$




$$
y=y^E+y^F
=
\frac{\mathcal RA^{-1}(h^e+h^F)+e_0}{4b!}.
$$



Write


$$
x=2^ax_0,\qquad
Q=x_0^Tx_0=2^\nu Q_*,
\qquad Q_*\in\mathbb Z_2^\times.
$$


The closed content theorem is reused:


$$
0\le a\le
\max_{0\le j<b}v_2(W_j)-1
\le \lfloor\log_2(n+2)\rfloor-1.
$$



The actual common adjoint is


$$
w=A^{-T}\mathcal R^Tx_0.
$$


The turn-12 adjoint-content and far-block results are also reused:


$$
0\le c_w:=\min_i v_2(w_i)\le \lfloor\log_2(n+2)\rfloor,
$$




$$
\min_{2n\le j\le2n+b-1}v_2(\theta_j)=c_w.
$$



These are not bounds on $\nu$.

## 1.1 What is accepted from A4 turn 17

The following claims pass at their stated scope and need no rerun:

- the corrected logarithmic source
  

$$
\mathcal L_m=m![z^m]\frac{F(z)}{1-z};
$$


- the refined guard
  

$$
y^F\in2^{B_*}\mathbb Z_2^{b+1},\qquad
  B_*=n-v_2(b!)-1-2s_2(n)-\ell;
$$


- the complete factorial alignment
  

$$
y^E=c_nx+z^E,\qquad
  v_2(c_n)=d=\frac n2-v_2(b!)-1;
$$


- the paid half-length exclusion theorem, conditional on the actual nonzero residue.

The derangement identity is classical binomial inversion applied to the actual adjoint. A4’s derivation and turn 12’s derivation establish the same identity; they are not two discoveries.

A4’s endpoint results on $15^r$ or $105^r$ have a different domain. I do not import them as binary-family bounds.

---

# 2. A normalized first-force recurrence

The first new step is to normalize the force before taking its adjoint contraction.

Define


$$
\boxed{\mathfrak f_i=\frac{f_i^0}{R}.}
\tag{2.1}
$$



For the recurrence proof, the displayed coefficient formula for $f_i^0$ can be considered for all $i\ge0$. This auxiliary scalar sequence does **not** extend the contact matrix: only $0\le i<b$ are used in the actual solve.

## 2.1 The differential operator

Introduce


$$
\mathscr L_n
=
\phi(z)(1-z)\frac{d}{dz}
-\left(n\phi'(z)(1-z)+(n+1)\phi(z)\right).
\tag{2.2}
$$



Its polynomial form is


$$
\boxed{
\mathscr L_n
=
\left(1-2z+\frac32z^2-\frac12z^3\right)\frac{d}{dz}
-\left(1+(n-1)z+\frac{1-n}{2}z^2\right).
}
\tag{2.3}
$$



The exact factorial-moment identity gives


$$
\mathfrak f_i
=
(n+i)![z^{n+i}]
\left(
\frac{2^n}{n!R}\,
\frac{\phi(z)^n}{(1-z)^{n+1}}
\right).
\tag{2.4}
$$


The generating function in parentheses is annihilated by $\mathscr L_n$.

For a general formal series


$$
H(z)=\sum_{m\ge0}\eta_m\frac{z^m}{m!},
$$


coefficient extraction from (2.3) gives


$$
\begin{aligned}
m![z^m]\mathscr L_nH
={}&
\eta_{m+1}-(2m+1)\eta_m\\
&+\frac{m(3m-2n-1)}2\eta_{m-1}\\
&-\frac{m(m-1)(m-n-1)}2\eta_{m-2}.
\end{aligned}
\tag{2.5}
$$



Taking $m=n+i+1$ proves the following.

### Theorem 2.1 — Actual normalized-force connection

For $i\ge0$,


$$
\boxed{
\mathfrak f_{i+2}
=
\alpha_i\mathfrak f_{i+1}
-\beta_i\mathfrak f_i
+\chi_i\mathfrak f_{i-1},
}
\tag{2.6}
$$


where


$$
\alpha_i=2n+2i+3,
$$




$$
\beta_i=\frac{(n+i+1)(n+3i+2)}2,
$$




$$
\chi_i=\frac{i(n+i)(n+i+1)}2.
\tag{2.7}
$$



At $i=0$, $\chi_0=0$, so no value of $\mathfrak f_{-1}$ is needed.

Because $n$ is even, both $\beta_i$ and $\chi_i$ are ordinary integers. Thus this is an integral recurrence; its displayed divisions by $2$ are already paid in the coefficients.

---

# 3. Integrality, eight-step contraction, and a compressed parameter interface

## 3.1 The two seeds

Reuse the exact seed expansions from the first-force witness, now as inputs to the recurrence.

For $r\ge0$, put


$$
T_r(h)=
\frac{2^r(r!)^2}{(2r)!}\binom hr^2.
\tag{3.1}
$$


For nonnegative integer $h$, this is zero when $r>h$, and


$$
v_2(T_r(h))
\ge r-s_2(r).
\tag{3.2}
$$



The exact seed formulas are


$$
\mathfrak f_0=\sum_{r\ge0}T_r(h),
\tag{3.3}
$$




$$
\mathfrak f_1
=
(2h+1)
\left(
\mathfrak f_0+
\sum_{r\ge0}\frac{h-r}{2r+1}T_r(h)
\right).
\tag{3.4}
$$


All denominators in the second sum are odd.

Since $h=2001b$ is odd,


$$
T_0=1,\qquad T_1=h^2
$$


are odd, and all $T_r$, $r\ge2$, are even. The second sum in (3.4) is odd: its $r=0$ term is $h$, its $r=1$ term is even, and all later terms are even.

Hence


$$
\boxed{
\mathfrak f_0\in2\mathbb Z_2,\qquad
\mathfrak f_1\in\mathbb Z_2^\times.
}
\tag{3.5}
$$



Combined with Theorem 2.1, this proves


$$
\boxed{\mathfrak f_i\in\mathbb Z_2\quad(i\ge0).}
\tag{3.6}
$$



In particular, on the actual contact range, which contains $i=1$,


$$
\boxed{
\min_{0\le i<b}v_2(f_i^0/R)=0.
}
\tag{3.7}
$$



Thus the normalized contact force $f^0/(2R)$ has minimum valuation **exactly** $-1$, not merely at most $-1$.

## 3.2 A uniform eight-step contraction

Let


$$
S_i=
\begin{pmatrix}
\mathfrak f_{i+1}\\
\mathfrak f_i\\
\mathfrak f_{i-1}
\end{pmatrix},
\qquad
T_i=
\begin{pmatrix}
\alpha_i&-\beta_i&\chi_i\\
1&0&0\\
0&1&0
\end{pmatrix}.
\tag{3.8}
$$


Then


$$
S_{i+1}=T_iS_i.
$$



On the original family,


$$
n\equiv2\pmod4.
$$


Modulo $2$, $\alpha_i=1$, and the pairs $(\beta_i,\chi_i)$, according to $i\bmod4$, are


$$
(0,0),\quad(0,0),\quad(1,0),\quad(1,1).
\tag{3.9}
$$



Multiplying these four explicitly determined matrices gives


$$
\boxed{
T_{4r+3}T_{4r+2}T_{4r+1}T_{4r}
\equiv
\begin{pmatrix}
0&0&0\\
0&0&0\\
1&0&0
\end{pmatrix}
\pmod2.
}
\tag{3.10}
$$


The matrix on the right has square zero. Therefore


$$
\boxed{
T_{8r+7}\cdots T_{8r}\in
2\,\operatorname{Mat}_3(\mathbb Z_2).
}
\tag{3.11}
$$



No computation is needed for this assertion: (3.9)–(3.10) are direct symbolic matrix multiplication over $\mathbb F_2$.

Starting with the integral seeds and applying successive blocks proves:

### Theorem 3.1 — Uniform normalized-force filtration

For every original $n$ and every $i\ge0$,


$$
\boxed{
v_2(\mathfrak f_i)\ge
\left\lfloor\frac{i+1}{8}\right\rfloor.
}
\tag{3.12}
$$



Equivalently, for every $K\ge1$,


$$
\boxed{
\mathfrak f_i\equiv0\pmod{2^K}
\qquad(i\ge8K-1).
}
\tag{3.13}
$$



This statement concerns the actual normalized first force. It is not an assertion about arbitrary primitive vectors.

## 3.3 Explicit parameter-digit cost

The seed series have rapidly increasing coefficient valuations. Since


$$
r-s_2(r)\ge\left\lfloor\frac r2\right\rfloor,
$$


both seeds modulo $2^K$ are determined by


$$
0\le r<2K.
\tag{3.14}
$$



For such $r$, $\binom hr\bmod2^K$ is determined by


$$
h\bmod2^{K+v_2(r!)}.
$$


A simple sufficient common input is therefore


$$
\boxed{h\bmod2^{3K}.}
\tag{3.15}
$$



The recurrence coefficients modulo $2^K$ require only $n\bmod2^{K+1}$ and the corresponding residue of $i$. The input (3.15) already pays this.

Consequently:

### Theorem 3.2 — Compressed normalized-force interface

At precision $2^K$:

- the seeds require fewer than $2K$ terms;
- fewer than $8K$ force coordinates can be nonzero;
- all of these coordinates are determined by $h\bmod2^{3K}$.

On the original exponents,


$$
h=2001\cdot9^{18}(9^{32})^u.
$$


Thus the required parameter residue is computable by modular exponentiation, using $O(\log(u+2))$ modular multiplications at $O(K)$-bit precision.

An elementary implementation of the seed and recurrence evaluation uses polynomially many $K$-bit operations; a conservative bound is


$$
O\!\left(K^2+\log(u+2)\right)
$$


modular multiplications, with intermediate precision at most $3K+O(1)$ bits.

The sufficient exponent period is


$$
\boxed{
u\longmapsto u+2^{\max(3K-8,0)},
}
\tag{3.16}
$$


because $v_2(9^{32}-1)=8$.

### Exact scope of the compression

This is a genuine answer to part of the high-word-cost issue:

> The normalized force at fixed precision does not require a scan of the full binary word of the original parameter.

It is **not** a periodicity theorem for $A^{-1}$, $w$, $Q$, or $E$.

For the physical force vector, the cutoff $i<b$ must still be imposed. When $b\ge8K-1$, its nonzero part modulo $2^K$ is wholly contained in the proved prefix. When this inequality fails, the original endpoint $b-1$ remains the endpoint.

---

# 4. A complete exponential connection with exactly two boundary source columns

The preceding homogeneous recurrence also has an exact inhomogeneous counterpart for the complete exponential source.

This is where the finite terminal and the factorial baseline must be retained.

## 4.1 Source-column generating polynomials

Put


$$
G_n(z)=e^z\phi(z)^n
$$


and define


$$
C_j(z)=
\sum_{r=0}^{j}\binom n{j-r}\frac{z^r}{r!}.
\tag{4.1}
$$


Equivalently,


$$
\sum_{j\ge0}C_j(z)t^j=(1+t)^ne^{tz}.
$$



Then the complete source columns satisfy


$$
\boxed{
(\mathbf a_j)_i
=
(n+i)![z^{n+i}]\,G_n(z)C_j(z).
}
\tag{4.2}
$$



For $j<b$, these are the actual columns of $A$. The polynomial $C_b$ below represents the next source column only; no contact equation is added.

Define the finite factorial polynomial


$$
U_b(z)=\sum_{j=0}^{b-1}j!\,C_j(z).
\tag{4.3}
$$



Two elementary identities are


$$
C_j'=C_{j-1}
$$


and


$$
(j+1)C_{j+1}=(n+z-j)C_j+zC_{j-1}.
$$


They imply the exact finite telescoping identity


$$
\boxed{
(1-z)U_b'-(n+z)U_b
=
1-b!\bigl(C_{b-1}+C_b\bigr).
}
\tag{4.4}
$$



The two boundary polynomials on the right are essential.

## 4.2 The complete exponential generating function

Let


$$
g_n(z)=\frac{d^n}{dz^n}\left(\frac{e^z}{1-z}\right).
$$


Its exponential coefficients are


$$
g_n(z)=\sum_{k\ge0}\mathcal D_{n+k}\frac{z^k}{k!}.
$$


The recurrence for $\mathcal D_m$ gives


$$
\boxed{
(1-z)g_n'-(n+1)g_n=e^z.
}
\tag{4.5}
$$



Thus


$$
h_i^e=(n+i)![z^{n+i}]\phi(z)^ng_n(z),
$$


and


$$
\mathscr L_n\bigl(\phi^ng_n\bigr)=e^z\phi^{n+1}.
\tag{4.6}
$$



On the other hand,


$$
\mathscr L_n(G_nU_b)
=
G_n\phi\bigl((1-z)U_b'-(n+z)U_b\bigr).
$$


Using (4.4),


$$
\mathscr L_n(G_nU_b)
=
e^z\phi^{n+1}
\left(1-b!(C_{b-1}+C_b)\right).
\tag{4.7}
$$



Subtracting the **whole** identities (4.6)–(4.7), then dividing by the already present $b!$, proves


$$
\boxed{
\mathscr L_n
\left(
\frac{\phi^ng_n-G_nU_b}{b!}
\right)
=
e^z\phi^{n+1}(C_{b-1}+C_b).
}
\tag{4.8}
$$



This is not coefficientwise deletion of a derangement or aligned residual tail. It is an exact differential identity after the complete finite factorial baseline has been subtracted.

## 4.3 The normalized complete force

Let


$$
t=(j!)_{0\le j<b},
\qquad
k_i=\frac{h_i^e-(At)_i}{b!}.
\tag{4.9}
$$


The full factorial source identity gives


$$
\boxed{
k_i
=
\sum_{j=b}^{2n+i}\frac{j!}{b!}(\mathbf a_j)_i\in\mathbb Z.
}
\tag{4.10}
$$



Define


$$
\Gamma_i
=
(n+i+1)![z^{n+i+1}]
e^z\phi(z)^{n+1}\bigl(C_{b-1}(z)+C_b(z)\bigr).
\tag{4.11}
$$


These are integral coefficients in divided-power coordinates.

Equation (4.8), extracted as in §2, proves:

### Theorem 4.1 — Complete finite-boundary exponential connection

For $0\le i\le b-3$,


$$
\boxed{
k_{i+2}
=
\alpha_i k_{i+1}
-\beta_i k_i
+\chi_i k_{i-1}
+\Gamma_i.
}
\tag{4.12}
$$


At $i=0$, the coefficient of $k_{-1}$ is zero.

The recurrence uses:

- the complete exponential source;
- the actual subtraction $At$;
- exactly the contact range $0,\ldots,b-1$;
- both boundary source polynomials $C_{b-1}$ and $C_b$.

There is no recurrence step through an invented contact row $b$.

## 4.4 The physical terminal

Since


$$
\mathcal Rt=-e_0+b!W_be_b,
$$


the second column is exactly


$$
\boxed{
y^E=\frac14\left(\mathcal RA^{-1}k+W_be_b\right).
}
\tag{4.13}
$$


Therefore


$$
\boxed{
4E=w^Tk+W_bx_{0,b}.
}
\tag{4.14}
$$



The term $W_bx_{0,b}$ is the actual physical terminal. It has not been absorbed into an extra contact condition.

---

# 5. The aligned residual satisfies the same boundary-driven connection

The complete factorial alignment says


$$
h^e=\sigma_n\Lambda f^0+\rho,
\qquad
c_n=\frac{\Lambda R}{2b!}\sigma_n.
$$


Since $f^0=R\mathfrak f$,


$$
\frac{\sigma_n\Lambda f^0}{b!}
=
2c_n\mathfrak f.
$$



Define


$$
\boxed{
r=k-2c_n\mathfrak f
=\frac{\rho-At}{b!}.
}
\tag{5.1}
$$


The previous sections prove $\mathfrak f\in\mathbb Z_2^b$, and $c_n\in\mathbb Z$, so


$$
r\in\mathbb Z_2^b.
$$



Because $\mathfrak f$ satisfies the homogeneous recurrence, $r$ satisfies the **same** inhomogeneous recurrence (4.12), with the same $\Gamma_i$. Its initial values are the complete, already-subtracted values in (5.1).

Moreover,


$$
\boxed{
4\Psi=w^Tr+W_bx_{0,b}.
}
\tag{5.2}
$$


Combining this with (4.14) and


$$
w^T\mathfrak f=2^{a+1}Q
$$


gives


$$
4E
=
2^{a+2}c_nQ+4\Psi,
$$


or


$$
E=c_n2^aQ+\Psi,
$$


with exactly the previously audited scalar and unit.

### What has changed

The forced baseline has now been removed at the level of a shared integral connection:

- $\mathfrak f$ is a homogeneous solution;
- $k$ is the complete boundary-driven exponential solution;
- $r=k-2c_n\mathfrak f$ is the complete aligned residual solution.

This organization avoids trying to truncate the derangement moment or its integerized residual coefficients.

It does not imply that $w^Tr+W_bx_{0,b}$ is nonzero at the required depth.

---

# 6. Finite-memory propagation—and its exact limitation

The eight-step contraction applies to the homogeneous part of every recurrence (4.12).

For a state


$$
K_i=
\begin{pmatrix}
k_{i+1}\\k_i\\k_{i-1}
\end{pmatrix},
$$


one has


$$
K_{i+1}=T_iK_i+e_1\Gamma_i.
\tag{6.1}
$$



Fix a modulus $2^K$. At a block-aligned starting index, a product of $8K$ homogeneous transfer steps is divisible by $2^K$. Thus sufficiently far from the left boundary, the state modulo $2^K$ depends only on a window of at most


$$
\boxed{8K+7}
\tag{6.2}
$$


recent forcing values $\Gamma_i$, not on the remote initial state.

More explicitly, for a state index $r\ge8K$, set


$$
s=8\left(\left\lfloor\frac r8\right\rfloor-K\right).
$$


Then


$$
\begin{aligned}
K_r\equiv
\sum_{t=s}^{r-1}
T_{r-1}\cdots T_{t+1}e_1\Gamma_t
\pmod{2^K},
\end{aligned}
\tag{6.3}
$$


provided all the displayed indices remain within the original recurrence range.

This is a proved local-memory statement with an explicit state dimension and window length.

### The unresolved input is not hidden

The forcing values


$$
\Gamma_i
=
(n+i+1)![z^{n+i+1}]
e^z\phi^{n+1}(C_{b-1}+C_b)
$$


still contain the actual boundary index $b$. The normalized-force periodicity of §3 does not evaluate them.

Likewise, an observation


$$
w^Tk+W_bx_{0,b}
$$


is not a single state of the recurrence. It is a contraction against the actual finite adjoint over all contact rows.

Accordingly, (6.3) is **not** yet a compressed algorithm for $E$. It specifies exactly which additional observable response must be compressed.

---

# 7. An actual normalized Gram-response connection

The common adjoint can now be connected to the normalized force without the $3n/2$-scale derangement baseline.

Define the actual finite matrices and vector


$$
\boxed{
\mathcal B=A^{-T}\mathcal R^T\mathcal R A^{-1},
}
\tag{7.1}
$$




$$
\boxed{
v_{\mathrm{term}}
=
bW_b^2A^{-T}e_{b-1}.
}
\tag{7.2}
$$


Both retain the complete finite reconstruction, including its last row.

Since


$$
x_0=2^{-a-1}\mathcal RA^{-1}\mathfrak f,
$$


we obtain the exact identities


$$
\boxed{
2^{a+1}w=\mathcal B\mathfrak f,
}
\tag{7.3}
$$




$$
\boxed{
Q=2^{-2a-2}\mathfrak f^T\mathcal B\mathfrak f.
}
\tag{7.4}
$$



From (4.13),


$$
\boxed{
E
=
2^{-a-3}
\mathfrak f^T
\left(\mathcal Bk+v_{\mathrm{term}}\right).
}
\tag{7.5}
$$


Similarly,


$$
\boxed{
\Psi
=
2^{-a-3}
\mathfrak f^T
\left(\mathcal Br+v_{\mathrm{term}}\right).
}
\tag{7.6}
$$



These are actual forced connections, not identities for a freely selected adjoint.

The alignment is visible inside the response:


$$
\mathcal Bk+v_{\mathrm{term}}
=
2c_n\mathcal B\mathfrak f+
\left(\mathcal Br+v_{\mathrm{term}}\right).
\tag{7.7}
$$



## 7.1 Paid finite-window norm extraction

Because $A^{-1}$ and $\mathcal R$ are $2$-integral,


$$
\mathcal B\in\operatorname{Mat}_b(\mathbb Z_2).
$$



To determine $Q\bmod2^K$, put


$$
L_N=K+2a+2,
\qquad
I_N=\min\{b-1,\ 8L_N-2\}.
\tag{7.8}
$$


By Theorem 3.1, the entries of $\mathfrak f$ after $I_N$ are divisible by $2^{L_N}$. Hence


$$
\boxed{
Q\equiv
2^{-2a-2}
\mathfrak f_{\le I_N}^{\,T}
\mathcal B_{\le I_N,\le I_N}
\mathfrak f_{\le I_N}
\pmod{2^K}.
}
\tag{7.9}
$$



The numerator is evaluated modulo $2^{L_N}$, and only then is the whole division by $2^{2a+2}$ performed. No entrywise inverse of that power of $2$ is used.

This is a connection for the **primitive norm excess** itself. The automatic valuation


$$
\frac{3n}{2}-s_2(n)+a+1
$$


of the complete derangement observation is absent because it was removed exactly through the normalized original force.

There is also the adjoint form


$$
Q=2^{-a-1}w^T\mathfrak f.
$$


If the actual $w$ is already available, $Q\bmod2^K$ needs only


$$
i\le\min\{b-1,\ 8(K+a+1)-2\},
\tag{7.10}
$$


with the whole $2^{a+1}$-division paid.

## 7.2 Paid finite-window exponential extraction

Put


$$
\mathcal E=\mathcal Bk+v_{\mathrm{term}}.
$$


This vector is $2$-integral. To determine $E\bmod2^K$, set


$$
L_E=K+a+3,
\qquad
I_E=\min\{b-1,\ 8L_E-2\}.
$$


Then


$$
\boxed{
E\equiv
2^{-a-3}
\mathfrak f_{\le I_E}^{\,T}\mathcal E_{\le I_E}
\pmod{2^K},
}
\tag{7.11}
$$


with evaluation modulo $2^{L_E}$ before the whole division.

Thus both observations have finite-window normalized interfaces. But the required response data are different:

- the norm needs a principal head block of $\mathcal B$;
- the exponential observation needs the head of the **complete response**
  

$$
\mathcal Bk+v_{\mathrm{term}}.
$$



Replacing the latter by a head block of $\mathcal B$ alone would omit the complete boundary-driven force.

---

# 8. Why this does not yet evaluate the half-length observation

A4’s theorem remains


$$
P_J\not\equiv0\pmod{2^{a+d+3}}
\quad\Longrightarrow\quad
\delta_2\le d-\nu\le d,
$$


where


$$
J\le\frac n2+a+s_2(b)+\ell+2.
$$



Nothing proved above supplies the required nonzero digit.

There are two distinct obstructions.

## 8.1 The source compression is not response compression

The normalized force modulo $2^K$ has an explicit compressed periodic interface. The finite response


$$
\mathcal B=A^{-T}\mathcal R^T\mathcal R A^{-1}
$$


still involves:

- the inverse of the original $b\times b$ contact matrix;
- all $b+1$ physical reconstruction rows;
- the actual endpoint contribution to $\mathcal R^T\mathcal R$.

There is no proved theorem here that determines the required head response entries from a bounded residue of $b$.

The exact new missing object is therefore not “the whole high word” in the abstract. It is the finite Gram-response head, together with the boundary-driven response in (7.11).

## 8.2 Fixed precision still does not become linear precision

For a fixed $K$, (7.9) and (7.11) involve $O(K+a)$ input coordinates.

At a linear target $K\asymp n$, however,


$$
8(K+2a+2)>b
$$


throughout the relevant range because $b=n/4002$. The cutoff then saturates at the **entire** contact vector.

Thus the new force filtration is useful for genuinely bounded precision. It does not turn a fixed-depth theorem into the desired linear-depth bound on $\nu$ or on resonance.

Likewise, applying (7.11) directly at A4’s half-length precision does not produce a small state space: its force window has already reached the finite boundary.

## 8.3 No forbidden coefficientwise disappearance has occurred

The turn-12 far-tail theorem remains fully compatible with this report.

The derangement and integerized residual observations still have shallow actual far-tail terms. Those terms have not been discarded. Instead, equations (7.4)–(7.6) were derived after the complete factorial moment and complete baseline subtraction.

The new truncation is a proved filtration of the **normalized contact force $\mathfrak f$**. It is not a truncation of the far source coefficients $\theta_j$.

---

# 9. A concrete follow-on lemma

The previous outstanding target can now be narrowed to a particular finite response, rather than another unspecified high-word scan.

## 9.1 Normalized response lemma

A useful next theorem would provide, at a specified bounded precision $2^L$,

1. the head block
   

$$
\mathcal B_{0:I,0:I}\pmod{2^L};
$$


2. the head response
   

$$
\left(\mathcal Bk+v_{\mathrm{term}}\right)_{0:I}
   \pmod{2^L};
$$


3. an explicit dependence on the original exponent $u$, including any necessary nonperiodic boundary state;
4. a proved resource bound for obtaining those entries without traversing all $b$ contact rows.

Here $I$ is the paid index in (7.8) or (7.11), not an independently shortened contact cutoff.

Such a lemma would combine with the now-proved $O(K)$-size normalized-force interface to evaluate actual primitive norm or exponential digits.

It must preserve


$$
\mathcal R^T\mathcal R,
\qquad
v_{\mathrm{term}}=bW_b^2A^{-T}e_{b-1},
\qquad
\Gamma_i
$$


from the complete two-boundary source.

A generic automaton existence theorem, a determinant-unit argument, or a new congruence equivalent to (7.9) is not enough. The response entries and their cost must be supplied.

## 9.2 The nonzero version needed for A4’s route obstruction

For an actual original index, it would suffice to find any $K\le a+d+1$ such that the completely paid evaluation in (7.11) yields


$$
E\not\equiv0\pmod{2^K}.
$$


The logarithmic guard then protects that nonzero digit, and A4’s norm-independent argument applies.

This can be substantially cheaper than evaluating all digits through the half-length threshold—but only if a nonzero digit is actually found or proved. No such digit is asserted here.

---

# 10. Resource accounting and bounded arithmetic

## 10.1 What is now genuinely feasible

The normalized first-force interface is a proved bounded arithmetic task.

Its inputs are


$$
u,\quad K,\quad
h\bmod2^{3K}
=
2001\cdot9^{18+32u}\bmod2^{3K}.
$$


Its verifiable output is


$$
(\mathfrak f_0,\ldots,\mathfrak f_{8K-2})\bmod2^K,
$$


followed by the proof-forced zero tail.

The costs are polynomial in $K$ and logarithmic in the encoded exponent $u$, not linear in the word length of $b$.

This remains true even in a separator regime where the actual binary word of $b$ would be enormous.

## 10.2 What has not been made feasible

The following are **not** supplied by that computation:

- $a$;
- the actual head of $w$;
- the necessary head Gram-response block;
- the response to $\Gamma_i$;
- a nonzero digit of $P_J$;
- a primitive denominator or whole-error evaluation.

The source-interface computation alone would therefore not settle the assigned target. I do not commission it merely to generate another receipt for a quantity whose structural properties have already been proved.

For scale only, at $u=0$ one has $a\le68$. If a future response lemma targeted $Q\bmod2^{64}$, a conservative paid modulus would be $2^{202}$, and the head size in (7.8) would be at most $1615$. Storing such a head block is not intrinsically prohibitive. **Computing it from the original finite matrix is the unproved step.** This is a resource illustration, not a proposed original-size solve or a claimed evaluation.

## 10.3 Computation status

**No bounded exact arithmetic calculation is required to prove the new results in this report, and none is commissioned.**

In particular, there is no request to rerun:

- the old precision-32 producer;
- accepted high-counter or high-block calculations;
- any final gcd or denominator;
- the optional $b=9,\ K=20000$ logarithmic zero;
- any accepted whole-error evaluation.

The unknown digits remain those of the actual response in §9. A feasible procedure for those digits has not yet been proved, so an unevaluated full-matrix specification is not presented as a bounded proposal.

---

# 11. The actual denominator and whole error remain unchanged

For completeness, retain


$$
\omega_j=j!W_j,
$$




$$
u_j=\frac{2\Lambda R\,x_j}{\omega_j},
\qquad
v_j=\frac{4b!\,y_j}{\omega_j}.
$$


The least simultaneous clearer is the actual one:


$$
d_B=
\operatorname{lcm}_{0\le j\le b}
\{\operatorname{den}(u_j),\operatorname{den}(v_j)\}.
$$



No reconstructed row content is divided out in this binary producer.

The weighted producer and all-prime reduction remain


$$
A_B=d_B^2\,4\Lambda^2R^2N,
\qquad
H_B=d_B^2\,8\Lambda Rb!H,
$$




$$
\boxed{
g_B=\gcd(A_B,|H_B|),\qquad
q_n=A_B/g_B,\qquad p_n=H_B/g_B.
}
$$



For every prime $p$,


$$
v_p(q_n)
=
\max\{v_p(\mathscr D_n)+v_p(N)-v_p(H),0\},
\qquad
\mathscr D_n=\frac{\Lambda R}{2b!}.
$$



At $2$,


$$
v_2(q_n)=\max\{C_n-\delta_2,0\},
\qquad
C_n=\frac{3n}{2}-v_2(b!)-s_2(n)-1.
$$


The retained ternary theorem is


$$
v_3(q_n)=n-\frac{b+15}{2}.
$$



If the half-length nonzero certificate is established on an infinite original sequence, A4’s theorem gives $\delta_2\le d$. Under the retained whole-error theorem,


$$
\epsilon_n=\frac{p_n}{q_n}-(e+\pi),
\qquad
\log|\epsilon_n|=-\beta n+o(n),
$$


with eventual nonvanishing, that sequence satisfies


$$
|q_n\epsilon_n|\longrightarrow\infty.
$$



This remains a conditional route obstruction.

Conversely, a favorable binary branch would still have to pay


$$
\sum_{p\ne2,3}v_p(q_n)\log p.
$$


Nothing in the new normalized connection controls that nonnegative contribution.

The evaluated form remains the whole, same-index form


$$
\boxed{
q_n(e+\pi)-p_n=-q_n\epsilon_n.
}
$$


The exponential contraction by itself is not substituted for it.

Whenever a requested digit exceeds the logarithmic guard $B_*$, the complete original $F/(1-z)$ logarithmic contribution remains compulsory.

---

# 12. Proof-status ledger

| Statement | Status |
|---|---|
| Correct source $F/(1-z)$ and refined guard $B_*$ | Reused after audit |
| Actual first-column and adjoint-content bounds | Closed results, reused |
| Far source-block content and shallow residual obstruction | Closed turn-12 results, retained |
| Derangement norm identity | Classical binomial inversion at the actual adjoint; not a second discovery |
| A4 half-length exclusion | Rigorous conditional theorem |
| Uniform or infinite-original nonzero half-length residue | **Not proved** |
| Integral recurrence for $\mathfrak f_i=f_i^0/R$ | **New explicit derivation** |
| $\mathfrak f_i\in\mathbb Z_2$, with $\mathfrak f_1$ a unit | **Proved** |
| Uniform eight-step contraction | **Proved symbolically** |
| $v_2(\mathfrak f_i)\ge\lfloor(i+1)/8\rfloor$ | **New original-force filtration** |
| Compressed periodic interface for normalized force | **Proved with parameter and state costs** |
| Complete exponential connection with $C_{b-1}+C_b$ | **New exact finite-boundary identity** |
| Same connection for the whole aligned residual | **Proved after whole baseline subtraction** |
| Actual normalized Gram-response formulas | **Proved with complete content payment** |
| Low-cost evaluation of the required finite response | Open |
| Linear bound on $\nu$ or normalized resonance | Open |
| Favorable all-prime, whole-error certificate | Not established |
| Irrationality or rationality of $e+\pi$ | Unresolved |

---

## Conclusion

The actual half-length nonzero observation remains unevaluated. I have not converted A4’s conditional exclusion into a nonzero theorem.

The new proved result is a normalized original-force connection:


$$
\boxed{
\mathfrak f_i=\frac{f_i^0}{R}\in\mathbb Z_2,\qquad
v_2(\mathfrak f_i)\ge
\left\lfloor\frac{i+1}{8}\right\rfloor,
}
$$


with an explicit three-state recurrence and a compressed parameter interface costing polynomial work in the precision and logarithmic work in the encoded exponent $u$.

The complete exponential source, after the actual finite factorial subtraction, satisfies the same connection with the exact boundary forcing


$$
\boxed{
e^z\phi(z)^{n+1}\bigl(C_{b-1}(z)+C_b(z)\bigr).
}
$$


The physical terminal survives as $W_bx_{0,b}$, and the complete factorial-aligned residual is subtracted as a whole.

These identities give a paid normalized connection for the actual adjoint, primitive norm excess, and exponential observation:


$$
\boxed{
2^{a+1}w=\mathcal B\mathfrak f,\qquad
Q=2^{-2a-2}\mathfrak f^T\mathcal B\mathfrak f,
}
$$




$$
\boxed{
E=2^{-a-3}
\mathfrak f^T(\mathcal Bk+v_{\mathrm{term}}).
}
$$



The exact remaining bottleneck is now the **finite Gram and boundary-driven response**, not the normalized force:

1. evaluate or bound the required actual response entries at paid precision;
2. obtain a nonzero exponential digit, or control the resulting primitive norm excess and complete resonance;
3. retain the logarithmic source whenever its guard is exceeded;
4. pay every prime in the actual primitive denominator against the whole nonzero same-index error.

No bounded calculation is needed for the proofs above. No feasible new calculation of the unresolved response digits has yet been justified.

**The requested nonzero theorem and linear cancellation bounds remain open. No unconditional proof or disproof of the irrationality of $e+\pi$ follows.**
