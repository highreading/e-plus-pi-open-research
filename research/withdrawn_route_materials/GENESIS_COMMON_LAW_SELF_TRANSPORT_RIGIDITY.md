> Archived research record. Read the [current proof status](../../docs/PROJECT_STATE.md) and [errata](../../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Genesis root candidate G-R10: common rational-time self-transport

2026-10-02. Author support deduction, no independent audit or main proof. The finite rational self-transport core is classical and discarded. It is not a retained Genesis tool.

## Candidate operation

A possible arithmetic replica would use one time change phi for both actual laws E(z)=exp(z), A(z)=4 atan(z), with a rational multiplicative gauge in E and a rational additive gauge in A. The hoped-for dilation would make the exponential and angle laws replicate together rather than merely recombining their endpoints. The complete allowed class below has no nontrivial positive dilation.

## ALL-class rigidity theorem

Let phi in C(z) be nonconstant, R in C(z) nonzero, B in C(z), and n,v in C constants. Suppose on a common analytic germ

exp(phi(z)) = R(z) exp(n*z),
A(phi(z)) = v*A(z)+B(z).

Then phi(z)=z or -z, n=v=1 or -1 accordingly, and R=1. The rational B is constant; with both atan germs normalized at0, B=0. Continued branches can differ by the corresponding constant integral multiple of4*pi, which is not suppressed in the statement.

Proof. Logarithmic differentiation of the exponential identity gives phi'-n=R'/R. The derivative of a rational function has no simple-pole coefficient at any finite point. In contrast, at every zero or pole of R, R'/R has a simple pole with nonzero integral residue. Thus R has no finite zero or pole and is constant. Consequently phi=n*z+c, with n nonzero because phi is nonconstant, and R=exp(c).

Differentiate the second identity:

B' = 4*n/(1+(n*z+c)^2) - 4*v/(1+z^2).

The first term has nonzero simple residues at the two distinct points (-c+i)/n and (-c-i)/n. Since B' has zero residues everywhere, they must be exactly the two points i,-i in the second term. This also forces v nonzero. Comparing the unordered pairs gives c=0 and n=1 or -1. The remaining rational differential is 4*(n-v)/(1+z^2), so v=n. Hence B'=0 and R=1. Branch normalization supplies the final constant statement.

The argument even allows arbitrary complex rational gauges, not just arithmetic ones. No rationality hypothesis on S is used. It excludes only the displayed law-preserving scalar self-transport class, not transformations mixing the two states, nonlinear state maps, independent time changes, analytic nonrational arguments, or infinite operations.

In particular substitution z/2 can create exp(z/2), but cannot replicate A with multiplier1/2 up to a rational additive gauge. A common higher integer-time replica is unavailable in this class. Separate multiplication and angle-addition laws do not give a synchronized arithmetic output.

## Fresh archive and literature gate

Fresh archive queries covered common symmetry/replication/dilation, simultaneous exponential or arctan transport, rational self-transport, and affine arctan symmetry across sources/work. Prior overlap includes Agent1's positive simultaneous subdivision warning and root G-R8's essential-singularity monomial normal form. No prior all-complex-rational-gauge classification in this exact form was located in the bounded query; that is not a novelty claim.

Fresh public queries covered rational exponential algebraicity/essential singularities, rational logarithmic derivative residues and arctangent primitives, and common affine exponential/arctan symmetries. Opened official NIST DLMF4.23 for atan logarithmic forms and the Berkeley author complex-analysis lecture20 for singularity background. More directly opened Maxwell Rosenlicht, *Integration in Finite Terms* (1972), full11-page scan at https://www.cs.ru.nl/~freek/courses/mfocs-2012/risch/Integration%20in%20Finite%20Terms--Maxwell%20Rosenlicht.pdf; read printedpp964--965 and967--970. Its differential-field/logarithmic-derivative and pole-order separation arguments are the essential public operator core. No numerical algebraicity theorem is imported from its functional statements. The exact classification above is an elementary specialization of this established mechanism and is DISCARD as a new Genesis route.

No bounded experiment is needed for the all-class proof. The main rationality problem remains open.

