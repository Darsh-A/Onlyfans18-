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
\begin{equation}
\int _{0}^{l} \psi(x)\psi^{*}(x)\, dx=1
\end{equation}
$$

$$
\begin{align}
B^2 \int_{0}^{l}\sin^2\left( \frac{n\pi}{l} \right)x \, dx \\
	B^2 \int _{0}^{l} \frac{{1-\cos\left( \frac{2n\pi}{l} \right)x}}{2} \, dx   \\
B=\pm \sqrt{ \frac{2}{l} }\:\:\:\:\:\:\:\: 
\end{align}
$$

$\sqrt{ \frac{2}{l} }$ is the normalisation constant 

*Normalised State(convention)*: $\psi_{n}(x)=\sqrt{ \frac{2}{l} }\sin(\frac{n\pi}{l})x$ 


### Operators 

- All observables are associated with *operators*
| Observables | Operators                             |
| ----------- | ------------------------------------- |
| K.E.        | $\hat{K.E.}$                          |
| Momentum    | $\hat{P_{x}},\hat{P_{y}},\hat{P_{z}}$ |
| Position      | $\hat{x},\hat{y},\hat{z}$             |


- All observables are nothing but eigen values 

$$
\frac{d^2\psi(x)}{dx^2}+kx=0
$$
$$
[-\frac{\bar{h^2}}{2m} \frac{d^2}{dx^2}] \psi(x)=E_{n}\psi_{n}(x)$$

$[-\frac{\bar{h}^2}{2m} \frac{d^2}{dx^2}]=\hat{K.E.}$

$$
\Phi(x)=c_{1}\phi_{1}(x) + c_{2}\phi_{2}(x) +\dots+c_{n}\phi_{n}(x)
$$
where, $c_{1},c_{2},\dots$ are eigen values which represent energies 

$K.E.=\frac{P_{x}^2}{2m}$

$$
\hat{P_{x}^2}=-\bar{h}^2 \frac{d^2}{dx^{2}} \Rightarrow \hat{P_{x}}=\begin{cases}
\:\:\:ih \frac{d}{dx} \\
-ih \frac{d}{dx}
\end{cases}
$$


### Expectation Value of an observable 

Expextation value is the wighted average of all possible eigen values 

$$
<\hat{A}>|<A>\:= \frac{{\int\hat{\psi}\:A\:\psi^{*} d\tau}}{\int \psi^{*}\:\psi \, dx }
$$

$\Psi=c_{1}\psi_{1}+c_{2}\psi_{2}$

$\hat{A}\psi_{1}=a_{1}\psi_{1}$
$\hat{A}\psi_{2}=a_{2}\psi_{2}$


$$
\int \phi_{m}\phi _{n}^{*} \, dx =\begin{cases}
1,\:m=n \\
0,\: m\neq n
\end{cases}
$$
$*\:\:\purp{\text{Basis functions are othogonal}}$


###### Example:
$\Phi=c_{1}\phi_{1}+c_{2}\phi_{2}$
$\Phi^*=c_{1}^*\phi^* + c_{2}^*\phi_{2}^*$ 

$$
\int \Phi \Phi^* \, dx =
\int  (c_{1}\phi_{1}+c_{2}\phi_{2})(c_{1}^*\phi^* + c_{2}^*\phi_{2}^*)\, dx   
= c_{1}c_{1}^*+c_{2}c_{2}^*
$$

$\hat{A}\phi_{n}=a\phi_{n}$

$$
\begin{align}
 \int \Phi\: \hat{A}\: \Phi^*\, dx
=c_{1}c_{1}^*a_{1} +c_{2}c_{2}^*a_{2} 
\end{align}
$$

Therefore, 

$$
\begin{align}
<\hat{A}> = \frac{{c_{1}c_{1}^*a_{1} + c_{2}c_{2}^*a_{2}}}{c_{1}c_{1}^*+c_{2}c_{2}^*} \\  \\

<\hat{A}> = \frac{c_{1}c_{1}^*}{c_{1}c_{1}^*+c_{2}c_{2}^*}a_{1} + \frac{c_{2}c_{2}^*}{c_{1}c_{1}^*+c_{2}c_{2}^*}a_{2} \\ \\
 <\hat{A}> = P_{1}a_{1}+P_{2}a_{2} \\ \\
P_{1}+P_{2}=1

\end{align}
$$

Generally, for
$$
\Phi=c_{1}\phi_{1}+c_{2}\phi_{2}+\dots+c_{n}\phi_{n}
$$

$$
P(P_{i})=\frac{c_{i}c_{i}^*}{{\sum_{i=0}^{n}}c_{i}c_{i}^*}
$$
$$
<\hat{A}> = \sum_{i=o}^{n}P_{i}c_{i}
$$


### Properties of $\Psi$

1. Single Valued
2. Continous 
3. Differentiable 
4. Square Integrable 


### Commutators 

- Associated with operators 

$$\begin{align}

[\hat{A},\hat{B}]f(x)=0 \\
[\hat{A}\hat{B}-\hat{B}\hat{A}]f(x)=0 \\
\end{align}$$
$\Rightarrow$ The two operators commute

- If the operators don't commute then the observable associated with them cannot be measured simultaneously
- When operators commute, more info about the system can be found simultaneously 

