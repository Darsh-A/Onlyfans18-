```ad-note
title: Important
icon: exclamation 
color: 255,0,0

A few topics from [[Moment of Inertia]] have been used in here.
```

To proceed with solving any problem using Euler's Equation, make sure the axes you are working with are the [principal axes](<Moment of Inertia#Principal Axes Finding>).

$$
\require{physics}
\begin{align}
\tau_{1} &= I_{1}\frac{d\omega_{1}}{dt} + (I_{3}-I_{2})\omega_{3}\omega_{2} \\
\tau_{2} &= I_{2}\frac{d\omega_{2}}{dt} + (I_{1}-I_{3})\omega_{1}\omega_{3} \\
\tau_{3} &= I_{3}\frac{d\omega_{3}}{dt} + (I_{2}-I_{1})\omega_{2}\omega_{1} \\
\end{align}
$$