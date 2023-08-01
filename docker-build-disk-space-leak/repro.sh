#!/bin/sh

set -e

OVERLAY_DIR=/var/lib/docker/overlay2

echo "BUILDING..."

uuidgen > lockfile.txt
docker build -t repro1:latest --target=target1 . &>/dev/null &
docker build -t repro2:latest --target=target2 . &>/dev/null &
docker build -t repro3:latest --target=target3 . &>/dev/null &
docker build -t repro4:latest --target=target4 . &>/dev/null &
wait
echo "build done!"

docker system prune -af --volumes >/dev/null
echo
echo "pruned everything. Docker THINKS this much disk space is in use:"
docker system df
echo
echo -n "ACTUAL disk space used: "
sudo du -hd0 "$OVERLAY_DIR"

echo -n "ACTUAL number of items in $OVERLAY_DIR: "
sudo ls "$OVERLAY_DIR" |wc -l

echo
