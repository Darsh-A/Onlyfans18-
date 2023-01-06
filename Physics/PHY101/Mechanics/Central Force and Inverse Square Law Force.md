Consider an isolated system containing two particles interacting under a central force $f(r)\hat{\mathbf{r}}$. The masses of the particles are $m_{1} \text{ and } m_{2}$ and their position vectors are $\require{physics} \vectorarrow{r_{1}} \text{ and } \vectorarrow{r_{2}}$ respectively.

![](https://i.imgur.com/JAjXvql.png)

The equations of motion therefore are:
$$
\require{physics}
\begin{align}
& m_{1}\ddot{r_{1}}= f(r)\hat{\mathbf{r}} \\
& m_{2} \ddot{r_{2}} = -f(r)\hat{\mathbf{r}} \\ \\
\text{Therefore }\mu \ddot{r}= f(r)\hat{\mathbf{r}},
\end{align}
$$
where $\mu$ is the reduced mass of the system $\mu = \frac{m_{1}m_{2}}{m_{1}+m_{2}}$

```ad-note
## Consequences of conservation of angular momentum
```


```ad-note
title: The motion is confined to a plane
$L = r \cross \mu \dot{r}$, so it follows that $r$ is always perpendicular to $L$ by the properties of cross product. Because $L$ is fixed in direction, the plane of the motion is also fixed, and $r$ can only move in a plane perpendicular to $L$.

Introducing polar coordinates to the system $r, \theta$ in the plane of motion, the equation of motion becomes $\mu \ddot{r}=f(r)\hat{\mathbf{r}}$ becomes:

$$
\require{physics}
\begin{align}
& \mu(\ddot{r} - r \dot{\theta}^{2})=f(r) \\
& \mu(r \ddot{\theta} + 2 \dot{r} \dot{\theta})= 0
\end{align}
$$

The consequence of second equation ensures that any central force has no tangential component.
```

```ad-note
title: Equality of Areas
color: 0,255,255

Since the magnitude of $L$ is constant, and is equal to:

$$
\require{physics}
L = \mu r^{2} \dot{\theta}
$$

This immediately leads to the law of equal areas. Since the area element in polar coordinates is:

$$
\require{physics}
\begin{align}
&dA = r^{2} \frac{d\theta}{2} \\
&\frac{dA}{dt}=\frac{r^{2}\dot{\theta}}{2} \\
& \frac{dA}{dt}= \frac{L}{2\mu}
\end{align}
$$

Since $L$ and $\mu$ is constant the rate of change of area is same.
```

## Consequences of the Conservation of Energy

The kinetic energy of $\mu$ is,
 $$
\require{physics}
\begin{align}
K &= \frac{1}{2}\mu v^{2} \\
&= \frac{1}{2}\mu(\dot{r}\hat{\mathbf{r}}+r\dot{\theta}\hat{\mathbf{\theta}})^{2} \\
&= \frac{1}{2}\mu(\dot{r}^{2}+r^{2}\dot{\theta}^{2}) \\
&= \frac{1}{2} (\mu \dot{r}^{2}+ \frac{L^{2}}{\mu r^{2}})
\end{align}
$$
The total energy $E$ of the system becomes:
$$
\require{physics}
\begin{align}
E &= K.E \text{ } + \text{ } U(r) \\
\implies E&= \frac{\mu \dot{r}^{2}}{2}+ \frac{L^{2}}{2\mu r^{2}}+ U(r)\\
\end{align}
$$
The above equation starts to look more and more like the energy equation of a particle moving in one dimension with all references to $\theta$ gone.

### Effective Potential $U_{eff}(r)$

In order to press the parallel further, we can replace $\frac{L^{2}}{2\mu r^{2}}+U(r)$ with $U_{eff}(r)$. Here $U_{eff}(r)$ is simply referred to as the effective potential which differs from true potential by a value of $\frac{L^{2}}{2\mu r^{2}}$ which is called the *centripetal potential*.

```ad-note
title: Note
color: 255,0,0
Introduction of the effective potential term is a just a way of conveniently representing the energy equation to look similar to energy equation of a particle undergoing one dimensional motion. 
```

## Formal Solution of Central Force Motion

$$
\require{physics}
\begin{align}
&E = \frac{1}{2}\mu \dot{r}^{2} + U_{eff}(r) \\
\implies & \dot{r} = \sqrt{( \frac{2}{\mu}(E-U_{eff}) \right)  }
\end{align}
$$