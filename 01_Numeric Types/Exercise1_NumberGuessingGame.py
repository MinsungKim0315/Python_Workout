# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 10:39:48 2024

@author: Minsung Kim
Exercise1_NumberGuessingGame
Problem
-Write a function (guessing_game) that takes no arguments.
-When run, the function chooses a random integer between 0 and 100 (inclusive).
-Then ask the user to guess what number has been chosen.
-Each time the user enters a guess, the program indicates one of the following:
    – Too high
    – Too low
    – Just right
-If the user guesses correctly, the program exits. Otherwise, the user is asked to
try again.
-The program only exits after the user guesses correctly.
"""
import random

def guessing_game():
    answer = random.randint(0, 101)
    while True:
        guess = int(input("Guess a number between 0 to 100: "))
        ##since input only gets String, you have to convert it to int
        if guess < answer:
            print(f"your guess of {guess} is Too low")
        if guess > answer:
            print(f"your guess of {guess} is Too high")
        if guess == answer:
            print(f"your guess of {guess} is Just right")
            break

guessing_game()
