import random

def guess_the_number():
    
    target_number = random.randint(1, 100)
    
    attempts = 0
    guess = None
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    
    while guess != target_number:
        
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        attempts += 1
        
        
        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
    
    
    print(f"Congratulations! You guessed the correct number in {attempts} attempts.")


guess_the_number()
