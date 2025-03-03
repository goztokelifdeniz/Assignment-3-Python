# Number Board Game

## Introduction
This project is designed to strengthen Python programming skills by implementing a number board game. The program introduces file operations, control flow, functions, lists, and designing a relatively complex algorithm.

## Description
You are required to develop a number board game where:
- The board consists of rows and columns with randomly distributed numbers.
- The numbers are read from an input file (`input.txt`), allowing the program to handle different board sizes dynamically.
- Each cell has four neighboring cells (left, right, above, and below).
- The player selects a cell, and all adjacent cells with the same number disappear.
- If a column becomes empty, the remaining columns shift left to fill the empty space.

## Game Play
1. The game starts by reading the board configuration from `input.txt`, which should be provided as a command-line argument.
2. The initial board and score (starting at 0) are displayed.
3. The player selects a cell by entering its row and column numbers.
4. If the selected cell has at least one adjacent cell with the same number, all connected cells disappear.
5. The board updates accordingly, and the score is recalculated based on the removed cells.
6. If no valid moves remain, the game ends with a "Game Over" message.
7. If an invalid cell is selected, an error message is displayed, and the player is prompted to enter new coordinates.

## Scoring System
The score is calculated using the formula:
> `Score = c * n`

where:
- `c` is the value of the selected cell.
- `n` is the number of removed cells.

Example: If the selected cell has the value `1` and removes `13` cells, the score increases by `1 * 13 = 13`.

## Important Notes
- The program should be executed as:
  ```bash
  python3 assignment3.py input.txt
  ```
