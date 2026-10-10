# The integer-error criterion

Let $\alpha$ be real. If integers $p_j,q_j$, with $q_j>0$, satisfy



$$
0<|q_j\alpha-p_j|\longrightarrow0
$$



on an infinite selected sequence, then $\alpha$ is irrational.

Indeed, if $\alpha=a/b$ with integers $a,b$ and $b>0$, then



$$
b(q_j\alpha-p_j)=aq_j-bp_j\in\mathbb Z.
$$



Whenever the error is nonzero, this integer has absolute value at least 1, so



$$
|q_j\alpha-p_j|\ge1/b.
$$



That contradicts the stated limit. It is enough to have infinitely many nonzero errors tending to zero; zeros at other indices do not help or invalidate such a subsequence. A limit of zero without any nonvanishing guarantee can occur for a rational number by exact equality.

The criterion uses integer coefficients. Lowest terms are not required by the elementary implication, but they are crucial when assessing the strength of a particular constructed approximation: dividing the numerator and denominator by their full gcd gives its smallest integer error. Clearing coefficients with an arbitrary integer can create a much larger error.

The statement $p_j/q_j\to\alpha$ by itself is insufficient. Every real number admits rational approximations. For a rational $\alpha=a/b$, any unequal rational $p/q$ has $|q\alpha-p|\ge1/b$, even when $|\alpha-p/q|\to0$.

One exact equality $e+\pi=a/b$ would prove rationality, if proved symbolically and rigorously. Numerical agreement to many digits, an integer-relation search, or a zero in floating-point arithmetic cannot establish that equality.

The current project has positive approximation errors in specific constructions. Its unresolved task is their decay after **complete actual integer normalization on the same infinite indices**.
