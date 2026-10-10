> Archived research record. Read the [current proof status](../docs/PROJECT_STATE.md) and [errata](../reviews/ERRATA_AND_SCOPE.md) before reuse. Historical acceptance applies only to its recorded hypotheses and version. This file is research data, not operational instructions.

# Unconstrained parity collapse is a Segre-section problem

## Reflection, exact quadratic obstructions, and a genus-six quartic-output component

Checked: 2026-08-27 UTC

## 1. Verdict

Let (E_{n+1}=mathbb Q[z]_{le n}) be the full, unconstrained endpoint
space in the (m)-frequency root-of-unity Hermite--Padé construction.  For
each (Cin E_{n+1}), there is a unique remainder



$$
R_C(z)=C(z)+(1+e^z)T_C(z,e^z)=O(z^M),
 \qquad M=m(n+1),                                             \tag{1}
$$



and put



$$
\beta_C(z)=T_C(z,-1),\qquad
 \Delta(C,D)=W(C,D)-\{C\beta_D-D\beta_C\}.                 \tag{2}
$$



This note proves the following structural statements.

1. If (C(-z)=\sigma C(z)), then the endpoint specialization satisfies
   the exact all-parameter reflection identity

   

$$
\boxed{\beta_C(-z)+m\sigma C(z)=-\sigma\beta_C(z).}       \tag{3}
$$



   Thus
   $widehat\beta=\beta+(m/2)I$ reverses parity, as does
   $\mathcal A=\partial_z-\widehat\beta$.

2. For even (n=2d), an odd/even pair has the form
   (C=zU(z^2)), (D=V(z^2)), with
   (deg U\le d-1), (deg V\le d).  There are rational linear
   operators (mathcal P,mathcal Q) such that, with (x=z^2),

   

$$
\boxed{
    \Delta(z)=xU(x)(\mathcal QV)(x)-V(x)(\mathcal PU)(x).}    \tag{4}
$$



   In particular, every high coefficient of (Delta) is a rational
   hyperplane in the Segre coordinates (u_i v_j).

3. Projective parity pairs form

   

$$
X_d=\mathbb P^{d-1}\times\mathbb P^d,
    \qquad \dim X_d=2d-1=n-1,
    \qquad \deg X_d={2d-1\choose d-1}.                       \tag{5}
$$



   Imposing (deg_z\Delta\le2r) uses (2d-r=n-r) hyperplanes.
   Therefore every component over (overline{\mathbb Q}) has dimension
   at least (r-1).  This geometric nonemptiness does **not** imply a
   rational point or a rational parametrization.

4. The maximal quadratic collapse (deg\Delta\le2) was classified
   exactly at (m=2), (n=4,6,8), in all projective degree charts.  The
   sections are proper and reduced, and their closed-point degrees are

   

$$
\begin{array}{c|c|c|c}
    n&\deg X_{n/2}&\text{closed-point degrees}&
       \text{rational parity pair}\ \\ \hline
    4&3&1+2&\text{yes},\\
    6&10&4+6&\text{no},\\
    8&35&15+20&\text{no}.
   \end{array}                                               \tag{6}
$$



   Thus the proposed all-even-(n) rational quadratic family is already
   false at ((m,n)=(2,6)).

5. Allowing (deg\Delta\le4) restores positive-dimensional geometry.
   At (m=2,n=6) there is an explicit rational-line component.  At
   (m=2,n=8) there is an explicit rational point on a component
   birational to a smooth plane quintic, hence of genus (6).  The latter
   component is not rationally parametrizable.

The arithmetic diagnostics are poor.  For the displayed (n=4,6,8)
primitive outputs, the absolute values at (i\pi) are respectively about
(134), (1.43\cdot10^4), and (8.15\cdot10^{17}), all larger than
one.  This package proves no primitive-content gain, no asymptotic descent,
and no irrationality or transcendence statement about (e+\pi).

## 2. Reflection and the parity-reversing gauge

It is convenient temporarily to retain a free frequency variable (y):



