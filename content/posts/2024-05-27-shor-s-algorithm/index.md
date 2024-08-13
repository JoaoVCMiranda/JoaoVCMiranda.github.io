---
layout: post
title: Inverse Quantum Fourier Transform
date: 2024-05-27 12:52 -0300
categories: [physics]
tags: [quantum physics]
lang: en
math: true
---

## Introduction

Hi there!

So Shor's algorithm[^fn-nth-1]... I might have some notion of what is about and what is does, but _how it works_ is a completely different history.

In this blog post I'm going to make some notes on what I've learned about the Shor's algorithm machinery.

The overall "way of working" of Shor's Factoring Algorithm involves several steps. And among them the most critical ones are the _Quantum Phase Estimation_(QPE) and the _Inverse Quantum Fourrier Transform_[^fn-nth-2](iQFT)

When I started this blog post thought about explaining how these critical steps work and what are they for in relation to the Shor's algorithm in particular... But I've decided split these into some posts. And then futher reference it in a more concise summary.

So this post will be just about the iQFT

## Inverse Quantum Fourier Transform (iQFT)[^fn-nth-4]
This algorithm is the basis for various quantum algorithms. At first, we might ask what is a Fourier Transform, how to apply it to quantum physics and why is it inverse!

A Fourier transform[^fn-nth-3] is an operation which is done to a function in order to change it's domain to another one with some interesting properties.

Eg. You can take the Fourier transform from the time domain of the audio of this video, and "convert" it to the frequency domain, and instead of having the waves that make my voice spread in time, you would have the frequencies(vibrations) that were used in the video, and the greater the amplitute, for longer you were exposed to this frequency in this video! 

But it doesn't strictly need to be a transformation between time and frequency, it could be, for example _position and momentum_!

### How is it done ?

