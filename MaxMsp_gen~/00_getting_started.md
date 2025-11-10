---
id: what_is_gen~?
aliases:
  - Getting Started with Max/MSP gen~
tags: []
book: true
classoption: onecolumn
cover: https://i.imgur.com/OK7HD1v.png
edited_seconds: 79
export: PDF
pandoc-latex-environment:
  error-box:
    - error
  info-box:
    - info
  tcolorbox:
    - box
  warning-box:
    - warning
priority: ★
progress: starting
status: in progress
subtitle: GETTING STARTED GUIDE
title: Getting Started with gen~
titlepage: false
titlepage-background: /Users/juaneduardoflores/Downloads/clouds_export.png
titlepage-rule-height: 0
titlepage-text-color: FF5f87
titlepage-text-size: 34pt
type: Guide
updated: 2025-11-08T23:56:47.650-06:00
---
# Getting Started with Max/MSP gen~
## Introduction

**gen~** is an environment that lives inside the visual programming language called **Max**. Instead of writing code line-by-line, in Max and gen~, we are patching virtual cables into "objects", similar to working with modular synthesizers. Just like other creative coding languages have special names for their files (for example, sketches for Processing or cartridges for PICO-8), Max files are called **patches**, like synth patches.

```{=latex}
\begin{center}
```