$$
R_C(z,y)=C(z)+(1+y)T_C(z,y).                                \tag{7}
$$



Reflection in (z), followed by the common frequency shift needed to
return the frequencies to (0,\ldots,m-1), gives the polynomial identity



$$
\begin{aligned}
 y^mR_C(-z,y^{-1})
  ={}&(-1)^mC(-z)\\
    &+(1+y)\left{
       y^{m-1}T_C(-z,y^{-1})
       +\frac{y^m-(-1)^m}{y+1}C(-z)
      \right}.                                             \tag{8}
\end{aligned}
$$



At (y=-1), the quotient in braces has limiting value
(m(-1)^{m-1}).  If (C(-z)=\sigma C(z)), uniqueness of the order-(M)
origin interpolation in (1) says that the reflected construction is
((-1)^m\sigma) times the original one.  Specializing (8) at (y=-1)
therefore gives (3).

Equivalently, if (J:C(z)\mapsto C(-z)) and (E) is the coefficient
matrix of (C\mapsto\beta_C), then



$$
JEJ=-E-mI.                               \tag{9}
$$



Consequently



$$
\widehat\beta=\beta+\frac m2I,
 \qquad J\widehat\beta J=-\widehat\beta,                   \tag{10}
$$



and, since (J\partial_zJ=-\partial_z),



$$
\mathcal A=\partial_z-\widehat\beta,
 \qquad J\mathcal AJ=-\mathcal A.                          \tag{11}
$$



The scalar gauge cancels from the alternating correction:



$$
\begin{aligned}
 \Delta(C,D)
  &=C(D'-\widehat\beta_D)-D(C'-\widehat\beta_C)\\
  &=C\mathcal AD-D\mathcal AC.                              \tag{12}
\end{aligned}
$$



This establishes the symmetry without a finite computation.  The replay
also checks (9) and (11) exactly on 18 pairs
(1\le m\le3), (1\le n\le6), as a convention audit.

## 3. The exact bilinear parity formula

Now let (n=2d), set (x=z^2), and write



$$
C(z)=zU(x),\quad U\in\mathbb Q[x]_{\le d-1},
 \qquad
 D(z)=V(x),\quad V\in\mathbb Q[x]_{\le d}.                 \tag{13}
$$



Because (mathcal A) reverses parity, there are unique rational matrix
operators



$$
\mathcal A(zU)=\mathcal PU,
 \qquad
 \mathcal A(V)=z\mathcal QV,                               \tag{14}
$$



where (mathcal P) is ((d+1)\times d) and (mathcal Q) is
(d\times(d+1)).  Substitution in (12) proves (4):



$$
\Delta(z)=zU\cdot z\mathcal QV-V\mathcal PU
           =xU\mathcal QV-V\mathcal PU.                    \tag{15}
$$



Thus (Delta) is even and has (x)-degree at most (2d).  If



$$
U=\sum_{i=0}^{d-1}u_ix^i,
 \qquad V=\sum_{j=0}^{d}v_jx^j,                             \tag{16}
$$



then every coefficient of (15) is linear in the products (u_iv_j).
No assertion about a nonlinear continuous optimizer is being smuggled into
this statement: (15) is an exact identity over (mathbb Q).

## 4. Segre dimension, degree, and the distinction between algebraic and rational existence

The pair (([U],[V])) lies on the Segre embedding



$$
X_d=\mathbb P^{d-1}\times\mathbb P^d
       \hookrightarrow\mathbb P^{d(d+1)-1}.                 \tag{17}
$$



Let (h_1,h_2) be the two hyperplane classes.  The Segre hyperplane class
is (H=h_1+h_2).  Therefore



$$
\begin{aligned}
 \dim X_d&=(d-1)+d=2d-1,\\
 \deg X_d
  &=\int_{X_d}(h_1+h_2)^{2d-1}
    ={2d-1\choose d-1}.                                    \tag{18}
\end{aligned}
$$



