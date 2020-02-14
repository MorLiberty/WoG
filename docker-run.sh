#!/bin/sh
sodu docker login --username mor12324 --password ml14678678
sodu docker-compose up -d; sodu docker-compose push
sodu docker logout
