![Polar Coordinates Image](https://d138zd1ktt9iqe.cloudfront.net/media/seo_landing_files/untitledjjhh-1605864512.png)

$x = r \cos \theta$
$y = r \sin \theta$

$r = \sqrt{ x^{2}+ y^{2}}, \theta=\tan ^{-1}\left( \frac{y}{x} \right)$

![](https://i.imgur.com/GSSxdOo.png)

$\require{physics} \hat{\mathbf{r}}= \cos \theta \hat{\mathbf{x}} + \sin \theta \hat{\mathbf{y}}$
$\require{physics}\hat{\mathbf{	\theta}}= -\sin \theta \hat{\mathbf{x}}+ \cos \theta \hat{\mathbf{y}}$

$\frac{d\hat{r}}{dt} = -\sin \theta \text{ } \hat{\mathbf{x}} \hat{\mathbf{\theta}} + \cos \theta \text{ } \hat{\mathbf{y}} \hat{\mathbf{\theta}} = \dot{\theta}\hat{\mathbf{\theta}}$
$\frac{d\hat{\mathbf{\theta}}}{dt}= -\cos \theta \hat{\mathbf{x}} \dot{\theta} - \sin \theta \hat{\mathbf{y}} \dot{\theta}= -\dot{\theta}\hat{r}$

## Position Vector
$$
\require{physics}

\begin{align}
\vectorarrow{r} &= x \hat{\mathbf{x}} + y \hat{\mathbf{y}} \\
&= r\cos \theta \hat{\mathbf{x}} + r \sin \theta \hat{\mathbf{y}} \\
&= r(\cos \theta \hat{\mathbf{x}} + \sin \theta \hat{\mathbf{y}}) \\
&= r \hat{\mathbf{r}}
\end{align}

$$
## Velocity Vector
$$
\require{physics}
\begin{align}
\vectorarrow{v}=\frac{d \vectorarrow{r}}{dt} &=\frac{dr}{dt}\hat{\mathbf{r}} + r\frac{d\hat{\mathbf{r}}}{dt} \\
&= \dot{r}\hat{r} + r \dot{\theta} \hat{\mathbf{\theta}}
\end{align}
$$
## Acceleration Vector
$$
\require{physics}
\begin{align}
\vectorarrow{a}= \frac{d\vectorarrow{v}}{dt} &= \ddot{r}\hat{\mathbf{r}} + \dot{r}\frac{d\hat{\mathbf{r}}}{dt} + \dot{r}\dot{\theta}\hat{\mathbf{\theta}} + r \ddot{\theta} \hat{\mathbf{\theta}} + r \dot{\theta} \frac{d\hat{\mathbf{\theta}}}{dt} \\
&= \ddot{r}\hat{\mathbf{r}} + \dot{r}\dot{\theta}\hat{\mathbf{\theta}} + \dot{r}\dot{\theta}\hat{\mathbf{\theta}}+r\ddot{\theta}\hat{\mathbf{\theta}} - r\dot{\theta}^{2}\hat{\mathbf{r}} \\
&= (\ddot{r}-r\dot{\theta}^{2})\hat{\mathbf{r}}+(r\ddot{\theta}+2\dot{r}\dot{\theta})\hat{\mathbf{\theta}}
\end{align}
$$
where,
$\ddot{r}=$ Magnitude of Linear Radial Acceleration.
$r\dot{\theta}^{2}$ = Magnitude of Centripetal Acceleration
$r \ddot{\theta}=$ Magnitude of Linear Tangential Acceleration.
$2\dot{r}\dot{\theta}=$ Magnitude of Coriolis Acceleration

and,
$(\ddot{r} - r\dot{\theta}^{2})\hat{\mathbf{r}}=$ Net Radial Acceleration
$(r \ddot{\theta} + 2\dot{r} \dot{\theta})\hat{\mathbf{\theta}}=$ Net Tangential Acceleration