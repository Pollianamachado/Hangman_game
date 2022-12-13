import random
secret_words = ["way", "end", "air", "man", "boy", "cat", "own", "foot", "banana", "both", "rice", "come" "small", "side", "show", "land", "love", "part", "word", "walk", 
                "line", "only", "work" "half", "year", "wine", "name", "life", "live", "help", "last", "left", "down", "next", "high", "find", "want", "much", "again",
                "home", "head", "very", "just", "most", "where", "kind", "whom", "time", "apple" "often", "animal", "could", "write", "under", "while", "along", "between", 
                "might", "found", "below", "always", "above", "often", "colonel", "mother", "limon", "earth", "woman", "thought", "market", "world", "salmon", "because",  
                "frame", "water", "first" "story", "little" "night", "right" "light", "house", "school", "purse", "cloud", "answer", "olive", "mango", "large", "place", 
                "great", "thing", "sound", "monday", "number", "almost", "ironic", "volcano", "transplant", "second", "before", "around", "should", "people", "mister", "father",
                "muscle", "enought", "scream", "plastic", "together", "clothes", "desinterested", "uninterested", "enormous", "regardless", "protein", "without", "following", 
                "nuclear", "another", "costume", "country", "original", "promise", "picture", "healthy", "curtain", "microscopic", "literally", "whisper", "children", "throught", 
                "unabashed", "important", "something"
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
error_count = 0
index = 0

while index < len(hangman):
    value = hangman[index]
    letters[index] = value

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

            values = list(letters.values())

            for key, value in enumerate(values):
                if value == guess:
                    letters_copy[key] = value
                    hit_count -= 1 
                    print(f"Position {key + 1} of the secret word")
                    
            if hit_count > 0:
                output = list(letters_copy.values())
                print(' '.join(output))

        if hit_count == 0:
            end_game()
            break
        else:
            if (hit_count < len(hangman)) and (guess in letters.values()):
                print(f"{hit_count} letter(s) left to complete the secret word")
            
    if guess not in letters.values():
        if len(guess) > 1:
            if guess == "STOP":
                break
            if guess != "STOP":
                print("Try one letter at time")
        elif guess in wrong_answer: 
            print("You alreary tried this letter")
        else:
            error_count += 1 
            wrong_answer.append(guess) 
            guess_error() 
            if error_count == 6: 
                break
