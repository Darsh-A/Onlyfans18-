For particle confined in length $l$,


$$
\frac{\partial^2\psi(x)}{\partial x^2}+k^2\psi(x)=0
$$

where, 
$$
\blue k^2=\frac{2mE}{\bar{h}^2}
$$
where, 
- $m$ is the mass of the particle 
- $E$ is the energy 
>$PE$ need not be taken into account as particle experiences no external force and undergoes no other interaction. Therefore, $PE=\text{constant}=0$  
>**Note:** For any quantum mechanical state, energy is an observable

- $\bar{h}=\frac{h}{2\pi}$ 

#### Boundary Conditions 

$$
\frac{\partial^2\psi(x)}{\partial x^2}+k^2\psi(x)=0
$$

1. $\psi(x=0)=0$
2. $\psi(x=l)=0$ 


#### Solutions 

$$\blue \psi(x)=A\cos kx+B\sin kx$$

**According to boundary conditions,**

>$\psi(x=0)=0 \Rightarrow A=0$
>
>$\psi(x=l)=0 \Rightarrow B\sin kl=0$

>$$\blue B \sin (kl)=\begin{cases} \red B=0\:\text{and}\:A=0, \text{trivial solution} \\  {\color{#77DD77}
\sin (kl)=0 \Rightarrow kl=n\pi}\:;\:\:n=\begin{cases}\red

n=0, \text{trivial solution} \\  \color{#77DD77}
n\neq 0
\end{cases}
\end{cases}$$

Therefore, 

$\blue\psi(x)=B \sin kl$  where  $\blue{k=\frac{n\pi}{l}}$ and $\purp n=1,2,3,\dots$

Also, $k^2=\frac{2mE}{\bar{h}^2}$
$$
\begin{align}
\left( \frac{n\pi}{l} \right)^2=\frac{2mE}{\bar{h^2}} \\ \\
\blue E=\frac{n^2h^2}{8ml^2}
\end{align}
$$
#### Conclusion 

$$\frac{\partial^2\psi(x)}{\partial x^2}+k^2\psi(x) \text{  is satisfied by}\begin{cases}

\psi_{n}(x)= B\sin\left( \frac{n\pi}{l} \right)x  \\ \\
E_{n}=n^2 \cdot \frac{h^2}{8ml^2}\:;\:n=1,2,3,\dots
\end{cases}$$


| $\red\text{Energy}$          | $\red\text{State}$                               |
| ---------------------------- | ------------------------------------------------ |
| $E_{1}=\frac{h^2}{8ml^2}$    | $\psi_{1}(x)=B\sin\left( \frac{\pi}{l} \right)x$ |
| $E_{2}=\frac{4h^2}{8ml^2}$   | $\psi_{2}(x)=B\sin(\frac{2\pi}{l})x$             |
| $E_{3}=\frac{9h^2}{8ml^2}$   | $\psi_{3}(x)=B\sin(\frac{3\pi}{l})x$             |
| $\vdots$                     | $\vdots$                                          |
| $E_{n}=\frac{n^2h^2}{8ml^2}$ | $\psi_{n}(x)=B\sin(\frac{n\pi}{l})x$                                                 |


**Note:**
Each state is associated with an observable energy



As,  $\blue e^{i\theta}=\cos \theta +i\sin \theta$

$$\psi(x)=Ae^{ikx} + Be^{-ikx} $$

$\psi(x=0)=0\Rightarrow A+B=0\Rightarrow A=-B$ 

$$\psi(x=l)=A(e^{ikl}+e^{-ikl})=A(2i)\sin(kl)$$



###### What is $\psi(x)$? (Max Born Interpreation)

- $\psi(x)$ is the wave function, represents the probability amplitude 
- $\psi(x)\psi^{*}(x)=|\psi(x)|^{2}$  represents the probability density 


**Note:**

- Probability can be discrete or continous 

$$
\begin{align}
{\red\text{Discrete}:}\: P_{i} =\frac{n}{N} \:\:\:\:\:\:\:\:\:\:\:\:\:     \\
{\red\text{Continous}:} \: P(x,x+dx)=g(x)dx
\end{align}
$$


$$\begin{align}
\text{Energy} \rightarrow \text{Discrete}\:\:\:\:\:\:\: \\
\text{As}\: n\uparrow , \text{Discreteness} \rightarrow \text{Continous}
\end{align}
$$

- The state of a system is expressed as the linear combination of all possible states 



### Normalisation of Wave Function 

$\psi_{n}(x)=B\sin (\frac{n\pi}{l})x$

$\psi^{*}_{n}(x)=B\sin \left( \frac{n\pi}{l} \right)x$

For normalisation, 
$$
\ref{limits}\int   \psi(x)\psi^{*}(x)dx 
$$
