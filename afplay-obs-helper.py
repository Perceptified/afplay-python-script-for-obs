#!/usr/bin/python3
#
# Script which uses afplay to play audio files, also writes the track title and artist name out
# to a text file which then can be used in OBS to display that information on stream.
# Copyright(left) : Markus Aigner 2023 (perceptified@gmail.com)
# 

import sys
import os
import subprocess
import random
import re

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
    # print(files)
    return files

def shuffleTracks(tracks):
    indices = [x for x in range(len(tracks))]
    i = random.choice(indices)
    j = random.choice(indices)
    for index in range(len(tracks)):
        tracks[i], tracks[j] = tracks[j], tracks[i]
    return tracks

def getShuffleSwitch(arguments):
    try:
        arguments.index("-r") or arguments.index("--random")
        shuffleSwitch = True
        # print(shuffleSwitch)
        return shuffleSwitch
    except ValueError:
        shuffleSwitch = False
        # print(shuffleSwitch)
        return shuffleSwitch
    
tracks = getDirectoryContent(directory)

if getShuffleSwitch(sys.argv) == True:
    tracks = shuffleTracks(tracks)
else:
    tracks = sorted(tracks)
for i in tracks:
    print(i)

# def escapeSpacesInTrackNames(tracks):
#    for index in range(len(tracks)):
#        tracks[index] = @str(tracks[index])
#    return tracks

# tracks = escapeSpacesInTrackNames(tracks)

trackPath = os.path.join(directory, tracks[0])
# trackpath = os.path.abspath(trackPath)
print(trackPath)
subprocess.run("afplay", "-v", str(volume), "\"" + trackPath + "\"")
# subprocess.run("afplay" + " -v " + str(volume))
# subprocess.run("/usr/bin/afplay" + " -v " + str(volume) + " " +  "\"" + trackPath + "\"")
# userInput = input("Type: Exit (to stop) Next (to jump to next track)")

# while userInput!="Exit" or userInput!="exit":
    # for track in tracks:
        # trackPath = os.path.join(directory, track)
        # track = track.translate(str.maketrans({' ' : '\ '}))
        # print(track)
        # track = os.path.normpath(directory + track)
        # print(track)
        # track = track.replace(r' ', '\ ')
        # track = re.sub(" ", r'\ ', track)
        # subprocess.run("afplay" + " -v " + str(volume) + " " + trackPath)