The condition (deg_z\Delta\le2r) is exactly



$$
[x^k]\Delta=0,
 \qquad k=r+1,\ldots,2d,                                   \tag{19}
$$



so it imposes (2d-r=n-r) rational hyperplanes in the Segre ambient
space.  The projective dimension theorem gives



$$
\dim\{([U],[V]):\deg\Delta\le2r\}\ge r-1                \tag{20}
$$



over (overline{\mathbb Q}).  If equality holds and the intersection is
proper, its cycle class is (H^{2d-r}[X_d]).  In particular, when
(r=1), a proper zero-dimensional section has scheme length



$$
{2d-1\choose d-1}.                 \tag{21}
$$



This is a scheme-theoretic degree statement, not a rational-point theorem.
The fields of definition of the closed points can have the full degrees in
(21).

For context, a smooth complete curve cut out by the (2d-2) hyperplanes
for (r=2) has, by adjunction,



$$
2g-2=(d-2){2d-2\choose d-2}+(d-3){2d-2\choose d-1}.       \tag{22}
$$



This gives generic genera (3) for (d=3) and (26) for (d=4).
Our special sections can be reducible, so (22) is a warning about the
ambient geometry, not the genus calculation for every component below.

## 5. Exact maximal quadratic sections at (m=2)

### 5.1 Complete projective chart cover

For every nonzero (U,V), let (r_U,r_V) be their highest nonzero
coefficient indices.  Normalize those two coefficients independently to
one and set all higher coefficients to zero.  The charts



$$
0\le r_U\le d-1,
 \qquad 0\le r_V\le d                              \tag{23}
$$



are disjoint and cover (X_d).  In each chart the replay imposes
([x^k]\Delta=0) for (k=2,\ldots,2d) and computes an exact Gröbner
basis over (mathbb Q).

All empty charts have unit ideal.  In every nonempty chart the lexicographic
basis has the triangular form



$$
y_1-f_1(t),\ldots,y_s-f_s(t),p(t),                         \tag{24}
$$



with coefficient (1) on every (y_j).  The displayed modular reductions
of (p) are irreducible, so



$$
\mathbb Q[\text{chart coordinates}]/I\simeq\mathbb Q[t]/(p) \tag{25}
$$



is a field.  Hence the projective sections are both proper and reduced.
Over (overline{\mathbb Q}), separability gives one transverse geometric
point for every degree of (p).  This verifies the hypothesis needed to
interpret (21) as the exact point count in these three finite cases.

### 5.2 (n=4): one rational point and one quadratic point

Only charts ((r_U,r_V)=(1,1),(1,2)) are nonempty.  Their primitive
eliminants are



$$
\begin{aligned}
  5395t^2+441920t-4876032,&\qquad (r_U,r_V)=(1,1),\\
  7504t-73219,&\qquad (r_U,r_V)=(1,2).
 \end{aligned}                                              \tag{26}
$$



The first reduces to (6t^2+5t+10), irreducible modulo (17); the second
is linear.  The degrees (2+1=3) equal
({3\choose1}), as required by (21).

One compatible integral representative of the rational point is



$$
C=69z+7z^3,
 \qquad D=3024-73219z^2-7504z^4.                            \tag{27}
$$



With the orientation in (12), its exact corrected output is



$$
\Delta(C,D)=-3\bigl(387072+39205z^2\bigr).                 \tag{28}
$$



### 5.3 (n=6): exact degree (4+6), hence no rational point

Only ((r_U,r_V)=(2,2),(2,3)) are nonempty.  The primitive eliminants are



$$
\begin{aligned}
p_6(t)={}&159993342795770461884943800767188500t^6\\
&-67438546005662613716276365764413484140t^5\\
&+10054011874051528444666073804339834290713t^4\\
&-640794824953351032715671993934338680314368t^3\\
&+16686314917234974894193328180042596881148410t^2\\
&-177663046598412168228481049962369139095522860t\\
&+654888248721539759263972539204284664122085105,
                                                               \tag{29}\\[2mm]
