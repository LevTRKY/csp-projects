import random # Imports the random module

def check_guess(guess, target): # This function checks if the guess is too high, too low
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

def number_guessing_game(): # This function is the main function that runs the game
    target = random.randint(1,100)  # It picks a random number between 1 and 100
    guesses = []
    
    while True:
        guess = int(input("Enter your guess: ")) # Asks the user to enter a guess
        guesses.append(guess)
        result = check_guess(guess, target)
        print(result)
        if result == "Correct!": # Once the user gets the correct number it ends the loop
            break
    
    print(f"You guessed the number in {len(guesses)} tries.") # Gives them how many tries it took to guess
    print("Your guesses were:", guesses) # Shows all the guesses that were made

if __name__ == "__main__":
    number_guessing_game()
