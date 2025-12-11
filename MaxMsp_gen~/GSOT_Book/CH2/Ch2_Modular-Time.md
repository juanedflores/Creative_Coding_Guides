---
id: Ch2_Modular-Time
aliases:
  - 2. Modular (Arithmetic of) Time
tags: []
book: true
classoption: onecolumn
cover: https://i.imgur.com/UgnDhPz.png
edited_seconds: 32
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
title: Ch2 Modular Time
titlepage: false
titlepage-rule-height: 0
titlepage-text-color: FF5f87
titlepage-text-size: 34pt
type:
  - Book Notes
updated: 2025-11-10T00:22:02.645-06:00
---
# 2. Modular (Arithmetic of) Time

In gen~, the passing time of a signal is sliced into **sample frames** at a rate defined as the **samplerate**. The samplerate is the number of sample frames that pass per second.

Remember that gen~ is calculating every passing sample frame. So think of the whole patch moving forward as a whole, one sample frame at a time.

There is a samplerate operator to see what the global sample rate is.

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/UTUqVul.png){ width=250}\
\textcolor{lightgray}{in gen~}

\hfill

![|400](https://i.imgur.com/wVnhSqp.png){ width=250}\
\textcolor{lightgray}{in Max}
```{=latex}
\end{center}
```

## A simple counter

To create a simple counter, all we need are two objects: 

- `[+]`
- `[history]`

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/6scaNTg.png){ width=300}\
\textcolor{lightgray}{Outside the gen~patch shows a toggle in its first inlet, and a `number~` object for its output.}

\hfill 

![|300](https://i.imgur.com/9EyQdry.png){ width=300}\
\textcolor{lightgray}{gen~ patch}

```{=latex}
\end{center}
```

When the toggle is on, it sends a value of 1.  When DSP is on, `[in 1]` will send a 1, then it will add 1 + 0, because the `[history]` object starts at 0, then sends it out to `[out 1]`.

On the next sample frame, 1 comes from `[in 1]`, and then it will do the addition of 1 + 1, because 1 was stored in the `[history]` object last sample frame. It will send the 2 to `[out 1]`, and will repeat. On the 48000th sample frame (if at a samplerate of 48k), it will accumulate to 48,000, after exactly 1 second.

Since we know that 48k is one second, we can also get the time elapsed by dividing it by `[samplerate]`.

## Adding a reset

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/eDSun5Y.png){ width=300}\
\textcolor{lightgray}{The Max patch. Adding a `click~` (a one sample spike) will reset the count back to 0.}

\hfill

![|400](https://i.imgur.com/ddtKltA.png){ width=300}\
\textcolor{lightgray}{gen~ patch introduces a `switch` operator.}
```{=latex}
\end{center}
```

### The switch operator (?)

::: box

\textcolor{black}{\textbf{DESCRIPTION}}

\hfill

**Conditional Ternary Operator**

\hfill

Selects between the second and third inputs according to the boolean value of the first. If the first argument is true, the second argument will be output. Otherwise, the third argument will be output.

\hfill

Same as the `?` operator.

\hfill

(inlet1: **condition to test**, inlet2: **value if true**, inlet3: **value if false**)

:::

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/tmvrcvK.png){ width=300}\
\textcolor{lightgray}{Illustration showing that switch allows 3rd inlet through when input is 0, and 2nd inlet when input is non-zero. }
```{=latex}
\end{center}
```

In code form:

```js
switch = boolean_input ? inlet2 : inlet3;
```

### The accum operator

The patch we built is functions exactly like the `accum` operator.

::: box

\textcolor{black}{\textbf{DESCRIPTION}}

\hfill

**An Additive Accumulator**

\hfill

The object adds to, and then outputs, an internal sum. This occurs at sample-rate, so the sum can grow very large, very fast. The value to be added is specified by either the first inlet or argument. The internal sum can be reset to the minimum by sending a nonzero value to the right-most inlet. The minimum value is 0 by default, but can be changed with the @min attribute. An optional maximum value can be specified with the @max attribute; values will wrap at the maximum. 

