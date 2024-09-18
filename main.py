#! /usr/bin/env python3

# Proof of concept for
# https://www.reddit.com/r/Bossfight/comments/1fiy1pt/comment/lnmh1ka/?context=3

# Run this program once without corruption,
# save the image, then once with corruption,
# and compare the outputs.
corruption = True

# Height and width of the image
imax = 100
jmax = 100

# Color of the background (here, uniform red)
bg_color = (1, 0, 0)
# Color of the foreground (here, uniform grey)
fg_color = (0.5, 0.5, 0.5)

# Implementation detail for the PPM format
channel_max = 7

# Input: float between 0 and 1
# Output: int between 0 and channel_max
def scale1(v):
    return int(v * channel_max)

# Input: RGB color tuple between 0 and 1
# Output: RGB color tuple scaled up to channel_max
def scale3(tup):
    r, g, b = tup
    return (scale1(r), scale1(g), scale1(b))

# Draws the shape of the image.
# Here we choose a uniform background of color bg_color,
# on which is a circle filled with fg_color.
def shade(i, j):
    offcenter = ((i - imax/2)**2 + (j - jmax/2)**2)**0.5
    if offcenter < imax / 4:
        return scale3(fg_color)
    else:
        return scale3(bg_color)


# Generate image.
# For simplicity we are using the PPM format
# which has a header and is then just a grid of space-separated
# R G B values.
print("P3")
print(f"{imax} {jmax}")
print(f"{channel_max}")
for i in range(imax):
    for j in range(jmax):
        r, g, b = shade(i, j)
        print(f"{r} {g} {b} ", end="")
    # Corruption comes in the form of an additive offset
    # of a third of a pixel.
    # This is a very simplistic model, and a more advanced
    # kind of pattern could be implemented.
    if corruption:
        print("0")
    else:
        print()