There are some considerations we might need to do. Remember the [interesting way of writing the superstates](https://www.youtube.com/watch?v=KgEqZn7O7io) which quantum particles could assume ?

This is how we can write for **one single particle** in superpostition state:

$$
| \Psi ⟩ = c_0 | 0 ⟩ + c_1 | 1 ⟩ 
$$

Which is equivalent to this using the [bra-ket notation](https://en.wikipedia.org/wiki/Bra%E2%80%93ket_notation)

$$
| \Psi ⟩ = c_0 | 0 ⟩ + c_1 | 1 ⟩ =  \begin{pmatrix} c_0 \\ 0 \end{pmatrix} + \begin{pmatrix} 0 \\ c_1 \end{pmatrix} = \begin{pmatrix} c_0 \\ c_1 \end{pmatrix}
$$

But how can we represent superstates with many quantum particles ?

It's expectected for it to grow exponetially, but how to represent this ?

Don't run yet. There's (at least) one mathematical property that satisfies it... It's the Tensor Product!!

The tensor product does exactlly what we're looking for. Suppose we have 2 Qubits, and we want to find a space in which we can represent their superposition. For a single particle we would have a Galois field of order 2. So our possibilities are:

$$
\Omega = \{0, 1\}
$$

One could say that the dimension of $ \Omega  $ is 2.

But if we had 2 particles, how our amostral space would look like ?

$$
\Omega = \{00, 01, 10, 11\}
$$

To "append" the new states to our superpositioned bits we use the tensor product of their probability distributions!!

$$
| \Psi_0 \Psi_1 ⟩ = | \Psi_0 ⟩ \otimes | \Psi_1 ⟩
$$

### But why do it ?

For finite values of Qubits, the iQFT allows us to represent a amplitude vector in a _position basis_ in which the wave function determines the probability of finding the particle in a given position.
or a _momentum basis_ in which the wave function determines the probability of this particle have a certain _momentum_(proportional to it's speed) and the contributions of each Qubit to the output vector!

#### What are the basis ?

The basis are orthonormal vectors which generate a space.
So for a vector of $ N $ Qubits, we have $ 2^N $ possible output states.

$$

|0⟩,|1⟩,|2⟩,\dots,|2^N-1⟩  = \begin{pmatrix} 1 \\ 0 \\ 0 \\ \vdots \\ 0 \end{pmatrix},
\begin{pmatrix} 0 \\ 1 \\ 0 \\ \vdots \\ 0 \end{pmatrix},
\begin{pmatrix} 0 \\ 0 \\ 1 \\ \vdots \\ 0 \end{pmatrix},
\dots,
\begin{pmatrix} 0 \\ 0 \\ 0 \\ \vdots \\ 1 \end{pmatrix}

$$

Every wave function can be expressed as a complex number(two events which only one can happen when it collapses)

### Contributions?

Well, yes, we can calculate in the discrete case "how much" of a certain wave function is in a given *direction* and a start position.

Suppose we have a Qubit vector 

$$ 
|X(x,t)⟩ = |x_0x_1x_2...x_{N-1}⟩ = \bigotimes_{i=0}^{N-1}|x_i⟩
$$

> Cool X-men symbol 

We can represent it's wave function in the position basis or in the momentum basis(where $ k = \frac{2\pi}{\lambda} $).


$$
\Psi (x) \leftrightarrow \hat \Psi (k)
$$

And notice that:

$$
\Psi, \hat \Psi : \mathbb{R} \rightarrow \mathbb{R}^{2^N}
$$

Let's say that, $ \Psi $ is a vector of this form

$$
\Psi(x) = \sum_{i=0}^{N-1}c_i| i ⟩ 
$$

And $ \hat \Psi $ is:

$$
\hat \Psi(k) = \sum_{i=0}^{N-1}b_i| i ⟩ 
$$

The quantum fourier transform will make a sort of weighted average of all of the components of $ \Psi $ over some direction.

But what direction should we use ? 
_All of them_.

For doing so, we'll take an evenly spread vectors in all of the directions according to the size of the Qubit vector.

For this, we use the $ Nth $ root of the unity $ \omega =  e^{i\frac{2\pi }{N}}$

> It's the first complex root of this polinomial $p(x) = x^N-1$

Therefore, these two equivalent representations of the state can be 


### So What is the iQFT ??

It's a operation applied to the vector of wave functions("amplitudes") of every Qubit in a quantum state.



And the inverse fourier transform is given by

$$

b_k = \frac{1}{\sqrt{N}} \sum_{i=0}^{N-1}c_i\omega^{ik}_{N}

$$

Where $ \omega_N $ is the $ N $th root of the unity.

So each "coordinate" on the basis generated by a QFT is a linear combination of all other in the "original" one with the intent to magnify the wave function's amplitude in a given direction. 

Notice that 

$$

e^{i\theta} = cos(\theta) + i sin(\theta) \therefore \lVert e^{i\theta} \rVert ^2 = cos^2\theta + sin^2\theta = 1

$$

So multiplying by $ \omega $ does not influence the modulus, and in order to renormalize after the sum, we divide by $ \sqrt{N} $


A Fourier Transform, even in it's quantum version is a linear (invertible) transformation.

A matrix which transforms the original vector to a new one. Which can also be called a _Quantum Gate_ 

Which I think is a fairly good way of visualizing it.

The bra-ket notation is certainly more concise, but the explicit matrix notation is easier to visualize:

$$
\begin{pmatrix} c_0 \\ c_1 \\ c_2 \\ \vdots \\ c_{N-1} \end{pmatrix}=

\frac{1}{\sqrt{N}}
\begin{pmatrix} 1 & 1 & 1 & \dots & 1 \\ 
                1 & \omega & \omega^2 & \dots & \omega^{N-1} \\
                1 & \omega^2 & \omega^4 & \dots & \omega^{2(N-1)} \\
                \vdots & \vdots & \vdots & \ddots & \vdots \\ 
                1 & \omega^{N-1} & \omega^{2(N-1)} & \dots & \omega^{(N-1)(N-1)}
\end{pmatrix}

\begin{pmatrix} b_0 \\ b_1 \\ b_2 \\ \vdots \\ b_{N-1} \end{pmatrix}
$$

This is equivalent to say:

$$
|\Psi⟩ = \mathscr{F} |\hat\Psi⟩
$$
> Very fancy F

Where:

$$
\mathscr{F} =

\frac{1}{\sqrt{N}}

\begin{pmatrix} 1 & 1 & 1 & \dots & 1 \\ 
                1 & \omega & \omega^2 & \dots & \omega^{N-1} \\
                1 & \omega^2 & \omega^4 & \dots & \omega^{2(N-1)} \\
                \vdots & \vdots & \vdots & \ddots & \vdots \\ 
                1 & \omega^{N-1} & \omega^{2(N-1)} & \dots & \omega^{(N-1)(N-1)}
\end{pmatrix}
$$

Cool, as you get to the end you might know how to do a QFT, but how to do an iQFT ?

Just undo what you've done!

$$
\mathscr{F}^{-1} =

\frac{1}{\sqrt{N}}

\begin{pmatrix} 1 & 1 & 1 & \dots & 1 \\ 
                1 & \omega^{-1} & \omega^{-2} & \dots & \omega^{-(N-1)} \\
                1 & \omega^{-2} & \omega^{-4} & \dots & \omega^{-2(N-1)} \\
                \vdots & \vdots & \vdots & \ddots & \vdots \\ 
                1 & \omega^{-(N-1)} & \omega^{-2(N-1)} & \dots & \omega^{-(N-1)(N-1)}
\end{pmatrix}
$$

$$
|\hat\Psi⟩ = \mathscr{F}^{-1} |\Psi⟩
$$


## Next steps
In the next posts, I'll write about the Quantum Phase Estimation algorithm and then summarize these posts to explain Shor's algorithm for asymmetric cryptography like RSA. 
For symmetric cryptography AES, first I'd need to write about amplitude amplification and the Grover's algorithm

:Youtube{url='nMNvtoZdcAw'}

## References
[^fn-nth-1]: [Shor's Algorithms](https://www.classiq.io/insights/shors-algorithm-explained)
[^fn-nth-2]: [Quantum Fourier Transform](https://en.wikipedia.org/wiki/Quantum_Fourier_transform)
[^fn-nth-3]: [Discrete FT to QFT](https://arcb.csc.ncsu.edu/~mueller/qc/qc19/readings/Quantum%20Fourier%20Transforms%20191119.pdf)
[^fn-nth-4]: [Course on QFT](https://arcb.csc.ncsu.edu/~mueller/qc/qc19/readings/Quantum%20Fourier%20Transforms%20191119.pdf)
