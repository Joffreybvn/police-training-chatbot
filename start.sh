#!/bin/sh

echo "Start script initialized"

rasa run --model models --enable-api --cors "*" --debug -p $PORT