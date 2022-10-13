from threading import current_thread
from concurrent.futures import ThreadPoolExecutor, as_completed
from traceback import print_exception

from app.models import Root
from django.core.management import BaseCommand

# Global QuerySet shared by all threads
query = Root.objects.select_related().all()
THREADS = 8


def hammer():
    global query

    cached = 0
    uncached = 0
    name = current_thread().name
    print(f"Hammer {name} started")

    for i in range(1000):
        list(query)
        if query._result_cache is not None:
            # Reset query cache
            query = query.all()
            cached += 1
        else:
            uncached += 1
    print(f"Hammer {name} finished (cached: {cached} uncached: {uncached})")


def main():

    with ThreadPoolExecutor(max_workers=THREADS) as pool:
        jobs = [pool.submit(hammer) for _ in range(THREADS)]

        for job in as_completed(jobs):
            err = job.exception()
            if err:
                print_exception(err)


class Command(BaseCommand):
    def handle(self, *args, **options):
        main()
