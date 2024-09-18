#! /usr/bin/env bash

THE_UNCORRUPTIBLE= python3 main.py > without.ppm
THE_UNCORRUPTIBLE=1 python3 main.py > with.ppm

magick without.ppm without.png
magick with.ppm with.png

