# .

## Finite Dimensional Spaces

Recall that a space is finite dimensional if it has a finite spanning set.

Suppose $V$ is a finite dimensional vector space and $S=\{v_{1}\dots v_{n}\}$
is a spanning set.
 
If $S$ is not linearly independent, there is some $v_{i}$ such that
	$v_{i} \in Span(S \setminus \{v_{i}\})$
So, $Span(S \setminus \{v_{i}\}) = Span(S) = V$
Thus,
	$S \setminus \{v_{i}\}$ is a smaller spanning set.

Again, if $S \setminus\{v_{i}\}$ is not linearly independent, we can remove another element to create an even smaller spanning set.
This can continue at most $n$ times.
So, at some point, we must end up with a spanning set which is linearly independent.


### Basis

A ***Basis*** of $V$ is a spanning set which is linearly independent.
 - And, any finite spanning set of a finite dimensional vector space has a subset which is a ***Basis***.
Also,
 - For any vector space 