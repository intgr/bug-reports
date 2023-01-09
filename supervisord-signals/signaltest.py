#!/usr/bin/env python
from signal import signal, SIGQUIT, SIGTERM
from time import sleep


def got_sigterm(*args):
    print("Received SIGTERM")
    exit(0)

def got_sigquit(*args):
    print("Received SIGQUIT")
    exit(0)


signal(SIGQUIT, got_sigquit)
signal(SIGTERM, got_sigterm)

sleep(100)
