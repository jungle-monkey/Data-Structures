from MyDict import picking_a_word, readFile

# This function checks that the word is 5 letters long and that it only contains alphabetic characters
def input_length_checker(master_word, user_word):
    if len(master_word) == len(user_word) and user_word.isalpha():
        return True
    else:
        return False


#This function checks the user_word guess against the selected right word and returns which characters are correct (C)
def response_checker(master_word, user_word):
    resp = ""
    if input_length_checker(master_word, user_word): # first, we check that the length of the input is a 5 letter word
        for i in range(len(master_word)): 
            if master_word[i] == user_word[i]: 
                resp += "C "
            elif user_word[i] in master_word: # same letter at a different index
                resp += "c "
            else:
                resp += "- "
        return resp.strip()
    else:
        print("Please, the word to guess should be 5 letters long. Try a new guess!")
        return None

#This function prints the users guess and the returned correct/incorrect characters
def printing_func(guesses_dictionary):
    if len(guesses_dictionary) != 0:
        for key in guesses_dictionary:
            print("Your guess: " + key + "    " + "Correct word: " + guesses_dictionary[key])


def main_game_loop(master_word, max_guesses):
    user_input_counter = 0
    guesses_dictionary = {}
    while user_input_counter < max_guesses:
            user_word = input("Please, enter your guess of the 5 letter word in English: ").casefold()
            responz = response_checker(master_word, user_word)
            if responz == None: # if the user_word is longer or shorter than 5 letters long, it will jump onto the next iteration
                continue
            guesses_dictionary[user_word] = responz
            if user_word == master_word:
                print("Well done! You guessed the word! You won this round!")
                return True
            printing_func(guesses_dictionary)
            user_input_counter +=1
    else:
        print("You lost. You could not beat the master. Try another round!")
        return False

#This function returns the new calculated scores after each game
def games_score_history(player_games_score, computer_games_score, last_game_result):
    if last_game_result == True:
        player_games_score +=1
    else:
        computer_games_score +=1
    return player_games_score, computer_games_score

# This function asks the user how many attempts he wants to have for the guessing
def get_max_guesses_number():
    max_guesses = 0
    max_guesses_input = input("Please, enter the maximum number of guesses (default 5): ")
    if max_guesses_input == "":
        max_guesses = 5
    else:
        try:
            max_guesses = int(max_guesses_input)
        except:
            print("Invalid input, maximum number of guesses set to 5")
            max_guesses = 5
    return max_guesses


if __name__ == "__main__":

    player_games_score = 0
    computer_games_score = 0

    while True:
        print("Welcome to the exciting world of Wordle!")
        max_guesses = get_max_guesses_number()
        word_bank = readFile("word_bank.txt")
        master_wrd = picking_a_word(word_bank).casefold()

        did_player_win_flag = main_game_loop(master_wrd, max_guesses)
        player_games_score, computer_games_score = games_score_history(player_games_score, computer_games_score, did_player_win_flag) # overwrites

        print("The games score history is: number of games you won = {}, number of games you lost = {}".format(player_games_score, computer_games_score))
        interrupt_game = input("Do you want to play again? Enter '(y)es' or '(n)o'. ")
        if interrupt_game != "y" and interrupt_game != "yes":
            break

    

