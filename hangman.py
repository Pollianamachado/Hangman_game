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

list = []
attempt = []
x = 0
error_count = 0

for letter in hangman:
    list.append(letter)

hit_count = len(list)

def end_game():
    print("Congratulations!!! The secret word is:")
    print("   ".join(list).upper()) 

def guess_error():  

    print("Wrong!")
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
    guess = str(input("Enter one letter: ")).upper()
    if guess in attempt:
        print(f"Hangman Game already filled with '{guess}'. Try another letter")
        continue
    elif guess in list:
        hit_count -= 1
        attempt.append(guess)
        if guess == list[0]:
            if len(attempt) == len(list):
                end_game()
                break
            else:
                print(f"Position {list.index(guess) + 1} of the secret word")
                print(guess, (len(list) - 1) * (" - "))
                # print((attempt) - (set(list).difference(attempt)))
        elif guess == list[1]:
            if len(attempt) == len(list):
                end_game()
                break
            else:
                print(f"Position {list.index(guess) + 1} of the secret word")
                print(f" -  {guess}", (len(list) - 2) * (" - "))
        elif guess == list[2]:
            if len(attempt) == len(list):
                end_game()
                break
            else:
                print(f"Position {list.index(guess) + 1} of the secret word")
                print(" - ", " - ", guess, (len(list) - 3) * (" - "))
        elif guess == list[3]:
            if len(attempt) == len(list):
                end_game()
                break
            else:
                print(f"Position {list.index(guess) + 1} of the secret word")
                print(" - ", " - ", " - ", guess, (len(list) - 4) * (" - "))
        elif guess == list[4]:
            if len(attempt) == len(list):
                end_game()
                break
            else:
                print(f"Position {list.index(guess) + 1} of the secret word")
                print(" - ", " - "," - "," - ", guess, (len(list) - 5) * (" - "))
        elif guess == list[5]:
            if len(attempt) == len(list):
                end_game()
                break
            else:
                print(f"Position {list.index(guess) + 1} of the secret word")
                print(" - ", " - "," - "," - "," - ", guess, (len(list) - 6) * (" - "))
        elif guess == list[6]:
            if len(attempt) == len(list):
                end_game()
                break
            else:
                print(f"Position {list.index(guess) + 1} of the secret word")
                print(" - ", " - "," - "," - "," - "," - ", guess, (len(list) - 7) * (" - "))
        elif guess == list[7]:
            if len(attempt) == len(list):
                end_game()
                break
            else:
                print(f"Position {list.index(guess) + 1} of the secret word")
                print(" - ", " - "," - "," - "," - ", guess, (len(list) - 3) * (" - "))
        if hit_count == 0:
            end_game()
            break
        else:
            print(f"{hit_count} letter(s) left to complete the secret word")
    elif guess not in list:
        error_count += 1
        guess_error()