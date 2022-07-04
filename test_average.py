# This program gets three test scores and displays
2 # their average. It congratulates the user if the
3 # average is a high score.
4
5 # The HIGH_SCORE named constant holds the value that is
6 # considered a high score.
HIGH_SCORE = 95
8
9 # Get the three test scores.

test1 = int(input('Enter the score for test 1: ' ))
test2 = int(input('Enter the score for test 2: ' ))
test3 = int(input('Enter the score for test 3: ' ))

# Calculate the average test score.
average = (test1 + test2 + test3) / 3

# Print the average.
print(f'The average score is {average}.')

# If the average is a high score,
# congratulate the user.
if average >= HIGH_SCORE:
    print('Congratulations!')
    print('That is a great average!')