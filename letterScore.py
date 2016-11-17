#   letterScore(letter, scorelist) takes as input a single letter string called letter and a list where each element
#   in that list is itself a list of the form [character, value] where character is a single letter
#   string and value is a number associated with that letter (e.g. it's scrabble score).
#   The DletterScore function then returns a single number, namely the value associated with the given letter.
#   For example, you can cut and paste the following scrabble score list into your recursion.py file.
#   This function is allowed to crash badly if the letter is not in the scorelist.

scrabbleScores = [ ["a", 1], ["b", 3], ["c", 3], ["d", 2], ["e", 1],
                 ["f", 4], ["g", 2], ["h", 4], ["i", 1], ["j", 8],
                 ["k", 5], ["l", 1], ["m", 3], ["n", 1], ["o", 1], ["p", 3],
                 ["q", 10], ["r", 1], ["s", 1], ["t", 1], ["u", 1], ["v", 4],
                 ["w", 4], ["x", 8], ["y", 4], ["z", 10] ]


def letterScore(letter, scorelist):
    for i in range(len(scorelist)):
        if letter == scorelist[i][0]:
            return scorelist[i][1]


print letterScore("c", scrabbleScores)