p_4(t)={}&125394998957965242568746346568928t^4\\
&-36527237785295297633448744768079120t^3\\
&+2659510553107316805141647632178597775t^2\\
&+73022500232870716038019055227320616875t\\
&-9950911220742621352146028015376933221875.
                                                               \tag{30}
\end{aligned}
$$



Modulo (13), their descending coefficient lists are respectively



$$
(3,9,5,3,10,10,8),
 \qquad (9,2,9,2,10),                                      \tag{31}
$$



and both reductions are irreducible.  Thus both rational chart algebras
are fields of degrees (6) and (4).  Their sum is (10={5\choose2}),
and neither chart has a rational point.

### 5.4 (n=8): exact degree (15+20), again with no rational point

Of the (20) charts, only ((3,3)) and ((3,4)) are nonempty.  Their
primitive eliminants have degrees (20) and (15).  Because the integer
coefficients are very large, the canonical term-list SHA-256 digests are



$$
\begin{array}{c|c|c}
(r_U,r_V)&\deg p&\text{SHA-256}\\ \hline
(3,3)&20&
\texttt{189c82406a54b253dc23453b0ff0d0f00234247931c89bf3f49d72ad3bedbbb5},\\
(3,4)&15&
\texttt{d2a08748916f53a0f15cc766b17d44f281e400746c4343334453cc728c47bc37}.
\end{array}                                                  \tag{32}
$$



The degree-(20) polynomial is irreducible modulo (67), with descending
coefficient list



$$
(33,36,54,43,63,45,45,27,53,46,66,13,30,28,36,9,22,50,45,25,3),
                                                               \tag{33}
$$



and the degree-(15) polynomial is irreducible modulo (17), with list



$$
(4,8,6,4,7,4,15,8,10,10,15,10,11,0,7,5).                 \tag{34}
$$



The exact script constructs the characteristic-zero eliminants before
hashing and reducing them; the modular lists are not heuristic samples.
The total degree (20+15=35={7\choose3}) verifies the proper Segre
intersection, and neither closed point descends to (mathbb Q).

Equations (29)--(34) are the promised exact obstruction to extrapolating
the exceptional (n=4) rational quadratic point.

## 6. Degree four at (n=6): a rational-line component

Let (U=c_0+c_1x+c_2x^2), and let (H_U) be the (4\times4) matrix whose
(j)-th column consists of the coefficients of (x^3,x^4,x^5,x^6) in



$$
xU\mathcal Q(x^j)-x^j\mathcal PU,
 \qquad 0\le j\le3.                                       \tag{35}
$$



Then (H_Uv=0) is exactly the condition that the corresponding (V) give
(deg\Delta\le4).  Direct exact expansion gives



$$
\det H_U=\frac1{65610000}
 (590c_0-5823c_1+57465c_2)F_3(c_0,c_1,c_2),                \tag{36}
$$



where



$$
\begin{aligned}
F_3={}&7205321900c_0^3-3108229108110c_0^2c_1
 +2198940343306875c_0^2c_2\\
&+59247653649156c_0c_1^2-43968648471037830c_0c_1c_2
 +428131795997165400c_0c_2^2\\
&-288908249720832c_1^3+219756314527540290c_1^2c_2
 -4252894345690332750c_1c_2^2\\
&+20845875463468743825c_2^3.                               \tag{37}
\end{aligned}
$$



On the linear factor in (36), use the homogeneous parametrization



$$
(c_0,c_1,c_2)=(5823t-57465s,,590t,,590s).                \tag{38}
$$



The last row of (H_U) vanishes identically.  If (H_U^{[3]}) denotes
its first three rows, then the signed maximal-minor vector



$$
v_j=(-1)^j\det H_U^{[3]}{}_{\widehat j},
 \qquad 0\le j\le3,                                       \tag{39}
$$