\hfill

(inlet1: **amount to add**, inlet2: **nonzero reset**)

:::

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/vOfSFYm.png){ width=200}\
\textcolor{lightgray}{Same as the previous patch.}
```{=latex}
\end{center}
```

```js
plusequals_1 = plusequals(in1, in2);
out1 = plusequals_1;
```

\pagebreak

## Playing a Sound File

Let's load an audio file into a `buffer~`.

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/gNu9vzn.png){ width=500}\
\textcolor{lightgray}{duduk.aif loaded into a buffer called `mybuf`}
```{=latex}
\end{center}
```

Use the `buffer` operator to load it into gen~. 

### The buffer Operator

::: box

\textcolor{black}{\textbf{DESCRIPTION}}

\hfill

**A Reference to an External buffer~ Object**

\hfill

References an external named buffer~ object. The first argument specifies a name by which to refer to this data in other objects in the gen patcher (such as peek and poke); the second optional argument specifies the name of the external buffer~ object to reference (if ommitted, the first argument name is used). The first outlet sends the length of the buffer in samples; the second outlet sends the number of channels. 

\hfill

arguments: (**1. buffer_name**)

\hfill

(outlet1: **length in samples**, outlet2: **number of channels**)

\hfill

:::


```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/cwboGuv.png){ width=500}\
\textcolor{lightgray}{gen~ patch showing the output of the first oulet of the buffer operator.}

\hfill

![|400](https://i.imgur.com/3VQqAHm.png){ width=500}\
\textcolor{lightgray}{The max patch showing the number of samples in the buffer.}
```{=latex}
\end{center}
```

To read the data in the buffer in gen~, we can use the `peek` operator.

### The peek operator

::: box

\textcolor{black}{\textbf{DESCRIPTION}}

\hfill

**Read values from a data/buffer object **

\hfill

Read values from a data/buffer object. The first argument should be a name of a data or buffer object in the gen patcher. The second argument specifies the number of output channels. The first inlet specifes a sample index to read (no interpolation); indices out of range return zero. The last inlet specifies a channel offset (default 0). 

\hfill

arguments: (1. **name**, 2. **channels**)

\hfill

outlets:

\hfill

(1: **sample index to read**, 2: **channel_offset**)

\hfill

:::

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/TSJ5u1H.png){ width=500}\
\textcolor{lightgray}{gen~ patch with the peek operator.}
```{=latex}
\end{center}
```

This patch plays through the file once but it doesn't loop, because it just keeps accumulating until it is reset manually.

## Looping a Buffer

We can have the buffer playback loop by using a ´wrap´ operator.

### The wrap operator

::: box

\textcolor{black}{\textbf{DESCRIPTION}}

\hfill

**Wrap input to a range within a low and high output value  **

\hfill

Low and high values can be specified by arguments or by inlets. The default range is 0..1. 

\hfill

arguments: (1. **input**, 2. **min**, 3. **max**)

\hfill

outlets:

\hfill

(1: **sample index to read**, 2: **channel_offset**)

\hfill

:::

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/OxBNN8G.png){ width=300}\
\textcolor{lightgray}{Adding the wrap with the max argument being provided by the buffer operator (giving the buffer sample size.)}
```{=latex}
\end{center}
```

## Wavetable Synthesis

Let's understand the concept of wavetable synthesis by trying to design a Sin Wave Generator.

Here is the general formula:

\hfill

\begin{align*}\scalebox{2}{$\LARGE s(t) = Asin(2\pi ft + \phi)$}\end{align*}

\hfill

or

\begin{align*}\scalebox{2}{$\LARGE Asin(\omega t + \phi)$}\end{align*}

\hfill

Where:

\hfill

- A: **Amplitude**, the peak deviation of the function from zero.
- $f$: **frequency**, the number of oscillations (cycles) that occur each second of time.
- $\phi$: **phase**, specifies (in radians) where in its cycle the oscillation is at t = 0.
