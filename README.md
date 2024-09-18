# The Grey Cat, The Uncorruptible.

This is a proof of concept for
[this post](https://www.reddit.com/r/Bossfight/comments/1fiy1pt/the_grey_cat_the_uncorruptible/)
(original source unknown) which I found interesting
enough to develop a minimal implementation.

# Theory

I do not claim to know how the image was generated.
I am however able to propose a proof of concept of how it could
have been implemented by showing a simple image transformation
that produces a similar result.

## Description

The image shows a grey cat on a background of horizontal lines
of irregular color. It is claimed that the file was obtained by
corrupting a normal picture.

<img src="the-uncorruptible.png" alt="The Uncorruptible" width="300"/>

The cat exhibits minimal signs of being corrupted by whatever
image transformation has made the background unintelligible.
Paying more attention however reveals that
- the cat _does_ have its color corrupted, it's just not very visible
  (see: evidence 1)
- the cat is inexplicably tilted to the right (see: evidence 2),
- a line is visible on the left (see: evidence 3).

# Practice

## Requirements

- a (recent) version of Python 3
- a way to visualize images in the [PPM](https://en.wikipedia.org/wiki/Netpbm) format.
    To this end I can suggest
    - `imagemagick` (offline image conversion), or
    - [`better-pbm-viewer`](https://perso.crans.org/vanille/better-pbm-viewer/) (online PPM visualization)

## Usage

The source code is `main.py`.

With the variable `corruption = False`, execute `python3 main.py > without.ppm`.
The image looks like this:

<img src="without.png" alt="Uncorrupted" width="300"/>

Then set `corruption = True` and execute again, this time saving the image to `with.ppm`.
The image is now like this:

<img src="with.png" alt="Corrupted" width="300"/>

Alternatively the bash script `run.sh` will do both of these for you.

# Evidence

### 1. Chromatic abberration on the cat

<img src="evidence/chromatic-abberration.png" height="300"/>
<img src="repro/chromatic-abberration.png" height="300"/>

The cat is not fully unaffected, it does show some signs of
its color being altered. This is because it is not perfectly grey
but a grey with a very light color. Though indistinguishable from
true grey when on its own, it is visibly colored when contrasted
with a different shade of itself.

### 2. Tilt

<img src="evidence/tilt.png" height="300"/>
<img src="repro/tilt.png" height="300"/>

The cat is not upright.
The direction in which it leans suggests that the reconstitution
is not perfect, and the means of corruption is probably deleting
pixels instead of adding them.

### 3. Vertical artifact

<img src="evidence/line.png" height="300"/>
<img src="repro/line.png" height="300"/>

A vertical-ish line is visible on the left.
Its offset seems to match the tilt of the cat.

The line does not seem to be material, it appears as the contrast
created by the sudden change of color.
Its irregularity in the cat version suggests that the corruption
is much less homogeneous as in the proof of concept.


