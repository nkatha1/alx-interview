#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))  # Expected Output: "Ben"
print("Winner: {}".format(isWinner(3, [4, 5, 1])))        # Expected Output: "Ben"
print("Winner: {}".format(isWinner(0, [])))               # Expected Output: None
print("Winner: {}".format(isWinner(1, [1])))              # Expected Output: "Ben"
print("Winner: {}".format(isWinner(2, [3, 7])))           # Expected Output: "Maria"

