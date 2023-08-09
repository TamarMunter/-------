import csv
from scipy import stats
import numpy as np

# Initialize lists
last_moves_list = []
len_of_game_list = []
data_list = []

# Read data from CSV file
with open('input.csv', 'r') as myFile:
    myReader = csv.reader(myFile)
    data_list = list(myReader)

# Process data
for data in data_list:
    last_move = data
    len_of_game = len(data) - 1
    len_of_game_list.append(len_of_game)
    last_move = last_move[-1]
    last_moves_list.append(last_move)

# Calculate mean of move lengths
mean_of_moves = np.mean(len_of_game_list)

# Calculate mode of last moves
x = stats.mode(last_moves_list, axis=None)
most_common_last_move = int(x.mode[0])

# Define a dictionary to translate values to their corresponding meanings
prophet_dict = {
    'Thumb': 5,
    'Index Finger': 4,
    'Middle Finger': 3,
    'Ring Finger': 2
}

# Find the meaning of the most common last move
most_common_last_move_meaning = None
for key, value in prophet_dict.items():
    if value == most_common_last_move:
        most_common_last_move_meaning = key
        break

# Print results
print("List of last moves:", last_moves_list)
print("Number of moves in each game:", len_of_game_list)
print("Mean number of moves per game:", mean_of_moves)
print("Most common last move:", most_common_last_move_meaning)
