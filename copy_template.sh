#!/bin/bash

year=$1
day=$2

touch "aoc_$year/input/day$day.txt"
sed "s/dayXX/day$day/" template.py >"aoc_$year/day$day.py"