satisfies (H_Uv=0) identically in (s,t).  At ([s:t]=[1:0]), the
full tail Jacobian on the two affine cones has rank (4); after quotienting
the two independent projective scaling directions, the local dimension is
one.  Hence (38)--(39) define an actual rational curve component, not only
a formal determinant factor.

At the arithmetically simplest displayed parameter ([s:t]=[0:1]), take



$$
\begin{aligned}
 C={}&5823z+590z^3,\\
 D={}&38680872000+14869741311z^2+1109528630z^4.
                                                               \tag{40}
\end{aligned}
$$



The exact output is



$$
\Delta(C,D)=-9P_6(z),                                     \tag{41}
$$



with primitive



$$
P_6(z)=683258923008000
       +138458274343783z^2
       +7014432262780z^4.                                  \tag{42}
$$



A bounded scan of all (1111) reduced affine parameters
(b=p/q), (|p|\le30), (1\le q\le30), found that both the smallest
(|P_b(i\pi)|) and the largest relative cancellation exponent occur at
(b=0), namely (42).  This is explicitly a finite diagnostic, not an
arithmetic theorem about the rational line.

## 7. Degree four at (n=8): a rational point on a genus-six component

Let



$$
U=c_0+c_1x+c_2x^2+c_3x^3,                                 \tag{43}
$$



and form the (6\times5) tail matrix (H_U) from the coefficients
(x^3,\ldots,x^8), analogously to (35).  Its last row is



$$
(0,0,0,0,-L),\qquad
 L=\frac{42271c_0-417198c_1+4117575c_2-40638465c_3}{315}.   \tag{44}
$$



On (L=0), eliminate (c_0):



$$
c_0=\frac{417198c_1-4117575c_2+40638465c_3}{42271}.        \tag{45}
$$



The determinant of the first five rows of the resulting (H_U) is a
homogeneous plane quintic (F(c_1,c_2,c_3)).  After primitive integer
normalization it has (21) terms and canonical term-list digest



$$
\texttt{c4ec249109d6978875808dcdfc162aa1252dc15921fa44157cc8bab6a6f51f9c}.
                                                               \tag{46}
$$



Writing (a=c_1,b=c_2,c=c_3), its reduction modulo (11) is



$$
\begin{aligned}
\overline F={}&a^5+a^4b+7a^4c+9a^3b^2+8a^3c^2
 +6a^2b^3+3a^2b^2c\\
&+8a^2bc^2+2a^2c^3+3ab^4+4ab^3c+ab^2c^2
 +5abc^3+6ac^4\\
&+4b^5+9b^4c+9b^2c^3+2bc^4+10c^5.                         \tag{47}
\end{aligned}
$$



The exact gradient ideals give



$$
\begin{array}{c|c}
 \text{projective patch}&\text{gradient ideal over }\mathbb F_{11}\\ \hline
 c=1&(1),\\
 c=0, b=1&(1),\\
 [a:b:c]=[1:0:0]&(\overline F_a,\overline F_b,\overline F_c)=(5,1,7).
 \end{array}                                                \tag{48}
$$



These patches cover (mathbb P^2), so the reduction is smooth.  Since a
reducible projective plane curve has intersecting components over the
algebraic closure, a smooth plane curve is geometrically irreducible.
Smooth reduction also certifies smoothness of the characteristic-zero
quintic.  Therefore its genus is



$$
g=\frac{(5-1)(5-2)}2=6.             \tag{49}
$$



The quintic has the rational point



$$
(c_1,c_2,c_3)=(1450665,14881,0),
 \qquad c_0=12867945.                                      \tag{50}
$$



At this point (H_U) has rank (4), so its kernel is one-dimensional.
Primitive compatible endpoint coefficients are



$$
\begin{aligned}
C={}&12867945z+1450665z^3+14881z^5,\\
D={}&504574901556626789015258880\\
&+598191925197439504473212224125z^2\\
&+68370439687845675316908865023z^4\\
&+797647048410487887961952688z^6\\
&+1091837679098938109485676z^8.                             \tag{51}
\end{aligned}
$$



