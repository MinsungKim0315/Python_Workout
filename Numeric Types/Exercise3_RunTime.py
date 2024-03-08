# -*- coding: utf-8 -*-
"""
Created on Fri Mar  8 09:26:23 2024

@author: minsung.kim
"""

def run_timing():
    i = 0
    time = 0
    total_time = 0
    while True:
        time = input("Enter 10 km run time: ")
        if not time:
             break
        i += 1
        total_time += float(time)
        
    average = total_time / i
    print(f'Average of {average}, over {i} runs')

run_timing()