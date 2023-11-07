import random

class HangmanGame:
    def __init__(self, max_nr_guesses=6):
        self.the_chosen_word = self.word_selector()
        self.guess_status = "-" * len(self.the_chosen_word)
        self.user_nr_guesses = 0
        self.max_nr_guesses = max_nr_guesses

        # print("Welcome to the Hangman game. Try to guess the word that the computer chose. You have 6 attempts. You can either guess single letters or the whole word. Are you ready?")

    def word_selector(self):
        with open("word_bank.txt", "r", encoding="utf-8") as word_bank:
            temp = word_bank.readlines()
            the_chosen = random.choice(temp).strip()
            return the_chosen

    def guess(self, user_input):
        # checking one letter guess
        if len(user_input) == 1: 
            for i in range(len(self.the_chosen_word)):
                if user_input == self.the_chosen_word[i]:
                    self.update_guess_status(i, user_input)
           # user guessed the last letter in less than 6 attempts  
           if self.guess_status == self.the_chosen_word: 
                return True
        # checking the whole word guess
        if len(user_input) == len(self.the_chosen_word): 
            if user_input == self.the_chosen_word:
                # print("Nice job! You guessed the word. " + f"The word: {self.the_chosen_word}")
                return True # break out of this loop/function
        self.user_nr_guesses += 1
        return False # run the game command again

    def user_input_checker(self, user_input):
        # checking that the user input is valid (no numbers, 1 letter, the whole word length...)
        if user_input.isalpha():
            # checking that the guess is either a letter or up to the same length as the word
            if user_input in self.the_chosen_word:
                return True
        else:
            return False

    def update_guess_status(self, letter_index, letter):
        # updating the status with the letter from the user_input
        self.guess_status = self.guess_status[:letter_index] + letter + self.guess_status[letter_index+1:]

    def guess_status_formatting(self):
        return_str = ""
        for letter in self.guess_status:
            return_str += letter + " "
        return return_str.strip()


def main():
    # Hook spot for the console script.
    user_nr_win_games = 0
    user_nr_lost_games = 0
    while True:
        # print("Welcome to the Hangman game. Try to guess the word that the computer chose. You have 6 attempts. You can either guess single letters or the whole word. Are you ready?")
        user_choice = input("Select (n) for new game or (q) to quit: ").casefold()
        if user_choice  == "q":
            break
        if user_choice != "n":
            print("Invalid input.")
            continue
        print("Welcome to the Hangman game. Try to guess the word that the computer chose. You have several attempts. You can either guess single letters or the whole word. Are you ready?")
        max_nr_guesses = input("Please enter the number of attempts you want to have for the game (by default it is 6): ") # watch out for invalid input
        if max_nr_guesses.isnumeric() != True:
            print("Invalid input. Please, enter a number!")
            continue
        max_nr_guesses = int(max_nr_guesses)   
        game = HangmanGame(max_nr_guesses)
        while True:
            print("The word: " + game.guess_status_formatting()) # the product of individual guess
            print("Your remaining attempts: " + str(game.max_nr_guesses - game.user_nr_guesses))
            user_guess = input("Enter your guess: ").casefold()
            if game.user_input_checker(user_guess) == False:
                print("Please, enter a valid input: a letter or a word")
                continue
            if game.guess(user_guess) == True:
                print("Nice job! You guessed the word. " + f"The word: {game.the_chosen_word}")
                user_nr_win_games += 1
                break
            if game.user_nr_guesses >= game.max_nr_guesses:
                print("Sorry. You got hanged! |---o/-< ")
                user_nr_lost_games += 1
                break
        print(f"Number of games won: {user_nr_win_games}" + "\n" + f"Number of games lost: {user_nr_lost_games}")

if __name__ == "__main__":
    main()