The six tail equations have Jacobian rank (6) on the (9)-dimensional
product of affine cones at (51).  Removing the two scaling directions
leaves local dimension one.  Moreover, away from the rank-drop locus the
kernel of (H_U) gives (V) by rational maximal minors.  Consequently the
closure of this graph is an actual component of the parity section,
birational to the smooth quintic (F=0).  In particular, it is a
genus-(6) component with a rational point, not a rational curve.

The exact corrected output is



$$
\Delta(C,D)=-135P_8(z),                                   \tag{52}
$$



where the primitive quartic is



$$
\begin{aligned}
P_8(z)={}&380509576250859788241707901911040\\
&+77106572277272551446181984162605z^2\\
&+3906224612207931823717824632944z^4.                      \tag{53}
\end{aligned}
$$



This rational point is therefore an exact existence result, but the
high-genus component supplies no rational parametrization for increasing
(n).

## 8. Primitive value/height diagnostics and the remaining obstruction

For a primitive even polynomial



$$
P(z)=\sum_{j=0}^r p_jz^{2j},
 \qquad H(P)=\max_j|p_j|,                                  \tag{54}
$$



define the diagnostic relative exponent



$$
\Theta(P)=-\frac{\log(|P(i\pi)|/H(P))}{\log H(P)}.         \tag{55}
$$



High-precision evaluation gives



$$
\begin{array}{c|r|c|c}
n&H(P)&|P(i\pi)|&\Theta(P)\\ \hline
4&387072&134.1594552916953486&0.6192375487450671\\
6&683258923008000&14342.20179388860312&0.7198023577157181\\
8&380509576250859788241707901911040&
815443423434634371.5770853346&0.4502396302336202.
\end{array}                                                 \tag{56}
$$



Every absolute value in (56) exceeds one.  The ratios to height are small,
but the primitive forms themselves are not small, and all three exponents
are below one.  These decimals are diagnostics only; the exact algebraic
claims are (28), (41), and (52).

The results isolate the obstruction sharply:

* maximal quadratic collapse exists over (overline{\mathbb Q}), but
  rational descent already fails at (m=2,n=6);
* fixed quartic collapse has positive-dimensional algebraic geometry, but
  even a rational component at (n=6) does not yet yield small primitive
  values, and a rational point at (n=8) lies on a nonrational component;
* no theorem controls the exterior content or the primitive height along
  an infinite sequence;
* no recursive rational curve, rational section, or number-field descent
  has been constructed for general even (n).

Therefore the parity-Segre route remains a legitimate finite structural
phenomenon, not a proof strategy completed by dimension counting.  In
particular, algebraic nonemptiness, continuous optimization, and finite
parameter scans must not be treated as arithmetic evidence.

## 9. Deterministic replay

The package consists of

* `sources/root_unity_unconstrained_parity_segre_collapse_audit.md`;
* `scripts/root_unity_unconstrained_parity_segre_collapse_certificate.py`;
* `results/root_unity_unconstrained_parity_segre_collapse_certificate.json`;
* `results/root_unity_unconstrained_parity_segre_collapse_hashes.sha256`.

Replay from the archive root with

```bash
python3 scripts/root_unity_unconstrained_parity_segre_collapse_certificate.py
```

The replay:

1. constructs the Hermite-cardinal endpoint matrix exactly over
   (mathbb Q) and checks the reflection matrix identities on a finite
   convention grid;
2. constructs (mathcal P,mathcal Q) and verifies (15);
3. audits every projective degree chart for (m=2,n=4,6,8), checks the
   triangular quotient-field bases and the stated irreducible modular
   reductions;
4. verifies the (n=6) determinant factorization, cofactor family, regular
   component point, displayed primitive output, and bounded diagnostic
   scan;
5. constructs the (n=8) quintic, checks its digest and smooth reduction,
   verifies the rational point and full tail-Jacobian rank, and reproduces
   the primitive output (53).

The script contains no randomized step.  No finite computation in the
replay is presented as an all-(n) rationality theorem.
