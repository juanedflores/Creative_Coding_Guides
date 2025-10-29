---
id: getting_started
aliases:
  - Getting Started with PICO-8
tags:
  - guide
author: Juan Eduardo Flores
book: true
classoption: onecolumn
cover: https://i.imgur.com/eBJ4EqC.png
edited_seconds: 1098
pandoc-latex-environment:
  error-box:
    - error
  info-box:
    - info
  tcolorbox:
    - box
  warning-box:
    - warning
title: Getting Started with PICO-8
titlepage: true
titlepage-background: /Users/juaneduardoflores/Downloads/clouds_export.png
titlepage-rule-height: 0
titlepage-text-color: FF5f87
titlepage-text-size: 24pt
updated: 2025-10-29T06:20:43.996-05:00
---

# Getting Started with PICO-8

## <u>Introduction</u>

PICO-8 is a popular example of a **fantasy console**. A fantasy console is a fictitious video game console played on an emulator (a software that imitates the architecture of a specific hardware).

PICO-8 creates the experience of retro gaming using the \textcolor{blue}{Lua programming language} and with very specific technical limitations. It can be a fun way to learn programming and game design.

The creator of PICO-8, described the term:

> A fantasy console is like a regular console, but without the inconvenience of actual hardware. PICO-8 has everything else that makes a console a console: machine specifications and display format, development tools, design culture, distribution platform, community, and playership. It is similar to a retro game emulator, but for a machine that never existed.
> 
> \- Joseph White

## <u>Influences</u>

The PICO-8 is a computer that never existed, but it is inspired by real computers from the 1980s.

::: columns

