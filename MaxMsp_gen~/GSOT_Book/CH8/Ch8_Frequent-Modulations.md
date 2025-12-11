---
id: Ch8_Frequent-Modulations
aliases:
  - 8. Frequent Modulations
tags: []
book: true
classoption: onecolumn
cover: https://i.imgur.com/MTr2xWV.png
edited_seconds: 2716
pandoc-latex-environment:
  error-box:
    - error
  info-box:
    - info
  tcolorbox:
    - box
  warning-box:
    - warning
progress: starting
status: in progress
titlepage: false
type:
  - Book Notes
updated: 2025-12-04T01:50:45.679-06:00
---
# 8. Frequent Modulations

The point of this chapter is to learn of the different signal modulation techniques.

## Amplitude Modulation

To make an audio signal quieter, you multiply it by a value between 0 and 1.

When the multiplier is a signal that <u>varies over time</u>, it is called a **"modulator"**.

The signal that is being modulated is called the **carrier signal**.

```{=latex}
\begin{center}
```
![](https://i.imgur.com/bvlBTyJ.png){width=300}\
\textcolor{lightgray}{Carrier wave of 100 hz}
```{=latex}
\end{center}
```
```{=latex}
\begin{center}
```
![](https://i.imgur.com/3F6mity.png){width=300}\
\textcolor{lightgray}{Modulator wave of 20 hz}
```{=latex}
\end{center}
```

This process is called **Amplitude Modulation** (AM).

This is similar to how envelopes work. They run from 0.0 (silence) to 1.0 (full amplitude) and back. This envelope is **unipolar**.

```{=latex}
\begin{center}
```
![](https://i.imgur.com/NRXCiWa.png){width=500}\
\textcolor{lightgray}{Resulting modulated wave.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/7dgy6DO.png){ width=500 }\
\textcolor{lightgray}{gen patch for simple AM}
```{=latex}
\end{center}
```

## Ring Modulation

Ring modulation is just the multiplication of two **bipolar** oscillators.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/n5kEIi1.png){ width=500 }\
\textcolor{lightgray}{Notice the two frequencies of the oscillators (1000Hz * 400Hz) are seen in the frequency analyzer.}

```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/Qero9I4.png){ width=500 }\
\textcolor{lightgray}{The resulting wave.}
```{=latex}
\end{center}
```

\pagebreak

**Back to AM**

We can vary the intensity of an amplitude modulation by changing the range of the modulator signal. This can be achieved easily with the `[scale~]` object. Notice how the waveform changes, and notice the frequency analysis.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/Fs5k6pL.png){ width=500 }\
\textcolor{lightgray}{Amplitude Modulation with the low bound set to 0 (full intensity range of 0 - 1)}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/yicqcJN.png){ width=500 }\
\textcolor{lightgray}{Frequency of 1200 hz in the middle from the carrier signal, 800 hz, and 1400 hz as sidebands}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/5nTCqBI.png){ width=500 }\
\textcolor{lightgray}{range of 0.6 to 1}

\hfill
\hfill

![|500](https://i.imgur.com/6QWsVy3.png){ width=500 }\
\textcolor{lightgray}{sidebands are weaker in intensity}
```{=latex}
\end{center}
```

\pagebreak

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/3KMeDW4.png){ width=500 }\
\textcolor{lightgray}{range of 1 - 1 removes the modulator signal entirely}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/rwZM7Q4.png){ width=500 }\
\textcolor{lightgray}{the remaining frequency in the graph is of the carrier signal, 1200 hz}
```{=latex}
\end{center}
```

\pagebreak

If you start going down below 0, the parts of the wave that get multiplied by a negative value get inverted.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/JEvRUkh.png){ width=500 }\
\textcolor{lightgray}{The sidebands are in greater intensity, while the carrier frequency diminishes.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/ovpVxkp.png){ width=500 }\
\textcolor{lightgray}{Compare this with the range of (0.6 - 1). The sideband intensity of this new plot are greater than the carrier signal.}
```{=latex}
\end{center}
```


```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/5r31dXY.png){ width=500 }\
\textcolor{lightgray}{range of (-1 - 1)}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/eDbcQ72.png){ width=500 }\
\textcolor{lightgray}{the remaining frequency peaks are of the sidebands, 1000 hz and 1400 hz. The carrier signal frequency has completely disappeared.}
```{=latex}
\end{center}
```

