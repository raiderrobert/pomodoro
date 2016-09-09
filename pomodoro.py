#!/usr/bin/env python 
import click
import progressbar
import time

@click.command()
@click.option('--minutes', default=25, help='Number of minutes, default 25.')
def pomodoro(minutes):
    bar = progressbar.ProgressBar(widgets=[
    progressbar.Bar(),
])
    for i in bar(range(minutes*60)):
        time.sleep(1)

if __name__ == '__main__':
    pomodoro()
