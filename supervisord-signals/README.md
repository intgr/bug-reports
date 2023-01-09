Repro
-----

Command:
```shell
supervisord -c ./supervisord.conf & PID=$!; sleep 2 && kill -TERM $PID
```
