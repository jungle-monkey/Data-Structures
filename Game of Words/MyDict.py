import random
def readFile(word_bank):
        fileObj = open(word_bank, "r")
        words = fileObj.read().splitlines()
        fileObj.close()
        return words


def picking_a_word(listi):
    return random.choice(listi) 

if __name__ == "__main__":
    word_list = readFile("word_bank.txt")
    print(word_list)
