import random
# Write your code here
word = ""
hidden = ""


def main():

    languages = ('python', 'java', 'kotlin', 'javascript')

    print("H A N G M A N")
    while True:

        print('Type "play" to play the game, "exit" to quit: ', end="")
        answer = input()
        if answer != "play":
            break
        print()

        global word
        global hidden

        word = random.choice(languages)
        latter_set = set(word)
        former_set = set()
        hidden = "-" * len(word)
        #  locations = [i for i in range(len(answer)) if answer.startswith(guess, i)]
        i = 8
        while i > 0:

            print(hidden)
            if '-' not in hidden:

                print(f"You guessed the word {word}!")
                print("You survived!")
                break

            print("Input a letter: ", end="")

            letter = input()

            if letter in former_set:

                print("You already typed this letter")

            elif letter in latter_set:

                latter_set.discard(letter)
                former_set.add(letter)
                hidden = open_letter(letter)

            elif len(letter) is not 1:

                print("You should input a single letter")

            elif not letter.islower():

                print("It is not an ASCII lowercase letter")

            else:

                i -= 1
                print("No such letter in the word")
                former_set.add(letter)

            if i > 0:
                print()

        if '-' in hidden:

            print("You are hanged!")


def open_letter(letter):

    global word
    global hidden

    new = ""

    i = 0
    for c in hidden:
        if word[i] == letter:
            new += letter
        else:
            new += c
        i += 1

    return new


main()
