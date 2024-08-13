---
layout: post
title: Quantum Supertasks 
date: 2024-05-10 22:53 -0300
categories: [physics]
tags: [quantum physics]
lang: en
math: true
---

These last few days I came across this interesting contest which is going on. Thanks to [this](https://www.youtube.com/watch?v=L9hU4xrhEDs)[^fn-nth-1] awesome video from _Quantum Sense_.

The contest pretty straightfoward, create a video of 1.5 min max explaining a quantum science topic of my choosing. So I choose to talk about _Quantum Supertasks_(or did I ?). And this post is more or less like and script of what I'd like to talk.

While writing, I had several video ideas, so I do my best to write here the scripts and choose the one of them. Or all of them, in superposition.

## Supertasks
So what are Supertasks? this definition cautch me on a old-ish [Vsauce video](https://www.youtube.com/watch?v=ffUnNaQTfZE&pp=ugMICgJwdBABGAHKBQpzdXBlcnRhc2tz)[^fn-nth-2]. But it's a task(algorithm) which the number of steps blows up to infinity when approximating a certain point in time, and in fact, these tasks seem to be not an easy deal.

But there are some known supertasks that have "solutions". Think of one of the [Zeno's Paradoxes](https://en.wikipedia.org/wiki/Achilles_and_the_Tortoise_(disambiguation)) _Achilles and the tortoise_, which ponterates on movements on kinematics should not exist at all as it takes an infinite number of steps in a finite time.

This is indeed an infinite geometric progression.


But even though things happen. Why ? This is where the quantum comes in. Things happens 'cause the universe is quantizided.(Or that's what we assume for quantum physics)

And it get even more interesting when we talk about the duality principle. As it states that, for very small particles we can assume that they are in a superposition state between a wave(continous) and a particle(discrete). This means that even in quantum physics things aren't exactly quantizided, in the real world they are, but in calculations they might be continoum probability distributions.This is both interesting and confusing.

### Solution to Zeno's paradox
But one can say that zeno's paradox is easily justifiable via the effective value of sum of an infinite geometric progression. 

Suppose that both Aquilles and the Tortoise have constant velocity denoted by $ V_a $ and $ V_t $ respectivelly, Aquilles is faster than the Tortoise, but he started later, in the beginning the distance between them is $ a $.

After $ t_1 = \frac{a}{V_a} $ seconds, Aquilles is on the same position as the tortoise in the beginning, but it has also run $ V_t*t_1 = V_t(\frac{a}{V_a}) = a\frac{V_t}{V_a} $. Which we can think of being the _new_ distance between them. By repeating this process what should be the total time for them to meet ? And the total distance ?

$$
t_{total} = t_1 + t_2 + ... =a \frac{1}{V_a} + a\frac{\frac{V_t}{V_a}}{V_a} + a\frac{(\frac{V_t}{V_a})^2}{V_a}+...
$$

Which can be written like this.

$$
V_a*t_{total} = \left( a + a\frac{V_t}{V_a} + a(\frac{V_t}{V_a})^2 + ... \right) = S_{total}
$$



let's plot these informations.
![Figure 1 - Achilles and Tortoise - Time vs Velocity](/assets/posts/20240423/Figure_1-darkmode.png ){:.dark .w-100}
![Figure 1 - Achilles and Tortoise - Time vs Velocity](/assets/posts/20240423/Figure_1-lightmode.png ){:.light .w-100}
_Graph of time vs position_

$$
Let\ q=\frac{V_t}{V_a}
$$

$$
S = a + aq +aq^2 + ... + aq^{n-1}
$$

$$
Sq = aq +aq^2 + aq^3 ... + aq^{n}
$$

$$
S(q-1) =a(q^{n}-1)
$$

$$
S = \frac{a(q^{n}-1)}{(q-1)}
$$

$$
as\ V_t< V_a\ and\ q = \frac{V_t}{V_a} \implies q < 1
$$

$$
\lim_{n \rightarrow +\infty}{S} =S_{total} =\lim_{n \rightarrow +\infty}{\frac{a(q^{n}-1)}{(q-1)}} = \frac{a}{1-q}
$$



This is when the overall result converges, yes, but would it be possible to do this on results that don't ? This is when superposition comes into play

The parity of the steps enter a superposition state because the steps converge into a singularity! 

This video might help to explain this situation.

:Youtube{url="KgEqZn7O7io"}

So in fact this paradox helps to illustrate the duality of nature, aquilles will surpass the tortoise in the continuum, however,even if we choose to discretize in a quantum level, the universe still has properties of the continuum. 

But now we can better understand with the consolidated field of probabilities in math. Therefore, still the great question remains, is the universe continuum or discrete ? It's, somehow, both. 

Thanks for reading until here! Plese feel free to comment bellow or in the video, I'll do my best to debate about any question that might arise.

And some special thanks to [3b1b](https://www.youtube.com/@3blue1brown) and [Manim Community](https://www.manim.community/) for mantaining such a nice python library!

## References
[^fn-nth-1]: [Quantum Sense](https://www.youtube.com/@quantumsensechannel)
[^fn-nth-2]: [Vsauce](https://www.youtube.com/@Vsauce) 

