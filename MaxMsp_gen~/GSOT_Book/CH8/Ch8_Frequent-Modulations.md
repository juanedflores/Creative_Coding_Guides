---
id: Ch8_Frequent-Modulations
aliases:
  - 8. Frequent Modulations
tags: []
book: true
classoption: onecolumn
cover: https://i.imgur.com/MTr2xWV.png
edited_seconds: 802
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
updated: 2025-11-22T16:38:40.777-06:00
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