Once the modulator signal's lower range crossed over to below 0, it became bipolar, therefore becoming **ring modulation** rather than **amplitude modulation**.

\pagebreak


```{=latex}
\begin{center}
```
**Same patch made in gen~**

![|500](https://i.imgur.com/QDB0P5G.png){ width=500 }\
\textcolor{lightgray}{same patch but made with gen~}
```{=latex}
\end{center}
```

::: info

\textcolor{teal}{\textbf{NOTE}}

\hfill

The scale operator has a default upper range value of 1.
```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/NxoXoEo.png){ width=500 }\
\hfill

![|400](https://i.imgur.com/qz69I9r.png){ width=500 }\
```{=latex}
\end{center}
```
By looking at the code sidebar we can see the default values when there is no patch cable connected.

:::

Thus the equation for ring modulation is simply:

$$\LARGE RM = C*M$$

---

To turn a bipolar oscillator to unipolar without the scale operator:

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/RmDOYvG.png){ width=400 }\
\textcolor{lightgray}{start with the bipolar modulator wave.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/SB4Zd0w.png){ width=400 }\
\textcolor{lightgray}{scale it down by multiplying it by 0.5}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/cfQq5q1.png){ width=500 }\
\textcolor{lightgray}{shift it up above 0 by adding 0.5}
```{=latex}
\end{center}
```

This is what the scale function was doing in the gen~ patch. It was scaling it with an upper bound of 1, and with a variable to represent the _lowerbound_. If the lowerbound was 0, it would look like the wave above. If it was -1, it was like the original bipolar oscillator. If above 0, it would be a weaker AM modulator signal.

This is the equation for AM.

$$\LARGE AM = C*((M * 0.5) + 0.5)$$

This is the part that makes the signal weaker by half (attenuation by half).

$$\LARGE (M * 0.5)$$

And this is where it is shifted above 0.

$$\LARGE ((M * 0.5) + 0.5)$$

\pagebreak

Since we know that RM = A * M, then we can rearrange the AM equation.

$$\LARGE AM = C*((M * 0.5) + 0.5)$$

Multiply the C with the contents in the parentheses.

$$\LARGE AM = (C * M * 0.5) + (C * 0.5)$$

We know that C*M is RM.

$$\LARGE AM = (RM * 0.5) + (C * 0.5)$$

Refactor

$$\LARGE AM = (RM + C) * 0.5$$

The last equation is just an average. Remember that an average is the total divided by the number of things being totalled. In this case there are two things added, and then divided by two (Same thing as multiplying by 0.5).

We can demonstrate this by using a `[mix]` operator, where at 0.5 it will be full Amplitude Modulation. At 1, it will be full Ring Modulation, and at 0, it is just the carrier.

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/rAANzqJ.png){ width=500 }\
\textcolor{lightgray}{blending Carrier only, AM, and RM together with the mix operator}
```{=latex}
\end{center}
```

::: box

**TIP**

The Fourier theorem says that any complex periodic signal can be described as a mixture (sum) of sine waves at different frequencies, amplitudes, and phases.

:::

## Make a Sine Wave with a Phasor

Here is a way to make a sine wave with a `[phasor~]` object.
```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/H22RarU.png){ width=300 }\
\textcolor{lightgray}{take a ramp from a phasor and multiply it by 2PI}
```{=latex}
\end{center}
```

Steps:

1. **Ramp**: (0 - 1) \rightarrow\  **Ramp**: (0 - 6.28)
2. **Ramp**: (0 - 6.28) \rightarrow\ sin() function
3. Output of sin() is the resulting wave.

\pagebreak

Result:

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/hTF7y9Y.png){ width=400 }\

\hfill
![|600](https://i.imgur.com/5PGXCZF.png){ width=500 }\
\textcolor{lightgray}{A sine wave generated with the sin() function and a phasor.}
```{=latex}
\end{center}
```

\pagebreak

::: info

\textcolor{teal}{\textbf{NOTE}}

\hfill

The cycle operator is closer to a cos plot. Remember the cycle is a wavetable of a cosine wave.

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/Kq6RT0U.png){ width=400 }\

