# This repository contains python projects.

Project 1 - Hangman Game

Objective of this project is to implement Hangman game with python. This is project uses concepts of strings, loops. 
Hangman is a random word guessing game. Interpreter will choose randomly from a list of words provided in the program. User first has to input thier name and start the game. User will be asked to guess a letter, and if it matches any letter in the word selected it will be shown as output and the game moves forward else the program will ask user to guess another letter. This continues till correct word is guessed or maximum number of chances - 16 is reached.


Project 2 - Calculating Performance Metrics without SKlearn, only using Numpy and Pandas

Performance metrics (Confusion Matrix, F1 score, AUC score, Accuracy Score, Mean Square Error, MAPE, R^2 Errors) are being calculated using 4 different types of sample datasets to understand the outcome depending on dataset
Class labels are derived from given score as y_pred = 0 if y_score <0.5 else 1

A - This dataset is highly imbalanced dataset with positive points>>negative points

B - This dataset is highly imbalanced dataset with negative points>>positive points

C - Computing the best threshold (similarly to ROC curve computation) of probability which gives lowest values of metric 'A' for the given data C
A=500×number of false negative+100×numebr of false positive
This data has number of negative points > number of positive points

D - Sample for performance metrics (for regression ) where two columns Y and Predicted_Y are given which are real valued features.

