Docker build disk space leak
============================

Bug reported at https://github.com/moby/moby/issues/46136

When running multiple `docker build` commands in parallel, Docker loses track of some directories and files it creates
under the `/var/lib/docker/overlay2` directory.
However, this issue does not occur when the "build" commands are run in sequence (e.g. remove the `&` in `repro.sh`).

After the build, despite running `docker system prune -af --volumes` to delete all build cache/artifacts and using
`docker system df` to verify that there should be no disk space in use, the size of Docker's `overlay2` directory grows
every time with no limit.

How to reproduce
----------------

Run the `./repro.sh` shell script multiple times and notice `overlay2` directory increasing in size.

The script needs to run `docker` commands and uses `sudo` to monitor the size of the `overlay2` directory.

It can be tested in the public playground https://labs.play-with-docker.com/ for example.

```shell
git clone https://github.com/intgr/bug-reports
cd bug-reports/docker-build-disk-space-leak
./repro.sh
```

Output
------

Notice that the ACTUAL number of items and disk space keeps growing every time when running `./repro.sh`, despite
Docker reporting 0 bytes used.

```
$ docker --version
Docker version 24.0.2, build cb74dfc
$ ./repro.sh
BUILDING...
build done!

pruned everything. Docker THINKS this much disk space is in use:
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          0         0         0B        0B
Containers      0         0         0B        0B
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B

ACTUAL disk space used: 7.4M	/var/lib/docker/overlay2            <-- !!!
ACTUAL number of items in /var/lib/docker/overlay2: 12              <-- !!!

$ ./repro.sh
BUILDING...
build done!

pruned everything. Docker THINKS this much disk space is in use:
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          0         0         0B        0B
Containers      0         0         0B        0B
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B

ACTUAL disk space used: 7.5M	/var/lib/docker/overlay2            <-- !!!
ACTUAL number of items in /var/lib/docker/overlay2: 21              <-- !!!

$ ./repro.sh
BUILDING...
build done!

pruned everything. Docker THINKS this much disk space is in use:
TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          0         0         0B        0B
Containers      0         0         0B        0B
Local Volumes   0         0         0B        0B
Build Cache     0         0         0B        0B

ACTUAL disk space used: 7.6M	/var/lib/docker/overlay2            <-- !!!
ACTUAL number of items in /var/lib/docker/overlay2: 30              <-- !!!
```
