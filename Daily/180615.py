

from raven import Client

client = Client('___DSN___')

try:
    1 / 0
except ZeroDivisionError:
    client.captureException()