![|400](https://i.imgur.com/y7iuACg.png){ width=400 }\

\textcolor{lightgray}{Patch notes drawn by Wendy Carlos in 1977}

```{=latex}
\end{center}
```

### Sample by Sample

Within Max, you can generate and process images, sounds, live data, and more; however, gen~ is specifically designed for working with sound at a sample-by-sample level. Normally, **MSP** objects are used for working with sound, as indicated by the tilde (~) symbol in their name. However, they process sound data streams in chunks of samples at a time ("signal vectors", "buffers", or "blocks").

### Export gen~ patches as C++ code

<!-- TODO: is it worth explaining what low-level means? -->
Because gen~ operates at such a low level, it makes it possible to export a patch as C++ code for use in other digital signal processing (DSP) applications. One example would be if you wanted to export your patch to a small microcontroller that specializes in sound for a site-specific installation or for creating a custom, portable instrument.

### The gen~ object

While Max MSP and gen~ workflows are similar, they can be thought of as different languages. Open up a max patch and press the "n" shortcut to create a new object, type in gen~, and press Enter.

```{=latex}
\begin{center}
```

![|300](https://i.imgur.com/Bl5zy2W.png){ width=300 }\

```{=latex}
\end{center}
```

Double-clicking this object will take you to the gen~ environment. You can think of this environment as the subatomic world of digital sound.

```{=latex}
\begin{center}
```

![|300](https://i.imgur.com/ZZcRUMu.png){ width=300 }\

\textcolor{lightgray}{The default patch of a newly create gen~ obejct.}

```{=latex}
\end{center}
```

With the ability to operate on single samples, we can start to explore new possibilities.

## Familiarize yourself with the UI

### Operators

The nature of sonic signal processing is a combination of signal streams and **operations**.

Operators can be found on the left sidebar, or you can type it when you press the `n` keyboard shortcut (for **new** operator). These gen~ operators might have identical names to Max MSP objects, but they are more low-level.

```{=latex}
\begin{center}
```

![|60](https://i.imgur.com/L3RcHCa.png){ height=300 }\

```{=latex}
\end{center}
```


### Ramps, The Universal Primitive of Repeating Change

### Envelopes

Think of envelopes as windows. They contain the "activity" of a neverending signal.

## Things to Know
- All of the processing inside of a gen~ object resembles MSP because processing in gen~ is also **synchronous**.
- There are no cold or hot inlets.
- There is no right-to-left ordering when you think of output from gen~ operators.
- Objects in gen are "**on**" all the time. Even a float operator. The output from a gen~ object is always a signal – it’ll be a 32-bit or 64-bit signal, depending on which version of Max you’re running.
![](https://i.imgur.com/AHS4yBv.png)
- Everything inside of the gen~ patching environment is done using 64-bit floating point numbers – in fact, you don’t need to distinguish between integer values and floating point numbers at all inside of your gen~ patcher (you’ll probably notice that in the example patches and in the work posted to the Forum).
- When you use an argument to set a default value, that value set by the argument is fixed and cannot be changed.
- In Gen you can name parameter operators using an argument, and then use that parameter name when performing calculations. Using them can make your Gen patching a lot nicer looking.
![](https://i.imgur.com/NijSdkq.png)
- Constants
![](https://i.imgur.com/D5KdnKZ.png)
- In the gen~ world, a pulse is the equivalent of a bang message, a transition from a zero value to any non-zero value that happens within the time frame of a single sample.



## Basic Example
![|500](https://i.imgur.com/OK7HD1v.png)
Here you have a normal max cycle~ object with a frequency of 220Hz going into a gen~ object. Inside the gen~ object we have this:

![|400](https://i.imgur.com/7VODaEf.png)

It defines that there is one input with the `[in 1]` object. The audio rate input that is coming in is then modulated by a gen~ `[cycle]` object with a frequency of 2Hz. The result of that is then attenuated by a default amplitude of 0.5, but can be defined as a parameter outside the gen~ environment. The result is the output of the `[gen~]` object.

You can enter the parameter for the amplitude by sending a message with the parameter name followed by its value.

![|300](https://i.imgur.com/LS7Rzku.png)
You can set a min and max value for a parameter by setting the corresponding attributes.

![](https://i.imgur.com/lR0A1xg.png)
As you are making your patch, the equivalent text based code is being updated. To see it click on the 'C' icon on the right sidebar.
![|80](https://i.imgur.com/zsg6s8E.png)
![](https://i.imgur.com/lGx4nKT.png)

## `[noise]`
It is just a random number generator. It outputs a random number between -1 and 1 every sample.

![|300](https://i.imgur.com/6aYJoB5.png)
<i style="color: #ccd3d5;">Inside the gen~ object.</i>
![](https://i.imgur.com/ktFXCZs.png)
```json
"data" : [ -0.962023636649588, -0.288658083802691, 0.574758381195038, 0.575675566991314, 0.966613906230083, 0.396488362616592, -0.336838704314311, -0.405994859607774, -0.681081685566267, 0.24073151207253, 0.042128926192442, -0.353167375977662, -0.103923029340541, 0.36415943796283, -0.947715632541594, 0.695417154910758, 0.068541726423958, -0.461319802713843, 0.47255146777022, 0.336373363043837, 0.742017665547112, -0.192726776108862, -0.900164048922914, -0.750947117349323, 0.521206528128382, 0.457912005855984, 0.143233176527335, -0.641371059859743, 0.028885235320216, -0.569798224625968, 0.047090293060671, -0.967912356300114, -0.730096148882075, -0.085211664178272, -0.99307038195947, -0.022702123954654, 0.11232612525633, -0.333894023639586, 0.924374253452418, 0.349485653323478, -0.397281134428541, -0.658903642374412, 0.748827614806493, 0.665614489482753, 0.997141079648681, 0.839261389642395, 0.593524578503594, 0.241690067558928 ]
```
<i style="color: #ccd3d5;">Data taken from the plot. Notice that they are 64 bit float values.</i>

---  
## `[poke] & [peek]` Reading and Writing Buffer Content
![](https://i.imgur.com/Z7vqTDQ.png)
![](https://i.imgur.com/8JL1PNA.png)

The gen~ code writes a random value into the `mynoise` buffer every sample at the audio rate (48000 times a second in this case). At the same time, another counter is using `peek` to output the value of the buffer. In this second buffer, I can set the amount to add after each count, for example, instead of going through the buffer at the normal speed of 1 sample each time, I can go through it 10, 100, or 1000 samples each time. In this case, I set a number between 0 and 1, because there is no such thing as a decimal sample index, it will hold the same sample it is on until it crosses into another sample index.
<mark style="background: #FFF3A3A6;">Notice how this removes high frequencies.</mark>

Now look at what happens when we interpolate linearly between these 10 samples.
![](https://i.imgur.com/aFnsdbW.png)
![](https://i.imgur.com/uWKAc3h.png)
<i style="color: #ccd3d5;">You can interpolate by setting this attribute value.</i>

<mark style="background: #FFF3A3A6;">Notice how even more high frequencies are removed.</mark>

![](https://i.imgur.com/gN13Vw4.png)
Here we can clearly see what interpolation does. The blue is the sample and hold, and the red is with linear interpolation.

Here is the normal MSP noise for comparison, they are the same thing. A random number generator that outputs a float between -1 and 1.
![](https://i.imgur.com/v7ciycg.png)

