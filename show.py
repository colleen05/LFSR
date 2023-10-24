#! /bin/python3

# File: show.py
# Project: LFSR
# Description: Python script for visualisation and analysis of LFSR
#     pseudorandomness.
# License: MIT License
# Author: Colleen ("colleen05")

# NOTE: There is a section at the bottom of this file which you may edit to
# moidfy the behaviour of this program.

import matplotlib.pyplot as plt

from PIL import Image

iseed = 0
nums = []
period = 0

# Attempt to find period.
def find_period(seq):
    i = 1
    while (seq[i] != seq[0]) and (i < 65536):
        i += 1
        if i == 65536:
            return 65536
    
    return i

# Change nums to contain the difference from last element
def make_diff():
    global nums

    diffs = [0] * 65537

    i = 1
    while i < 65536:
        diffs[i] = abs(nums[i] - nums[i-1])
        i += 1

    nums = diffs

# Change nums where Y = count_of X in nums
def make_dist():
    global nums

    dist = [0] * 65536

    i = 0
    while i < 65536:
        dist[nums[i]] += 1
        i += 1

    nums = dist

# Show pyploy window
def show_plot():
    plt.plot(nums, 'o')
    plt.xlabel("Seed")
    plt.ylabel("RNG(Seed)")
    plt.gcf().text(0.02, 0.92, "Seed = " + str(iseed) + "\nPeriod = " + str(period), fontsize=12)
    plt.show()

# Open RNG LSV file, setting up global variables
def open_rng_lsv(fname):
    global iseed, nums

    with open(fname) as f:
        lines = f.read().splitlines()

        for l in lines:
            nums.append(int(l))
    
        iseed = nums[0]
        del nums[0]

# Export PNG image of the distribution
def make_image(fname):
    im = Image.new(mode="RGB", size=(256,256))

    for x in range(256):
        for y in range(256):
            v = nums[y * 256 + x]
        
            r = (v & 0xFF00) >> 8       # For MSB
            g = (v & 0x00FF)            # For LSB
            b = int(v / 65536 * 256)

            r = b
            g = b

            im.putpixel((x, y), (r, g, b))

    im.save(fname)

##############################################################################
#{========== EDIT THIS PART TO MODIFY THE BEHAVIOUR OF THE SCRIPT ==========}#
##############################################################################

open_rng_lsv("rng.lsv")
make_image("dist.png")
period = find_period(nums)
# make_diff()
# make_8bit()
# make_dist()
show_plot()
