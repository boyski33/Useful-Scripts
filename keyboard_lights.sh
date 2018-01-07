#!/bin/bash
# This script is used to press 'Scroll Lock' on my Cooler Master keyboard
# which is the hotkey to turn on the keyboard backlights.

flag=$(xset -q | awk ' /Scroll Lock/{ print $12 }')

if [[ "$flag" == 'on' ]]; then
	xset led off
else
	xset led on
fi
