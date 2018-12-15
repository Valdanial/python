from datetime import timedelta

def add_gigasecond(moment):
    return add_seconds(moment, 1000000000)

def add_seconds(moment, seconds):
    return moment + timedelta(0, seconds)
