---
id: Ch8_Frequent-Modulations
aliases:
  - 8. Frequent Modulations
tags: []
book: true
classoption: onecolumn
cover: https://i.imgur.com/PtaK6Ef.png
edited_seconds: 92
pandoc-latex-environment:
  error-box:
    - error
  info-box:
    - info
  tcolorbox:
    - box
  warning-box:
    - warning
titlepage: false
updated: 2025-11-10T00:22:43.164-06:00
---
# 8. Frequent Modulations

The point of this chapter is to learn how to modulate one audio signal with another.

## Amplitude Modulation

To make an audio signal quieter, you multiply it by a value of less than one. When the multiplier is a signal that <u>varies over time</u>, it is called a **"modulator"**.

The signal that is being modulated is called the **carrier signal**.

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/5jFOHMj.png){ width=300 }\
```{=latex}
\end{center}
```

![|400](https://i.imgur.com/PkFTAa4.png)
<i style="color: #ccd3d5;">Blue is Carrier, Red is Sub-Audio Modulator.</i>

![](https://i.imgur.com/PtaK6Ef.png)
<i style="color: #ccd3d5;">The resulting Amplitude Modulated waveform plotted for 1 second.</i>

![](https://i.imgur.com/oCamMvl.png)
<i style="color: #ccd3d5;">Carrier wave at 500Hz, Modulator at 200Hz, and lowerbound at 0.5, affecting the modulation depth.</i>

![](https://i.imgur.com/42rDmlR.png)

![](https://i.imgur.com/qz69I9r.png)
<i style="color: #ccd3d5;">The scale operator has a default upper bound of 1, so when the lowerbound variable is set to -1, the scale object is doing nothing at all. It is just multiplying two bipolar oscillators together. This is ring modulation.</i>

## Ring Modulation
![](https://i.imgur.com/YAL778L.png)

To prove that Ring Modulation is just the multiplication of two bipolar oscillators:
![](https://i.imgur.com/FNzWv08.png)

Thus the equation is simply:
$$\LARGE RM = C*M$$
## Amplitude Modulation
For AM, it is multiplying a bipolar oscillator with a unipolar oscillator.

To turn a bipolar oscillator to unipolar, observe this example:
![](https://i.imgur.com/RmDOYvG.png)
We have a 200Hz sine wave plotted for 10ms.

We can make it weaker by half by multiplying it by 0.5.
![](https://i.imgur.com/SB4Zd0w.png)

And shifting up above 0:
![](https://i.imgur.com/cfQq5q1.png)

This is what the scale function was doing in the gen~ patch. It was scaling it with an upper bound of 1, and with a variable lowerbound. If the lowerbound was 0, it would look like the wave above. If it was -1, it was like the original bipolar oscillator. If it was above 0, it would be a weaker modulation depth.

This is the equation for AM.
$$\LARGE AM = C*((M * 0.5) + 0.5)$$
This is the part that makes the signal weaker by half (attenuation by half).
$$\LARGE (M * 0.5)$$
And this is where it is shifted above 0.
$$\LARGE ((M * 0.5) + 0.5)$$
Here is an example in normal Max MSP to show this.
![](https://i.imgur.com/2lEuSQV.png)

Since we know that RM = A * M, then we can rearrange the AM equation.
$$\LARGE AM = C*((M * 0.5) + 0.5)$$
Multiple the C with the contents in the parentheses.
$$\LARGE AM = (C * M * 0.5) + (C * 0.5)$$
We know that C*M is RM.
$$\LARGE AM = (RM * 0.5) + (C * 0.5)$$
Refactor
$$\LARGE AM = (RM + C) * 0.5$$

The last equation is just an average. Remember that an average is the total divided by the number of things being totalled. In this case there are two things added, and then divided by two (Same thing as multiplying by 0.5).

We can demonstrate this by using a `[mix]` operator, where at 0.5 it will be full Amplitude Modulation. At 1, it will be full Ring Modulation, and at 0, it is just the carrier.

![](https://i.imgur.com/ZHW8FOr.png)

## Frequency Modulation
Here is a way to make a sine wave with a `[phasor~]` object.
![|400](https://i.imgur.com/H22RarU.png)
You scale a phasors range of 0 - 1, to 0 - TWO_PI, then send it to the sin function.

![](https://i.imgur.com/7N4q55r.png)

To make PM and FM in gen, it looks very similar. The only difference is that one is modulating the phase, and the other is modulating the rate of change of the `[phasor]` operator.
![](https://i.imgur.com/HZMbKG4.png)

![](https://i.imgur.com/semrU6a.png)

### Adding Envelopes
Here is an example of a trumpet sound with an envelope on the amplitude and index, duration of 600ms.
![](https://i.imgur.com/kx3Ucuw.png)

You can push this further by having a fundamental frequency as an input and just determining the ratio you want for the carrier and modulator. This way you can keep the same change in timbre with different pitches.
![](https://i.imgur.com/oHZgbhc.png)
![](https://i.imgur.com/0oYZGNy.png)
