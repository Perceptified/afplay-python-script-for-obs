#!/usr/bin/python3
#
# Script which uses afplay to play audio files, also writes the track title and artist name out
# to a text file which then can be used in OBS to display that information on stream.
# Copyright(left) : Markus Aigner 2023 (perceptified@gmail.com)
# 

import sys

directory=sys.argv[0]
numberOfArguments=len(sys.argv)

if(sys.argv[1]==""):
    volume=0.1
else:
    volume=sys.argv[1]

# Start at 1 so the command name itself is not used alongside
for i in range(1, numberOfArguments):
    print(sys.argv[i], end = " ")

