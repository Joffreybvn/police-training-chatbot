#!/bin/sh

echo "Start script initialized"

cd /bot || exit
rasa run --model models --enable-api --cors "*" --debug -p $PORT