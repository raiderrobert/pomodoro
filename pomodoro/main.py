#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import progressbar
import time

@click.command()
@click.option('--minutes', '-m', help='Number of minutes, default 25.')
@click.option('--seconds', '-s', help='Number of seconds.')
def main(minutes, seconds):
    bar = progressbar.ProgressBar(widgets=[
        progressbar.Bar(),
    ])
    
    if minutes is None:
        if seconds is None:
            minutes = 25 
        else:
            minutes = 0
    else
        minutes = int(minutes)
    
    seconds = 0 if seconds is None else int(seconds)
            
    for i in bar(range(minutes*60+seconds)):
        time.sleep(1)
        
    print("Take a 5 minutes break")

if __name__ == '__main__':
    main()
