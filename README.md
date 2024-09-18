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

![](without.png "Uncorrupted")

Then set `corruption = True` and execute again, this time saving the image to `with.ppm`.
The image is now like this:

![](with.png "Corrupted")


