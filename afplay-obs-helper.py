#!/usr/bin/python3
#
# Script which uses afplay to play audio files, also writes the track title and artist name out
# to a text file which then can be used in OBS to display that information on stream.
# Copyright(left) : Markus Aigner 2023 (perceptified@gmail.com)
# 

import sys
import os
import random

"""
afplay-obs-helper.py

this program takes a directory as input, walks that directory, either selects a file at random (see options for details)
or from top to bottom, writes the track name and title out to a text file which is currently intended to be read
by OBS (open broadcaster software) to be then displayed in the live stream feed.

Usage:
afplay-obs-helper.py -[hVvr] <DIRECTORY>

Options:
-h --help: Display help text and exit.
-V --version: Display version information and exit.
-v --volume: play at volume (passed on to afplay, any volume over 1 will be blocked by this program for the sake of the user's ears.)
-r --random: the audio files in the directory will be played in a random order.

"""

directory=sys.argv[1]
numberOfArguments=len(sys.argv)
volume = 0.2
tracks = []

def getDirectoryContent(directory):
    # print(directory)
    files = []
    for candidate in os.listdir(directory):
        if not candidate.startswith(".") and not candidate == "Thumbs.db" and not os.path.isdir(os.path.join(directory, candidate)) == True:
            files.append(candidate)
    return files

def shuffleTracks(tracks):
    indices = [x for x in range(len(tracks))]
    i = random.choice(indices)
    j = random.choice(indices)
    tracks[i], tracks[j] = tracks[j], tracks[i]
    return tracks

tracks = getDirectoryContent(directory)
if sys.argv.__contains__("-r") or sys.argv.__contains__("--random"):
    tracks = shuffleTracks(tracks)
for i in tracks:
    print(i)