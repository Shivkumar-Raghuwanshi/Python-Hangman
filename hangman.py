from random import choice
from collections import Counter

g21_countries = '''Argentina Australia Brazil Canada China France Germany India Indonesia Italy Japa Republic_of_Korea Mexico Russia Saudi_Arabia South_Africa Türkiye United_Kingdom United_States European_Union African_Union'''

country = g21_countries.split()
# randomly choose a secret word from our "g21_countries".


word_of_country = choice(country)

if __name__ == '__main__':
    print('Guess the word! HINT: word is a name of a G21 countries')

    for char in word_of_country:
        # For printing the empty spaces for letters of the word
        print('_', end=' ')

    # list for storing the letters guessed by the player
    guessed_letter = ''
    chances = len(word_of_country) + 2
    print("\nYou have only", chances, "chances to guess the word")
    correct = 0
    flag = 0

    try:
        while (chances != 0) and flag == 0:  # flag is updated when the word is correctly guessed
            chances -= 1
            try:
                guess = str(input('\nEnter a letter to guess: '))
            except:
                print('\nEnter only a letter!')
                continue

            # Validation of the guess
            if not guess.isalpha():
                print('\nEnter only a LETTER')
                continue
            elif len(guess) > 1:
                print('\nEnter only a SINGLE letter')
                continue
            elif guess in guessed_letter:
                print('\nYou have already guessed that letter')
                continue

            # If letter is guessed correctly
            if guess in word_of_country:
                # number_of_already_guessed stores the number of times the guessed letter occurs in the word
                number_of_already_guessed = word_of_country.count(guess)
                for _ in range(number_of_already_guessed):
                    guessed_letter += guess  # The guess letter is added as many times as it occurs

            # Print the word
            for char in word_of_country:
                if char in guessed_letter and (Counter(guessed_letter) != Counter(word_of_country)):
                    print(char, end=' ')
                    correct += 1
                # If user has guessed all the letters once the correct word is guessed fully,
                elif (Counter(guessed_letter) == Counter(word_of_country)):
                    # the game ends, even if chances remain
                    print('\nCongratulations, You won!')
                    flag = 1
                    print("\nThe word was: ", word_of_country)
                    break  # To break out of the for loop
                else:
                    print('_', end=' ')

        # If user has used all of his chances
        if chances <= 0 and (Counter(guessed_letter) != Counter(word_of_country)):
            print('\nYou lost! Try again..')
            print('\nThe word was: ', word_of_country)

    except KeyboardInterrupt:
        print('Bye! Try again.')
        exit()
