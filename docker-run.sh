#!/bin/sh
sudo docker login --username mor12324 --password ml14678678
sudo docker-compose up -d; sudo docker-compose push
sudo docker logout
