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
\implies & \dot{r} = \sqrt{ \frac{2}{\mu}(E-U_{eff}) } \\
\implies & \frac{dr}{dt} = \sqrt{ \frac{2}{\mu}(E-U_{eff}) }  \\
\implies & \int_{t_{0}}^{t} dt = \int _{r_{0}}^{r} \frac{dr}{\sqrt{ \frac{2}{\mu}(E-U_{eff})}} \\
\implies & t-t_{0} = \int _{r_{0}}^{r} \frac{dr}{\sqrt{ \frac{2}{\mu}(E-U_{eff})}}
\end{align}
$$

The above equation gives us $r$ as a function of $t$. But often times we need to find the path of the particle which means knowing $r$ as a function of $\theta$ rather than $t$, so in order to find θ as a function of $t$, therefore we make use of

$$
\require{physics}
 \frac{d\theta}{dt}= \frac{L}{\mu r^{2}} 
$$

In the above equation since $r$ is known to be a function of $t$. We can use chain rule to write

$$
\require{physics}
\frac{d\theta}{dr}= \frac{d\theta}{dt} \frac{dt}{dr}
$$

which is

$$
\require{physics}
\begin{align}
& \frac{d\theta}{dr}=\frac{L}{\mu r^{2}}\sqrt{ \frac{\mu}{2(E-U_{eff})} } \\
\implies & \theta - \theta_{0} = L \int _{r_{0}}^{r} \frac{dr}{r^{2} \sqrt{ 2\mu(E-U_{eff}) } } 
\end{align}
$$

### Central Force Description of Free Particle Motion

![](https://i.imgur.com/76rQhGp.png)

Two non-interacting particles $m_{1}$ and $m_{2}$ move toward each other with velocities $v_{1}$ and $v_{2}$, respectively. Therefore,

$$
\require{physics}
\mu = \frac{m_{1}m_{2}}{m_{1}+m_{2}}
$$

Their paths are offset by distance $b$ as shown in the diagram. The relative velocity is:

$$
\require{physics}
\begin{align}
v_{0} &= \dot{r} \\
&= \dot{r}_{1} - \dot{r}_{2} \\
&= v_{1}-v_{2}
\end{align}
$$

Here $v_{0}$ is constant because $v_{1}$ and $v_{2}$ are constant. The energy the system relative to the center of mass is

$$
\require{physics}
E = \frac{1}{2}\mu_{0}v_{0}^{2} + U(r) = \frac{1}{2}\mu_{0}v_{0}^{2}
$$

as $U(r)=0$ for non interacting particles.

$$
\require{physics}
U_{eff}(r)= \frac{L^{}{2}}{2\mu r^{2}}+ U(r) = \frac{L^{2}}{2 \mu r^{2}}
$$

We can evaluate $L$ easily by

$$
\require{physics}
E = \frac{1}{2}
\mu \dot{r}^{2}+ \frac{L^{2}}{2 \mu r^{2}}= \frac{1}{2}\mu v_{0}^{2}
$$

When $m_{1}$ and $m_{2}$ pass each other the value of $\dot{r}=0$ and $r=b$

$$
\require{physics}
\begin{align}
\frac{L^{2}}{2 \mu b^{2}}=\frac{1}{2}\mu v_{0} ^{2} \\
L =\mu b v_{0}
\end{align}
$$

and this relation always holds true because $L$ is constant. Therefore,

$$
\require{physics}
U_{eff}=\frac{1}{2}\mu v_{0}^{2} \frac{b^{2}}{r^{2}}
$$

The following is the energy diagram:

![](https://i.imgur.com/BV7Bfzh.png)

The kinetic energy associated with radial motion is $K = \frac{1}{2} \mu \dot{r}^{2} = E-U_{eff}$

As $K$ can never be negative, the motion is restricted to regions where $E - U_{eff} \geq 0$. Initially as $r$ is very large and $U_{eff} \approx 0$. As the particles approach, the kinetic energy decreases vanishing at the turning point $r_{t}$, where the radial velocity is $0$ and the motion is purely tangential. At the turning point $E = U_{eff}(r_{t})$, which gives

$$
\require{physics}
\frac{1}{2}\mu v_{0}^{2}= \frac{1}{2}\mu v_{0}^{2} \frac{b^{2}}{r_{t}^{2}}
$$

$$
\require{physics}
r_{t}=b
$$

Which is as we expected, since $r_{t}$ is the distance of closest approach of the particles; it is the minimum value of $r$. Once the turning point is passed, $r$ increases and the particles separate.