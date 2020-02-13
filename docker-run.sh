
#!/bin/sh
docker login --username mor12324 --password ml14678678
docker-compose up -d; docker-compose push
docker logout