\hfill
![|600](https://i.imgur.com/wdV4N7k.png){ width=500 }\
\textcolor{lightgray}{A sine wave generated with the cos() function and a phasor.}

\hfill

Notice how the plot is off by one sample.
```{=latex}
\end{center}
```


:::

\pagebreak

## Phase and Frequency Modulation

PM and FM look very similar. The only difference is that one is modulating the phase, and the other is modulating the rate of change of the `[phasor]` operator (how fast the ramp completes a cycle per second).

### Phase Modulation

Below is **phase modulation**. The following image is the gen~ patch used to generate it.

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/fstBm8G.png){ width=400 }\
\textcolor{lightgray}{phase modulation signal}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|300](https://i.imgur.com/YR5uX5t.png){ width=300 }\
\textcolor{lightgray}{the output of a sine function is being summed with a ramp that goes from 0 to 2PI, both combined to be entered as an input to another sine function.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/Znl7iMQ.png){ width=500 }\
\textcolor{lightgray}{spectroscope of the PM wave.}
```{=latex}
\end{center}
```

The process of this was a bit harder to grasp.
Let me attempt to look at the process more closely by going through the samples one by one.

---

First I increased the frequencies of both the carrier and modulator to be able to see a good chunk of the wave in a 44 sample window.

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/efs2g1C.png){ width=500 }\
\textcolor{lightgray}{Carrier is 3000Hz and Modulator is 1200Hz. The wave is a 1ms capture with 44 samples.}
```{=latex}
\end{center}
```

The output of the modulator signal is being summed with the ramp that goes from 0 to TWOPI. I want to see what that summed signal looks like.

::: info

\textcolor{teal}{\textbf{NOTE}}

\hfill

When you see two cables going into one operator, they are being summed.

```{=latex}
\begin{center}
```
![|200](https://i.imgur.com/cFj4z7o.png){ width=250 }\
\textcolor{lightgray}{}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|200](https://i.imgur.com/boA1c36.png){ width=250 }\
\textcolor{lightgray}{}
```{=latex}
\end{center}
```

These two images are showing the same thing. Without the `[+]` operator is cleaner but could confuse a beginner trying to learn.
:::

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/t89ujd0.png){ width=450 }\
\textcolor{lightgray}{Here we have graphed both the ramp that goes from 0 to TWOPI, and the bipolar sin wave.}

![|500](https://i.imgur.com/lDK5YrG.png){ width=450 }\
\textcolor{lightgray}{Now we have graphed the signal that is both signals summed together.}

```{=latex}
\end{center}
```

Here is the plot of the resulting wave after sin() function is applied, along with individual sample values.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/dZvL6tk.png){ width=500 }\
\textcolor{lightgray}{}
```{=latex}
\end{center}
```

```{=latex}
\begin{table}
\begin{tabular}{ll}
Input  & sin() Output \\
&  \\
1.030  & 0.857        \\
1.289  & 0.960        \\
1.546  & 0.999        \\
1.805  & 0.972        \\
2.072  & 0.877        \\
2.352  & 0.710        \\
2.647  & 0.474        \\
2.964  & 0.176        \\
3.304  & -0.161       \\
3.670  & -0.504       \\
4.064  & -0.797       \\
4.487  & -0.974       \\
4.939  & -0.974       \\
-0.863 & -0.759       \\
-0.356 & -0.348       \\
0.176  & 0.175        \\
0.730  & 0.666        \\
1.301  & 0.963        \\
1.886  & 0.950        \\
2.480  & 0.614        \\
3.077  & 0.064        \\
3.675  & -0.508       \\
4.266  & -0.902       \\
4.847  & -0.990       \\
5.412  & -0.765       \\
5.959  & -0.318       \\
6.483  & 0.198        \\
6.982  & 0.643        \\
1.170  & 0.920        \\
1.613  & 0.999        \\
2.026  & 0.898        \\
2.411  & 0.667        \\
2.768  & 0.364        \\
3.100  & 0.041        \\
3.409  & -0.264       \\
3.699  & -0.528       \\
\end{tabular}
\end{table}
```

\pagebreak

