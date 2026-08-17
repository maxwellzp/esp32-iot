#!/usr/bin/env bash

set -e

DEVICE="/dev/ttyUSB0"

echo "Uploading project to $DEVICE..."

mpremote connect "$DEVICE" cp main.py :main.py
mpremote connect "$DEVICE" cp config.py :config.py

mpremote connect "$DEVICE" mkdir :sensors 2>/dev/null || true

mpremote connect "$DEVICE" cp sensors/__init__.py :sensors/__init__.py
mpremote connect "$DEVICE" cp sensors/dht22.py :sensors/dht22.py

mpremote connect "$DEVICE" cp config_private.py :config_private.py

mpremote connect "$DEVICE" mkdir :connectivity 2>/dev/null || true
mpremote connect "$DEVICE" cp connectivity/__init__.py :connectivity/__init__.py
mpremote connect "$DEVICE" cp connectivity/wifi.py :connectivity/wifi.py

mpremote connect "$DEVICE" mkdir :api 2>/dev/null || true
mpremote connect "$DEVICE" cp api/__init__.py :api/__init__.py
mpremote connect "$DEVICE" cp api/server.py :api/server.py

echo "Project uploaded successfully."
