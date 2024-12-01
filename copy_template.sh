#!/bin/bash

year=$1
day=$2

touch "$year/aoc_$year/input/day$day.txt"
sed "s/dayXX/day$day/" template.py >"$year/aoc_$year/day$day.py"