![|400](https://i.imgur.com/EjYUBbn.png){ height=250 }\

\textcolor{lightgray}{Apple IIe}

![|400](https://i.imgur.com/sMaaeHj.png){ height=250 }\

\textcolor{lightgray}{Commodore 64}


:::

::: columns

The **Apple IIe** was released in January 1983. It was intended for home and educational use. It had a 280x192 pixel display with 6 colors for high resolution, and 16 colors for low resolution.
  

The **Commodore 64** has a 320x200 pixel display with 16 colors. It was released in August 1982 and became the best-selling single computer model of all time.
  
:::

::: columns

```{=latex}
\begin{center}
```

![|200](https://i.imgur.com/d4lzO0X.png){ height=90 skipabove=0.5cm }\


![|200](https://i.imgur.com/gkO7cC1.png){ height=90 }\

```{=latex}
\end{center}
```

:::

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/UFC247G.png){ width=70% }\
\textcolor{lightgray}{BBC Micro}
```{=latex}
\end{center}
```

\hfill \break

::: columns

The **BBC Micro** was a family of computers designed by Acorn Computers as part of the BBC's Computer Literacy Project in the early 1980s, aimed at promoting computer literacy in the UK.

In 1982, there was a TV series called _The Computer Programme_, which focused on learning how to use this machine. It was broadcast on BBC2.

It can be switched between several display modes. Modes 0 to 6 could display a palette of sixteen colors using the eight basic colors at the vertices of the RGB color cube and eight flashing colors made by alternating the basic color and its inverse.

Mode 0 has a resolution of 640x256 pixels.

```{=latex}
\begin{center}
```

![|200](https://i.imgur.com/rnkAIjy.png){ width=150 }\

```{=latex}
\end{center}
```

:::

\pagebreak
\hfill

```{=latex}
\begin{center}
```

![A caption|300](https://i.imgur.com/Jnn3tGh.png){ width=57% }\

BBC Micro running on an emulator.

\hfill \break

![A caption|300](https://i.imgur.com/LTuaPOl.png){ width=57% }\

PICO-8's Command Line Interface.

```{=latex}
\end{center}
```

\pagebreak

## Command Line Interface (CLI) / Terminal / Console / Shell

Now that you can see the inspiration, let's get familiar with the command line interface because it is the first thing you see when you start PICO-8.

It displays the logo, some version information, and a prompt to enter [commands]{.underline}.

The **>** symbol followed by the blinking red cursor indicates that the system is ready to accept [user input]{.underline}.

### Historical Background

![|700](https://i.imgur.com/OrdaN0l.png){ width=100% }\
\textcolor{lightgray}{Desktop interface of the Magic Cap operating system. It used the "desktop metaphor", which uses imagery that represent a real physical desktop.}

\hfill

Before Graphical User Interfaces (GUIs) that rely on the use of a mouse to click graphic icons that resemble real-world objects to open and close windows, there was the command line interface (CLI). 

> According to a wikibook Operating System Design: "A [command line interface or CLI]{.underline} is a method of interacting with a computer by giving it lines of textual commands

**CLI**, **terminal**, **console**, and even **shell** are all terms that are often used interchangeably to indicate a text based system for navigating an operating system. It could get confusing, but they all refer to similar concepts.

\pagebreak

A [Terminal]{.underline} is a program that emulates a physical terminal, which historically was an electromechanical device that connected to a larger computer to interact with its functions.

On a terminal, you can type commands, press enter, and see the results.

It comes from a history that predates screens where a printer was used to print the results of our commands. See:

- [Z3 (1941)](https://en.wikipedia.org/wiki/Z3_(computer))
- [Teleprinter](https://en.wikipedia.org/wiki/Teleprinter)
- [Teletype Model 33 (1963)](https://en.wikipedia.org/wiki/Teletype_Model_33)

---

A [Console]{.underline} was initially the switches and indicators available literally on the console panel of a computer.

```{=latex}
\begin{center}
```

![|500](https://i.imgur.com/mkMpdku.png){ width=50% }\
\textcolor{lightgray}{The front panel of the PDP-11/20, which ran the 1st edition of Unix in 1972.}

```{=latex}
\end{center}
```

Later the term was used for a special teletype/terminal attached to the computer. The operator could use the console to perform privileged operations.

---

In the world of Unix, a [Shell]{.underline} is a command-line interpreter that provides a user interface for access to an operating system's services. There are many different Unix shells. Popular shells for interactive use include [Bash]{.underline}, [Zsh]{.underline}, and [Fish]{.underline}.

In Unix based systems like Linux or MacOS, you see this command prompt: 

```shell
$
```

In Windows, you might see what is seen in PICO-8, the **>** symbol, prompting the user to enter a command. It is based on the Microsoft Disk Operating System (MS-DOS) command line interface.

\pagebreak

### SPLORE & File System Navigation Commands

PICO-8 actually tells you to type **HELP** for help. By typing help and pressing enter, you get in return a list of commands that you can use in PICO-8.

```{=latex}
\begin{center}
```

![|400](https://i.imgur.com/EY2cHO6.png){ width=80% }\

```{=latex}
\end{center}
```

Before we learn how to install demos and run them, let's type the command that is in \textcolor{magenta}{pink text: SPLORE}. Remember that the computer does not receive the typed command until you press the **ENTER** key.

\commandline{> \textbf{SPLORE}}

::: info

In PICO-8, everything is uppercase. If you try typing uppercase letters by pressing Shift, you will find that you will get random symbols instead. Just type in lowercase letters when entering commands and when you start to write code later on.

:::

[SPLORE]{.underline} is a graphical interface for exploring PICO-8 cartridges that others have written and published. Here you can also publish your own games. Think of it as a way to explore and browse through a library of games that the public contributes to.

\pagebreak

```{=latex}
\begin{center}
```
::: columns
![|400](https://i.imgur.com/S8YRq2w.png){ height=250 }\

![|400](https://i.imgur.com/ynqgZuF.png){ height=250 }\
:::
```{=latex}
\end{center}
```
```{=latex}
\begin{center}
```
\textcolor{lightgray}{BUBBLEGUM SPIN by BEE\_RANDON. Being played after navigating SPLORE}
```{=latex}
\end{center}
```

Navigate around using the arrow keys on your keyboard, and use the **Z** key to select an option and to run a cart. The **ESC** key is also very useful for many purposes. It is typically used to exit or to pause the game.

---

This is an opportunity to introduce one quirk of PICO-8 games: they only use up to six different buttons for input, comprising the four arrow keys and two additional buttons.

```{=latex}
\begin{center}
```

![|300](https://i.imgur.com/emvmmoT.png){ width=50% }\

```{=latex}
\end{center}
```

By default, the **Z** key is the [O] and the **X** key is the [X] button. You could also use C/V or N/M respectively. These buttons are configurable, allowing you to change them if desired.

::: warning

\commandline{> \textbf{KEYCONFIG}}

\hfill

This command is used to change the key assignments for the six buttons, for each of the two players. Be cautious when using this command, as it will modify the key bindings for all PICO-8 games until you reset them.

\hfill

If that happens, you can reset to default by entering keyconfig and then pressing the **DELETE** key on your keyboard for each input.

```{=latex}
\begin{center}
```

![](https://i.imgur.com/4cwFqXF.png){ width=50% }\

```{=latex}
\end{center}
```

:::

---

While getting to have fun in SPLORE, you might notice that the games are limited to a 16 color palette and a small resolution of **128 x 128 pixels**. This is part of the design culture of PICO-8, which embraces limitations to inspire creativity.

```{=latex}
\begin{center}
```
![|400](https://i.imgur.com/HTZrefn.png){ width=70% }\

![|300](https://i.imgur.com/ZBqDcAr.png){ width=50% }\
```{=latex}
\end{center}
```

Other limitations worth mentioning:

- 4-channel sound
- 8192 tokens (code size, the number of characters you are allowed to use)

### File Navigation

In the command line, we don't have a GUI to click on folders or files, so we need to learn how to get around our file system using text commands.

What we know as folders in GUIs are called **directories** in command line interfaces.

To view the files and directories in the current directory, we can use the 'ls' command.

::: info

\commandline{> \textbf{LS}}

\hfill

**LS** stands for "list". It lists all files and directories in the current directory.

:::

Currently, we don't have any directories, so nothing is listed under what is our [home directory]{.underline}. This directory is represented by the lone forward slash `/`.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/5S3Wsi5.png){ width=70% }\
```{=latex}
\end{center}
```

Let's try this command next:

```shell
> INSTALL_DEMOS
```

This will install some demo cartridges into our file system. Try typing **LS** again to see the newly created directory.

```{=latex}
\begin{center}
```
![|500](https://i.imgur.com/yYmgR4b.png){ width=70% }\
```{=latex}
\end{center}
```

At the bottom of the screen, we can see:

```shell
DIRECTORY: /
DEMOS
````

To enter the DEMOS directory, we can use the **CD** command.

::: info
```shell
> CD <directory_name>
```

CD stands for "change directory." It allows us to navigate into a different directory.
:::

```shell
> CD DEMOS
```

```{=latex}
\begin{center}
```
![](https://i.imgur.com/Ti9UTpC.png){ width=80% }\
```{=latex}
\end{center}
```

Now, if we type **LS** again, we can see the demo cartridges that were installed.

```{=latex}
\begin{center}
```
![](https://i.imgur.com/mLmMQDI.png){ width=80% }\
```{=latex}
\end{center}
```

To run a cartridge, we can use the **LOAD** command followed by the name of the cartridge.

::: info

```shell
> LOAD <cartridge_name>
```

Loads the specified cartridge.

:::

::: box

**TIP**

A tip when typing file or directory names: you can use the TAB key to auto-complete names. Just type the first few letters and press TAB, and it will fill in the rest for you if there is a unique match.

:::

```shell
> LOAD API.P8
```

```{=latex}
\begin{center}
```
![](https://i.imgur.com/yW7pUTc.png){ width=80% }\
```{=latex}
\end{center}
```

Lastly, use the **RUN** command to run the cartridge.

::: info

```shell
> RUN
```

Runs the currently loaded cartridge.

:::

```{=latex}
\begin{center}
```
![](https://i.imgur.com/z8Chors.png){ width=60% }\
```{=latex}
\end{center}
```

\textcolor{red}{API.P8} is now running! Pressing **ESC** will bring you back to the command line interface.

::: box

**TIP**

You can press **Ctrl + L** to clear the terminal screen!

:::

::: box

**TIP**

Instead of typing **RUN** each time, you could just press **Ctrl + R** to run the currently loaded cartridge or restart it.

:::

\pagebreak

## The Code Editor

To access the code editor, press the **ESC** key while in the command line interface.

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/SpdntJL.png){ width=60% }\
```{=latex}
\end{center}
```

You may notice how we have a mouse! Yes, this is a graphical user interface (GUI) for writing code. On the top right are icons to navigate through different types of editors, but for now, press **ESC** again to return to the command line interface.

---

## Simple Functions

Before writing a game, you can get acquainted with some simple functions in the console.

```lua
-- Print "HELLO WORLD" to the console
PRINT("HELLO WORLD")

```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/su0WADl.png){ width=60% }\
```{=latex}
\end{center}
```

```lua
-- Draw a rectangle at x = (80, 80)
-- and y = (120, 100)
-- with a fill color of 12
RECTFILL(80,80,120,100,12)
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/tYCbXLl.png){ width=60% }\
```{=latex}
\end{center}
```

\pagebreak

## Core Functions

There are three core functions that PICO-8 uses to run a program.

```lua
function _init()
    -- This function runs once when the program starts
end

function _update()
    -- This function runs 30 times per second
end

function _draw()
    -- This function also runs 30 times per second
end
```

\pagebreak

## Making a Simple Animation

As a first exercise let's create a floating cloud like Cory Arcangel's [Super Mario Clouds](https://en.wikipedia.org/wiki/Super_Mario_Clouds).

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/cD1M3hp.png){ width=100% }\
```{=latex}
\end{center}
```

### Sprite Editor

To navigate to the sprite editor, go to the editor and click on the icon that looks like a little character with two eyes.

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/8sHNuNN.png){ width=80% }\
```{=latex}
\end{center}
```

Here, you can draw a sprite within this 8x8 pixel canvas.

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/eBJ4EqC.png){ width=60% }\
```{=latex}
\end{center}
```

Note how I draw it in the top left-most tile, which is assigned the number "000".

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/L4slxvK.png){ width=60% }\
```{=latex}
\end{center}
```

Return to the terminal screen by pressing "ESC" again.

### The spr() function

You can draw a sprite onto the screen by using the spr() function.

The first parameter is _n_, which is the assigned **number of the sprite**. In our case, we drew our sprite in the top left-most box, which is assigned the value of 0.

```lua
-- spr(sprite_number)

-- draw sprite 0,
spr(0)
```

The second and third parameters are X and Y coordinates for where it will be drawn, referring to the sprite's top-left pixel.

```lua
-- spr(sprite_number, x, y)

-- draw sprite 0, at (x=20, y=20)
spr(0, 20, 20)
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/WgBXIPA.png){ width=90% }\
```{=latex}
\end{center}
```

There are even more parameters! They are optional. You could specify how many tiles wide or tall to draw from the sprite sheet.

For example, if you had more drawn sprites in the sprite editor:

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/eWfWkN7.png){ width=90% }\
```{=latex}
\end{center}
```

You could draw more than one using the sprite command if that is useful to you.

```lua
-- spr(sprite_number, x, y, w, h)

-- draw from sprite 0 at (20, 20), with tile width of 1 and height of 2 included
spr(0, 20, 20, 1, 2) 
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/n97sdbS.png){ width=90% }\
```{=latex}
\end{center}
```

```lua
-- draw from sprite 0 at (20, 20), with tile width of 2 and height of 1 included
spr(0, 20, 20, 2, 1) 
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/tvhUJS4.png){ width=90% }\
```{=latex}
\end{center}
```

```lua
-- draw from sprite 0 at (20, 20), with tile width of 2 and height of 2 included
spr(0, 20, 20, 2, 2) 
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/W5dhbZJ.png){ width=90% }\
```{=latex}
\end{center}
```

Here is a drawing with the different `w` and `h` values and what they would draw:

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/iQw6UhK.png){ width=90% }\
```{=latex}
\end{center}
```

The last two optional parameters are booleans (true or false). They are `flip_x` and `flip_y`, used to flip the sprite vertically or horizontally, as desired.

```lua
-- draw 2x2 tiles at (20, 20), flip it vertically (flip x).
spr(0, 20, 20, 2, 2, true, false)
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/wC13M6F.png){ width=90% }\
```{=latex}
\end{center}
```

```lua
-- draw 2x2 tiles at (20, 20), flip it horizontally (flip y).
spr(0, 20, 20, 2, 2, false, true)
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/hhh86zT.png){ width=90% }\
```{=latex}
\end{center}
```

```lua
-- draw 2x2 tiles at (20, 20), flip it vertically.
spr(0, 20, 20, 2, 2, true, true)
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/u32knM5.png){ width=90% }\
```{=latex}
\end{center}
```

### Making it Move

Let's draw our cloud sprite and make it move across the screen!

First let's choose an initial X and Y position for our cloud, plug it into the `spr()` function, and write that inside the `_draw()` function.

```lua
function _draw()
  -- draw cloud sprite at (20, 20)
  spr(0, 20, 20)
end
```

#### Variables:

We can use variables to store the X and Y position of our cloud. In order to make the cloud move horizontally, we will need to change its X position over time, this is where variables come in handy.

Let's create a variable for the cloud's x position: `cloud_x`.

```lua
cloud_x = 20

function _draw()
  -- draw cloud sprite at (20, 20)
  spr(0, cloud_x, 20)
end
```

#### Incrementation:

To make the cloud move, we can increment the cloud_x variable within the `_update()` function. This function runs 30 times per second, so by increasing `cloud_x` by a small amount each time, the cloud will appear to move across the screen from left to right.

```lua
cloud_x = 20

function _draw()
  -- draw cloud sprite at (20, 20)
  spr(0, cloud_x, 20)
  -- increment by 0.1 each time draw loop happens
  cloud_x = cloud_x + 0.1
end
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/pBS7XyG.png){ width=100% }\
```{=latex}
\end{center}
```

The sprite appears to move, but it leaves a trail behind it. This is because the screen is not being cleared before each new frame is drawn. By cleared, we mean filling the screen with a solid color before drawing the new frame.

#### Clearing the Screen; CLS() Function:

To clear the screen, we can use the **CLS()** function at the beginning of the `_draw()` function. This function fills the screen with a solid color (default is black) before drawing anything else.

```lua
cls(0)
```

```lua
function _draw()
	-- clear the screen by drawing sa olid black color
	cls(0)
	-- draw cloud sprite at (20, 20)
	spr(0, cloud_x, 20)
	-- increment by 0.1 each time draw loop happens
	cloud_x = cloud_x + 0.1
end
```

::: box

> `cls(0)` is the equivalent of using:
> ```lua
> rectfill(0,0,127,127,0)
> ```

:::
```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/bkvaBND.png){ width=100% }\
```{=latex}
\end{center}
```

This looks like a moving cloud! I drew the cloud sprite with a blue background, though..

Instead of using the default clearing the screen with a black solid color, let's use the same blue:

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/HTZrefn.png){ width=50% }\
```{=latex}
\end{center}
```

Looking at my color palette with their assigned numbers, I know that the blue I used is assigned the value of 12.

```lua
function _draw()
	-- clear the screen by drawing a solid black color
	cls(12)
	-- draw cloud sprite at (20, 20)
	spr(0, cloud_x, 20)
	-- increment by 0.1 each time draw loop happens
	cloud_x = cloud_x + 0.1
end
```

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/axZJ7Wm.png){ width=100% }\
```{=latex}
\end{center}
```

That looks like a sky! But something happened with my black outline. This is because black is used as the default transparency color. If you really want black to be opaque, you can add this line in `_init()`:

```lua
function _init()
  palt(0, false)
end
```

Or you could use a different color. I'll just use the dark blue color instead.

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/KgEayf2.png){ width=100% }\
```{=latex}
\end{center}
```

### Wrapping Around the Screen

When the cloud completely exits the frame, we are left with just a blank blue screen. We should reset it to the left side so that it becomes visible again.

To do this, we can use an if statement. In English, if the cloud is out of frame on the right, then reset it to a position on the left side.

We can write the code in the `_update()` function.

```lua
function _update()
  if cloud_x > 127 then
    cloud_x = -8
  end
end
```

If cloud_x becomes higher than 127, it means it has completely left the frame; therefore, that is when the reset should happen.

The reset position should be a negative value that is the width of the sprite size, so -8.

### Full Minimal Program

```{.lua emphasize=2-2,3:3-3:12}
cloud_x = 20

function _update()
	-- reset cloud to the left side when out of frame
	if cloud_x > 127 then
		cloud_x = -8
	end
end

function _draw()
	-- clear the screen by drawing a solid black color
	cls(12)
	-- draw cloud sprite at (20, 20)
	spr(0, cloud_x, 20)
	-- increment by 0.1 each time the draw loop happens
	cloud_x = cloud_x + 0.1
end
```

### Adding More Clouds (Making Objects)

::: box

**TIP**

To take a screenshot of your screen, press **Ctrl + 6**.

:::

```{=latex}
\begin{center}
```
![|600](https://i.imgur.com/4neWxUc.png){ width=100% }\
```{=latex}
\end{center}
```

