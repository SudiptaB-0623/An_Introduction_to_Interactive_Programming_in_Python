# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

# write import statements
import math
import random
import simplegui

# define global variables
num_r = 100
remaining_guesses = 0
secret_no = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global num_r, remaining_guesses, secret_no
    remaining_guesses = int(math.ceil(math.log((num_r - 0), 2)))
    secret_no = random.randrange(0, num_r)
    print "\nNew game. Range is from 0 to", num_r
    print "Number of remaining guesses is", remaining_guesses

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_r
    num_r = 100
    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_r
    num_r = 1000
    new_game()
    
def input_guess(guess):
    global remaining_guesses
    print "\nGuess was", guess
    guess = int(guess)
    remaining_guesses -= 1
    print "Number of remaining guesses is", remaining_guesses
    # main game logic goes here
    if remaining_guesses > 0:
        if guess > secret_no:
            print "Lower"
        elif guess < secret_no:
            print "Higher"
        else:
            print "Correct"
            new_game()
    else:
        if guess == secret_no:
            print "Correct"
        else:
            print "You ran out of guesses. The number was", secret_no
        new_game()
    
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess:", input_guess, 200)

# call new_game 
new_game()
