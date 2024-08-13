---
layout: post
title: Quantum Computers
date: 2024-05-13 23:06 -0300
categories: [physics]
tags: [quantum physics]
lang: en
math: true
---

Hello there again!

In this post I'd like to share some interesting things about the way that quantum computers work!

## What I thought it was 

At first I had no idea how supercomputers might work. Actually the first ideias came when I started studying how normal computers work, at the lowest level, with binary logic is just about having two states and a way to analyze them: (1,0), (True, false), (HIGH, LOW). 

> Formally one could say something like any set isomorphic to a [ _Galois Field_ ](https://en.wikipedia.org/wiki/Finite_field) with two elements $ \mathbb{Z}_2$

In fact, if you want you can make computers completelly out of the box with anything! Even [origami](https://www.quantamagazine.org/how-to-build-an-origami-computer-20240130/)! 

Okay, where are we going with this... What if we define our bit as a quantum state of an electron(up,down) ?

This is when things get interesting!

I've always heard that supercomputers or quantum computers can solve hard problems for regular computers in a fraction of the time that these would do it. But a great question to be made is _How_ ?

My first hipothesys what to entangle the _in_ bit with the _out_ bit and assemble them in a way that when a "pulse" is sent, it would propagate through the logic operations and it would find the best way out just like [water in a maze](https://www.youtube.com/watch?v=81ebWToAnvA)[^fn-nth-1] but the answer to any complex combinatorial circuit would be answered in constant time. And this feels very likely to be wrong or scary.

## How I think it is now

After sharing my hypothesys with a professor I became aware that quantum computers process signalsin a very _parallelized_ way in fact with exponential proportion with the number of  _quantum_ bits or Qubits.

So the "frequency"(number of calculations per unit of time) increases exponentially with the number of QuBits. For example, a 10 Qubit supercomputer can do 2 times more calculations than a 9 Qubit one within the same time interval. And this is fascinating 'cause, suppose a 10 Qubit computer could do about the same numbers of operations ( $2^{10}$ ) as  a raspberry pi 3 does 1Ghz, but a 12 Qubit would be more or less like an intel i7. 

And the "available" supercomputers today as the [IBM Osprey](https://spectrum.ieee.org/ibm-quantum-computer-osprey) have 433 Qubit. That's a lot.

There are at least two types of ports parallel ports and serial ports, the one that is most likely to you know is the serial port, as it in several eletronic devices, and it's more versative to use and therefore cheaper.

But there's also another type of port which is the parallel port which you might know from the VGA cable, which used to be included the computers and monitors.

The difference of parallel ports is that it's an interface that can send one bit sequence per "wire" so the processing of these signals can be made in parallel, while serial ports must have some sort of memory to process stuff. The issue with parallel ports is that they're expensive an limited.(You can only parallelize while there are wires to send the signal through)

Okay and how about the quantum stuff ? This is when things get even more interesting!

With quantum computers you can send Qubits in serie in a [superpositon state](https://joaovcmiranda.github.io/posts/quantum-supertasks/)!! So you can also have the best of both worlds in superposition.
One signal pipe, but for each bit it's as if you were sending two, and this grows exponentially to every possible sequence of bits ( $ 2^L $ ) of lenght $ L $

Therefore, the equivalent processing on a supercomputer with $ N $ Qubits is a classical computer with $ 2^N $ bits

So we would have like a vector of random variables not yet collapsed, and the real work with the analogous to the [combinatorial circuit](https://en.wikipedia.org/wiki/Combinational_logic) (and, or, not) would be work on maximizing the probabilities for when this supervector collapses, it will collapse on the right answer as if it "passed" through every possible state in parallel.

:Youtube{url="BZQ-U7Ek8rQ"}


## References
[^fn-nth-1]: [Steve Mould](https://www.youtube.com/@stevemould)
