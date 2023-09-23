import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    print("Lets start the Game")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input("Guess the Number : "))
        attempts += 1

        if guess < number_to_guess:
            print("Higher than!")
        elif guess > number_to_guess:
            print("Lesser than !")
        else:
            print(f"!!!! You guessed the number {number_to_guess} in {attempts} attempts.")
            break
    
    if attempts == max_attempts:
        print(f"Sorry, you've reached the maximum number of attempts. The number was {number_to_guess}.")

if __name__ == "__main__":
    guess_number()
