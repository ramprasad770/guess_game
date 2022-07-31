import random
from sympy import *
def play():
    guess=random.randint(1,100)
    clues=[]
    clues.append(isprime(guess))
    clues.append(guess%5==0)
    clues.append(guess%2==0)
    
    for i in range(10):
        a=int(input("Enter a guess(1-100):"))
        if guess==a:
            print("correct guess.")
            return i
        elif i<3:
            if i==0:
                if clues[0]==True:
                    temp="Guess is a prime"
                else:
                    temp="Guess is not a prime."
            if i==1:
                if clues[1]==True:
                    temp="Guess is a multiple of 5."
                else:
                    temp="Guess is not a multiple of 5."
            if i==2:
                if clues[2]==True:
                    temp="Guess is a even number."
                else:
                    temp="Guess is a odd number."
            print("Wrong guess")
            print("Hint :"+temp)
        else:
            temp="Your guess is higher then actual."
            if guess>a:
                temp="Your guess is lesser than actual."
            print("Wrong guess")
            print("Hint :"+temp)
    return i


def check(p1,p2):
    res="This is a tie match."
    if p1>p2:
        res="Player2 won the game."
    if p2>p1:
        res="Player1 won the game."
    return res
print("""
      ***** WELCOME TO GUESSING GAME *****
      """)
print("""
      ************** RULES ***************
      """)
print("""
      1.IT's a 2 players game.
      2.Starting with player1.
      3.Each player have 10 chances to guess a 
      number between (1-100 inclusive). Using 
      guesses given at every wrong guess.
      """)
print("""
      4.If player1 guessed correct,then count
      of guess are considerd and player2 can
      start the game.
      """)
print("""
      5.At the end of the game by comparing 
      who guessed the correct number at less
      guesses declare as won the game.
      """)
print("""
      6.If both take same count of guesses
      then it's a tie game.
      """)
game=str(input("Enter s to start,q to quit game:"))

if game=="q":
    print("Game is ended,see u again")
if game=="s":
    print("Game is started for player1:")
    p1=play()
    print("Player1 game is finished.")
    print()
    print()
    print("Game is started for player2:")
    p2=play()
    print()
    print(check(p1,p2))
    