import random
secret_words = ["limon", "plastic", "market", "wine", "cat", "frame", "purse", "cloud", "costume", "muscle", "earth", "woman", "promise", "answer", "olive", 
                "healthy", "curtain", "scream", "whisper", "mango", "protein", "rice", "nuclear", "clothes", "world", "often", "love", "mother", "walk", "half",
                "salmon", "monday", "water", "place", "thing", "number", "mister", "sound", "children", "head", "kind", "country", "father", "picture", "night"
                ]
hangman = random.choice(secret_words).upper()

print("Hangman Game:", len(hangman) * (" - "))
print("             o")
print("            -|-")
print("            / \\")
print(f"The secret word has {len(hangman)} letters. Try to win before the hangman is complete!")

letters = {}
letters_copy = {}
wrong_answer = []
x = 0
error_count = 0
index = 0

for letter in hangman:
    list.append(letter)
while index < len(hangman):
    value = hangman[index]

    letters_copy[index] = " _ "
    index += 1

hit_count = len(letters.values())

def end_game():
    print("Congratulations!!! The secret word is:")
    print("   ".join(letters.values()).upper())  

def guess_error():  

    print(f"{error_count} wrong answer(s)")
    if error_count == 1:
        print("Hangman: o")
    if error_count == 2:
        print("Hangman: o")
        print("         |")
    if error_count == 3:
        print("Hangman: o")
        print("         |-")
    if error_count == 4:
        print("Hangman: o")
        print("        -|-")
    if error_count == 5:
        print("Hangman: o")
        print("        -|-")
        print("        /  ")
    if error_count == 6:
        print("Hangman: o")
        print("        -|-")
        print("        / \\")
        print("GAME OVER!")
              
while True:
    guess = str(input("Guess one letter: ")).upper()
    if guess in letters_copy.values():
        print(f"Hangman Game already filled with '{guess}'. Try another letter")
    else:
        if guess in letters.values():
           
            keys = list(letters.keys())
            values = list(letters.values())
                    
            hit_count -= 1        
            position = values.index(guess)
            print(f"Position {position + 1} of the secret word")

            letters_copy[position] = guess

            if hit_count > 0:
                output = list(letters_copy.values())
                print(' '.join(output))

        if hit_count == 0:
            end_game()
            break
        else:
            if hit_count < len(letters):
                print(f"{hit_count} letter(s) left to complete the secret word")
            
    if guess not in letters.values():
        if guess in wrong_answer:
            print("You alreary tried this letter")
        else:
            wrong_answer.append(guess)
            error_count += 1
            guess_error()