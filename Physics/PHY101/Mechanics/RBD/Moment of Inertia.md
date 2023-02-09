## Products of Inertia
$$
\require{physics}
\begin{align}
I_{xx} &= \Sigma m_{j}(y_{j}^{2}+z_{j}^{2}) \\ 
I_{yy} &= \Sigma m_{j}(x_{j}^{2}+z_{j}^{2}) \\
I_{zz} &= \Sigma m_{j}(x_{j}^{2}+y_{j}^{2}) \\ \\
I_{xy} &= - \Sigma m_{j}x_{j}y_{j}  \\
I_{yz} &= - \Sigma m_{j}y_{j}z_{j}  \\
I_{xz} &= - \Sigma m_{j}x_{j}z_{j}  \\ \\
I_{xy} &= I_{yx}  \\
I_{yz} &= I_{zy} \\
I_{xz} &= I_{zx}
\end{align}
$$

## Moment of Inertia Tensor

$$
\require{physics}
\begin{align}
\tensorTwo{I} &= \begin{pmatrix}
I_{xx} & I_{xy} & I_{xz} \\
I_{yx} & I_{yy} & I_{yz} \\
I_{zx} & I_{zy} & I_{zz} \\
\end{pmatrix}
\end{align}
$$

## Principal Axes Finding
The principal axes can be found by solving the equation:
$$
\require{physics}
\begin{bmatrix}
I_{xx}-\lambda & I_{xy} & I_{xz} \\
I_{yx} & I_{yy}-\lambda & I_{yz} \\
I_{zx} & I_{zy} & I_{zz}-\lambda \\
\end{bmatrix}
=0
$$
This forms a cubic equation of form:
$$
\require{physics}
a_{0}+a_{1}\lambda+a_{2}\lambda^{2}+a_{3}\lambda^{3}=0
$$
Solving the above equation gives at max 3 real roots.
The principal axes can then by found by substituting the value of $\lambda$ in the above matrix, and then multiplying it with standard axes:
$$
\require{physics}
\begin{pmatrix}
I_{xx}-\lambda & I_{xy} & I_{xz} \\
I_{yx} & I_{yy}-\lambda & I_{yz} \\
I_{zx} & I_{zy} & I_{zz}-\lambda \\
\end{pmatrix}
\begin{pmatrix}
x \\
y \\
z
\end{pmatrix}
=0
$$
This gives us a set of equations, the principal axes then become the normalized coefficient of each variab
## Parallel Axis Theorem

$$
\require{physics}
I = I_{c} + Mh^{2}
$$
where:
$I$: Moment of Inertia of the body
$I_{c}$: Moment of Inertia of the body about the center
$M$: Mass of the body
$h$: The distance between the two axes

## Perpendicular Axis Theorem
$$
\require{physics}
I_{a}=I_{b}+I_{c}
$$
where $a, b, c$ are three axes perpendicular to each other.