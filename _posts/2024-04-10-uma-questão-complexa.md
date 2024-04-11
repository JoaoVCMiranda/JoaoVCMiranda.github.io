---
layout: post
title: Uma questão complexa
date: 2024-04-10 16:59 -0300
categories: [Math]
tags: [complex numbers, polynomials]
math: true
---

## Calcule $tan(1º)+tan(5º)+...+tan(177º)$

Para solucionar essa questão, utilizarei de um fato conhecido de complexos:

$$
\frac{1}{1-z}=\frac{1}{2}(1+icotg(\frac{Arg(z)}{2}))
$$

Prove você.

### Manipulações trigonométricas
Sabendo que $tan(\theta)=cotg(90-\theta)$, teremos que:

$$
\sum_{k=0}^{44}tan(4k+1)=\sum_{k=-22}^{22}cotg(4k+1)
$$

Usando algumas propriedades de complexos como o produto de complexos e a fórmula de De Moivre, podemos unir as duas equações da seguinte maneira:

$$
\sum_{k=-22}^{22}cotg(4k+1)=2Img(\sum_{k=-22}^{22}\frac{1}{1-\omega z^k})
$$

onde $$\omega = cis(2º)$$  e $$z = cis(8º)$$

### Modelagem polinomial

Com isso em mente, sabemos que o polinômio das n-raízes da unidade é da seguinte forma  $$ p(z)=z^n-1$$ , $$ \{1, z=cis(\frac{360º}{n}),z^2,...,z^{n-1} \} $$

E pelas relações de Girard a soma do inverso das raízes de um polinômio $p(x)$ qualquer é:

$$
\sum \frac{1}{x_k} = (-1)\frac{p_1}{p_0}
$$

Agora precisamos gerar um polinômio cujas as raízes sejam da forma $1-\omega z^k$

> você consegue perceber que  $$\sum_{k=-22}^{22}\frac{1}{1-\omega z^k}=\sum_{k=0}^{44}\frac{1}{1-\omega z^k}$$, por quê?

Para transformar o polinômio unitário que conhecemos $$ p(z)=z^{45}-1 $$ em um polinômio cuja as raizes são da forma $$ 1-\omega z^k $$. Precisaremos:

Escalar todas as raízes por um fator de $-\omega$.

Transladar todas as raízes por uma constante 1

** tem que ser nessa ordem ?(resposta: acho que sim)

Escalar raízes de um polinômio qualquer por um fator $$ a $$.

 

$$
p(x) = (x-x_1)...(x-x_n)\implies p(\frac{x}{a})=(\frac{x}{a}-x_1)...(\frac{x}{a}-x_n)\\ \implies p(\frac{x}{a})=\frac{1}{a^n}(x-ax_1)...(x-ax_n) 
$$

$$
\boxed{g(x)=a^np(\frac{x}{a})=(x-ax_1)...(x-ax_n)} 
$$

E para transladar é como imaginar que você está no referencial da reta numérica, se você quer que seja adicionado um valor $$ c $$ nas raízes, você deve ir “$$ c $$” para trás, e caso seja para subtrair “$$ c $$” para frente… Dessa forma

$$
p(x) \implies \boxed{g(x)=p(x-c)}
$$

Aplicando isso à função $p(z)$ teremos que:

$$
g(z) = (-\omega)^{45} p(-\frac{z}{\omega})
$$

Tem raízes da forma $$-\omega z^k$$

 

$$
h(z) = g(z-1)
$$

Tem raízes da forma $$ 1-\omega z^k $$

$$
h(z)=(z-1)^{45}+w^{45}
$$

### Binômio de Newton

Podemos agora calcular os coeficientes de $$ z^0 $$ e $$ z^1 $$

$$
[z^0]=\omega^{45}+(1)^{0}(-1)^{45}\binom{45}{0} = cis(90º)-1=\boxed{i-1} 
$$

$$
[z^1]=(1)^{1}(-1)^{44}\binom{45}{1}=\boxed{45}
$$

Assim, 

$$
\sum_{k=-22}^{22}\frac{1}{1-\omega z^k} = (-1)\frac{45}{i-1}=\frac{45}{2}(1+i) \implies \boxed{Img(\sum_{k=-22}^{22}\frac{1}{1-\omega z^k}) = \frac{45}{2}}
$$

Finalmente, podemos concluir que nosso resultado da nossa questão original é:

$$
\boxed{tan(1º)+tan(5º)+...+tan(177º) = 45}
$$
