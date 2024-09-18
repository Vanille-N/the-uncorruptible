#! /usr/bin/env bash

THE_UNCORRUPTIBLE= python3 main.py > img/without.ppm
THE_UNCORRUPTIBLE=1 python3 main.py > img/with.ppm

magick img/without.ppm img/without.png
magick img/with.ppm img/with.png