### Frequency Modulation

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/ufyaMY2.png){ width=500 }\
![|500](https://i.imgur.com/wqaEwbK.png){ width=500 }\
\textcolor{lightgray}{gen patch for frequency modulation. FM and PM are practically the same.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/dTBXOdl.png){ width=500 }\
\textcolor{lightgray}{The freqscope shows that that the FM signal has similar bands as PM}
```{=latex}
\end{center}
```

---

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/Jmw8sjY.png){ width=500 }\

\hfill

![|300](https://i.imgur.com/N1eySoL.png){ width=200 }\
\textcolor{lightgray}{The wave that is being summed with the Hz amount of the carrier phasor is a sine wave that is 200 Hz in rate and -200 - 200 in the y-range.}
```{=latex}
\end{center}
```

### Modulation Index

The "amount of modulation" can be changed by adding another parameter called the **modulation index**, sometimes called **depth**. An index of 1 is the original amount of modulation.


```{=latex}
\begin{center}
```
**PM**

![|500](https://i.imgur.com/S1gNIeW.png){ width=400 }\
\textcolor{lightgray}{Phase modulation wave with a modulation index of 2}

\hfill

![|500](https://i.imgur.com/FBiBJ84.png){ width=400 }\
\textcolor{lightgray}{The PM gen patch with modulation index.}
![|500](https://i.imgur.com/yo2R2CD.png){ width=400 }\
\textcolor{lightgray}{Frequency bands of PM patch with modulation index of 2. Notice that it has more sidebands.}

```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
**FM**

![|500](https://i.imgur.com/eqGcDkg.png){ width=400 }\
\textcolor{lightgray}{Frequency Modulation wave with a modulation index of 20}

\hfill

![|500](https://i.imgur.com/utZlNvK.png){ width=400 }\
\textcolor{lightgray}{The FM gen patch with modulation index.}
![|500](https://i.imgur.com/CQ7op8p.png){ width=400 }\
\textcolor{lightgray}{More bands start to appear as the index gets higher.}
```{=latex}
\end{center}
```

### Sidebands

As noticed before, the spectra coming out of these two circuits are _identical_.

FM and PM have a lot more sidebands compared to AM, especially if the index is high.

For a carrier frequency of $\LARGE "C"$ and a modulator frequency of $\LARGE "M"$, the output frequencies are at the carrier $\LARGE C$ followed by pairs of sidebands at $\LARGE C+M$ and $\LARGE C-M$ just like AM/RM. 

\hfill

But also at $\LARGE C+2M$ and $\LARGE C-2M$.

\hfill

$\LARGE C+3M$ and $\LARGE C-3M$,

\hfill

and so on.

...

More generally:

$$\LARGE CarrierHz + k * ModulatorHz$$

$$\LARGE CarrierHz - k * ModulatorHz$$

\hfill

Where $\LARGE k$ indicates the whole numbers (1, 2, 3, etc).

For example, with a carrier at 1600Hz and modulator at 100Hz, the spectrum will show a central peak at 1600Hz, sidebands above at 1700Hz, 1800Hz, 1900Hz, and below at 1500Hz, 1400Hz, 1300Hz, etc.

The intensity of each of these pairs of sidebands depends on the modulation index in a complex way. Increasing it will result in brighter and more complex sounds.

### Modulation Index Envelope

Many implementations use an envelope signal to control this modulation index to shape the PM or FM spectrum into an expressive event.

For example, rising quickly to a bright sound and then decaying more slowly to a duller sound, which is a timbral profile common to many musical instruments.

Here is the PM patch with an inlet that will modify the index.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/n8G7tHZ.png){ width=500 }\

\hfill

![|500](https://i.imgur.com/TJeKe85.png){ width=500 }\
\textcolor{lightgray}{The blue plot shows the input envelope (0 - 1), and the orange plot shows the change to the modulation amount with an original index of 3.}
```{=latex}
\end{center}
```

\pagebreak

To get an event we can add an envelope to the whole sound.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/AMAbxE7.png){ width=500 }\

\hfill

![|500](https://i.imgur.com/ZGmNlua.png){ width=500 }\
\textcolor{lightgray}{We can use the same envelope that we are using to change the index for the amplitude of the whole generated sound.}

![|500](https://i.imgur.com/m0PExg1.png){ width=500 }\
\textcolor{lightgray}{It's a good idea to use two different envelopes for more complex sounds.}
```{=latex}
\end{center}
```

### Frequency Ratios and Harmonicity

As you play around with some combinations of frequencies, some are more clangorous, metallic, bell-like, or enharmonic than others. Since sidebands appear at $\LARGE C + k*M$, where $\LARGE k$ is some positive or negative **whole number**, it makes sense that the sidebands will form a more harmonic alignment with the carrier when the *ratio* of the modulator and carrier frequencies is made of simple whole numbers, such as:

- 1:2
- 1:5
- 4:3
- and so on.

This ratio is sometimes called the **harmonicity ratio**.

For example, when the modulator frequency is twice the carrier frequency (a ratio of 2:1), the resulting spectrum will contain only odd harmonics, much like a square wave.

John Chowning has said that it is better to think of there being a fundamental frequency control and to set carrier and modulator as multiples of that **core frequency**.

That way, the spectral shape of the sound stays consistent as the core frequency control changes, and thes ound will be harmonic if the carrier and modulator multipliers form a simple ratio (3:2, 2:3, 3:4, etc.). It is the ratio that defines the **harmonicity**.

This is a revised patch that follows Chowning's recommendation:

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/wnt5wKY.png){ width=400 }\
\textcolor{lightgray}{A new parameter called Hz is added on the left, which multiplies to updated carrier and modulator params that represents a multiple of that core frequency.}
```{=latex}
\end{center}
```

### Parallel Modulators/Carriers

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/kPYi1Om.png){ width=400 }\
\textcolor{lightgray}{Phase Modulation with two modulators. More can be added, but as more get added the waveform becomes more complex.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/3WyPyn3.png){ width=400 }\
\textcolor{lightgray}{Phase Modulation with two carriers. A mix operator is used to blend between the two carriers. A value of 0.0 is carrier1, a value of 1.0 is carrier2, and a value of 0.5 is the average between the two.}
```{=latex}
\end{center}
```

### Using More Complex Waveforms as Modulator Signals

Look at the parallel modulators example. Both sine waves are added together to form one signal.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/PM78JgV.png){ width=500 }\
\textcolor{lightgray}{1 ms plot with a core frequency of 1200 Hz. This is plotting both modulator1 (orange), modulator2 (blue), and the sum of both signals (green). Note how the resulting wave requires a range of -2 and 2 in order to fully see it.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/XVYQHBi.png){ width=350 }\
\textcolor{lightgray}{Frequency plot of modulator1 and modulator2. First peak is 1200 Hz, second peak is 2400 Hz.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/Mu7gaa0.png){ width=350 }\
\textcolor{lightgray}{Frequency plot of the summation of modulator1 and modulator2 wave.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/5PM2tXy.png){ width=500 }\
\textcolor{lightgray}{Frequency plot of the Pulse Modulation Signal. Carrier parameter is 1, meaning that its frequency is 1200 Hz.}
```{=latex}
\end{center}
```

The peaks are: 

- 1200 Hz at -36.31 dB
- 2400 Hz at -31.64 dB
- 3600 Hz at -26.35 dB
- 4800 Hz at -32.76 dB
- 6000 Hz at -32.31 dB
- 7200 Hz at -38.28 dB
- 8400 Hz at -43.79 dB
- 9600 Hz at -51.43 dB
- 10800 Hz at -57.62 dB
- 12000 Hz at -66.22 dB
- 13200 Hz at -75.05 dB

::: info

\textcolor{teal}{\textbf{NOTE}}

\hfill

There is a small peak at around 1Hz. -68.87 dB. Also the exact dB is not the point, rather the ratios of the peaks relative to each other is.

:::

Peaks will continue but gradually lower in intensity.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/A6dHabN.png){ width=500 }\
\textcolor{lightgray}{This spectrogram shows the peaks in different colors depending on intensity. You can see that they gradually get less intense as they get higher in frequency (also lower).}
```{=latex}
\end{center}
```

As a review of how the sidebands of PM work, let's walk it through step by step again.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/bur6rTL.png){ width=500 }\
\textcolor{lightgray}{Carrier is 1200Hz. Modulator1 and Modulator2 are not seen because index of both is 0, meaning there is no modulation. PM is in magenta.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/hej6yrp.png){ width=500 }\
\textcolor{lightgray}{Carrier is 1200 Hz. Modulator 1 is at index 1, meaning it is fully on, and it is also 1200 Hz.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/jHpiNRa.png){ width=500 }\
\textcolor{lightgray}{Frequency peaks of PM with only one modulator at the same frequency as the carrier. Note that some peaks are not seen here, but it definitely continues on. (1.2k, 2.4k, 3.6k, 4.8k, 6k, 7.2k, and so on)}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/iICVPaC.png){ width=500 }\
\textcolor{lightgray}{Both modulators have an index of 1, both with a frequency same as carrier.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/v4vTGsv.png){ width=500 }\
\textcolor{lightgray}{Frequency peaks of PM with both modulators at regular intensity.}
```{=latex}
\end{center}
```
```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/Oz5ILrx.png){ width=500 }\
\textcolor{lightgray}{The last example is the same as using one modulator 
with an index of 2. That is why it results in more sidebands.}
```{=latex}
\end{center}
```

Remember how the sidebands are generated from one modulator. Carrier frequency is at the highest intensity, while the sidebands are CarrierHz +/- ModulatorHz.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/KxklALp.png){ width=500 }\
\textcolor{lightgray}{Plot of wave 
with a carrier of 1200 Hz, and one single modulator of 120 Hz (1200 * 0.1).}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/OzxPYRQ.png){ width=500 }\
\textcolor{lightgray}{Frequency peaks of a signal with a carrier of 1200 Hz, and modulator of 120 Hz.}
```{=latex}
\end{center}
```
```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/GuYqewj.png){ width=500 }\
\textcolor{lightgray}{Carrier at 1200 Hz. Both modulators are at 0.5 index, and a frequency of 120 Hz. Essentially the same as one modulator with an index of 1 and frequency of 120 Hz.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/mtSQTB8.png){ width=500 }\
\textcolor{lightgray}{Carrier at 1200 Hz. Both modulators are at 0.5 index, and a frequency of 120 Hz. Essentially the same as one modulator with an index of 1 and frequency of 120 Hz. (Note: Sidebands decay in intensity quicker)}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/28YIE69.png){ width=500 }\
\textcolor{lightgray}{Carrier at 1200 Hz. Both modulators are at 0.5 index, and a frequency of 120 Hz. Essentially the same as one modulator with an index of 1 and frequency of 120 Hz. (Note: Sidebands decay in intensity quicker)}
```{=latex}
\end{center}
```

Interesting things start to happen as you gradually change one modulator frequency.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/IOHjxnQ.png){ width=500 }\
\textcolor{lightgray}{Modulator1 is 120 Hz, Modulator2 is 123.6 Hz.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/L0KTYJ7.png){ width=500 }\
\textcolor{lightgray}{This spectrogram shows the beating as one modulator is slightly off from the other.}
```{=latex}
\end{center}
```

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/7OkRyZh.png){ width=500 }\
![|500](https://i.imgur.com/Q7pnbji.png){ width=500 }\
![|500](https://i.imgur.com/5FtVY2y.png){ width=500 }\
\textcolor{lightgray}{Modulator1 is 120 Hz, Modulator2 is 600 Hz. We see sidebands at Carrier - Modulator1Hz, and Carrier - Modulator2Hz.}
```{=latex}
\end{center}
```

::: info

\textcolor{teal}{\textbf{NOTE}}

\hfill

The reason it starts to get confusing is because of how the frequencies start to wrap around when they reach 0 and 20,000 Hz. If the sideband falls at -200Hz, it will result in a peak at 200Hz.

:::

The point is this: We can extrapolate that *any* waveform made up of a more complex combination of sine waves will create a whole set of sidebands for each sine wave component.

### Hearing the Difference Between PM and FM

Moving beyond basic sinusoidal modulators, we can start to hear the differences between PM and FM.

Let's try using a triangle modulator.
```{=latex}
\begin{center}
```
![|200](https://i.imgur.com/MqonExh.png){ width=150 }\
![|500](https://i.imgur.com/DArw4fx.png){ width=500 }\
\textcolor{lightgray}{Modulator signal that is a triangle wave.}
![|500](https://i.imgur.com/VunZtVB.png){ width=500 }\
![|500](https://i.imgur.com/Kd2v8k7.png){ width=500 }\
\textcolor{lightgray}{Note how the harmonics fall quickly with a triangle wave. In this spectrogram the triangle signal has a fundamental frequency of 400 Hz.}
```{=latex}
\end{center}
```

::: info

\textcolor{teal}{\textbf{NOTE}}

\hfill

The ratios of a triangle wave harmonics are only odd numbers. For example, with a fundamental of 400 Hz, we have a harmonic at 3:1 (1200 Hz), 5:1 (2000 Hz), 7:1 (2800 Hz) and so on. The intensities can also be predicted, with a pattern of 1/3, 1/5, 1/7, and so on.

:::

In order to hear the difference between FM and PM, let's keep the triangle wave modulator at a very low frequency:

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/mOLRCaC.png){ width=500 }\
\textcolor{lightgray}{PM waveform.}

\hfill

![|500](https://i.imgur.com/qLAy9eH.png){ width=400 }\
\textcolor{lightgray}{PM spectrogram with a carrier at 600 Hz, and a modulator at 3 Hz. Index is high value like 143.
![|500](https://i.imgur.com/6TlhFwT.png){ width=500 }\
\textcolor{lightgray}{FM waveform.}

\hfill

![|500](https://i.imgur.com/xGxr4id.png){ width=400 }\
\textcolor{lightgray}{FM spectrogram with same carrier and modulator.}
```{=latex}
\end{center}
```

Let's take a look at another quick example to ensure we have an understanding.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/DzkKAyW.jpeg){ width=500 }\
\textcolor{lightgray}{Using Partiels by IRCAM we can look at a Spectogram. A breakdown of the sections is below.}
```{=latex}
\end{center}
```


1. First section is the carrier wave of 1500 Hz.

2. Carrier: **1500 Hz**; Modulator: (**300 Hz**, index: **0.5**)


Sidebands (+):

- 2700 Hz (+ 1200 (ModulatorHz * 4)); 0.0001 A.
- 2400 Hz (+ 900 (ModulatorHz * 3)); 0.0021 A.
- 2100 Hz (+ 600 (ModulatorHz * 2)); 0.024 A.
- 1800 Hz (+ 300 (ModulatorHz * 1)); 0.195 A.

Carrier 1500 Hz. 0.757 Amplitude

Sidebands (-):

- 1200 Hz (- 300 (ModulatorHz * 1)); 0.1957 A.
- 900 Hz (- 600 (ModulatorHz * 2)); 0.0236 A.
- 600 Hz (- 900 (ModulatorHz * 3)); 0.002 A.
- 300 Hz (- 1200 (ModulatorHz * 4)); =.0001 A.

3. Carrier: **1500 Hz**; Modulator1: (**300 Hz**, index: **0.5**); Modulator2: (**300 Hz**, index: **0.5**)


Same sidebands, but you can see that they all gain more energy. Similar to index 1.0.

1. Carrier: **1500 Hz**; Modulator1: (**300 Hz**, index: **0.5**); Modulator2: (**600 Hz**, index: **0.5**)

Sidebands (+):

- 4200 Hz (+ 1200 (ModulatorHz * 4)); 0.00001 A.
- 3900 Hz (+ 1200 (ModulatorHz * 4)); 0.0002 A.
- 3600 Hz (+ 1200 (ModulatorHz * 4)); 0.0005 A.
- 3300 Hz (+ 1200 (ModulatorHz * 4)); 0.0025 A.
- 3000 Hz (+ 1200 (ModulatorHz * 4)); 0.006 A.
- 2700 Hz (+ 1200 (ModulatorHz * 4)); 0.0275 A.
- 2400 Hz (+ 900 (ModulatorHz * 3)); 0.048 A.
- 2100 Hz (+ 600 (ModulatorHz * 2)); 0.2 A.
- 1800 Hz (+ 300 (ModulatorHz * 1)); 0.1545 A.

Carrier 1500 Hz. 0.711 Amplitude

Sidebands (-):

- 1200 Hz (- 300 (ModulatorHz * 1)); 0.2186 A.
- 900 Hz (- 600 (ModulatorHz * 2)); 0.1689 A.
- 600 Hz (- 900 (ModulatorHz * 3)); 0.0505 A.
- 300 Hz (- 1200 (ModulatorHz * 4)); 0.0189 A.

