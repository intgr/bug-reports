Django query race condition repro
=================================

To hit this race reliably, I needed to modify Django and inject `time.sleep(0)`
in SQLCompiler.compile method:

```python
    def compile(self, node):
        vendor_impl = getattr(node, "as_" + self.connection.vendor, None)
        if vendor_impl:
            sql, params = vendor_impl(self, self.connection)
        else:
            sql, params = node.as_sql(self, self.connection)
        time.sleep(0)  # <--- Yield to other threads
        return sql, params
```

Install deps & run:

```shell
poetry install
poetry shell
./manage.py migrate
./manage.py repro
```

Actual code lives in
[app/management/commands/repro.py](app/management/commands/repro.py)

Successful reproduction output looks like:
```
Traceback (most recent call last):
  File ".../django/django/db/backends/utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
  File ".../django/django/db/backends/sqlite3/base.py", line 357, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.OperationalError: no such column: app_root.id

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File ".../django-query-race-condition/app/management/commands/repro.py", line 38, in main
    job.result()
  File ".../lib/python3.10/concurrent/futures/_base.py", line 451, in result
    return self.__get_result()
  File ".../lib/python3.10/concurrent/futures/_base.py", line 403, in __get_result
    raise self._exception
  File ".../lib/python3.10/concurrent/futures/thread.py", line 58, in run
    result = self.fn(*self.args, **self.kwargs)
  File ".../django-query-race-condition/app/management/commands/repro.py", line 21, in hammer
    list(query)
  File ".../django/django/db/models/query.py", line 394, in __iter__
    self._fetch_all()
  File ".../django/django/db/models/query.py", line 1866, in _fetch_all
    self._result_cache = list(self._iterable_class(self))
  File ".../django/django/db/models/query.py", line 87, in __iter__
    results = compiler.execute_sql(
  File ".../django/django/db/models/sql/compiler.py", line 1400, in execute_sql
    cursor.execute(sql, params)
  File ".../django/django/db/backends/utils.py", line 103, in execute
    return super().execute(sql, params)
  File ".../django/django/db/backends/utils.py", line 67, in execute
    return self._execute_with_wrappers(
  File ".../django/django/db/backends/utils.py", line 80, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File ".../django/django/db/backends/utils.py", line 84, in _execute
    with self.db.wrap_database_errors:
  File ".../django/django/db/utils.py", line 91, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File ".../django/django/db/backends/utils.py", line 89, in _execute
    return self.cursor.execute(sql, params)
  File ".../django/django/db/backends/sqlite3/base.py", line 357, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.OperationalError: no such column: app_root.id
```
