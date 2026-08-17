#!/usr/bin/env bash

DEVICE="/dev/ttyUSB0"

mpremote connect "$DEVICE" reset
mpremote connect "$DEVICE" repl
