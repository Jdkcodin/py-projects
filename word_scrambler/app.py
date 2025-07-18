import random 
print("WORD SCRAMBLER")

while True:
    word = input("Enter the word to be scrambled (or 'quit') : ")
    if word == "quit":
        print("GOODBYE")
        break
    letter = list(word)
    random.shuffle(letter)
    print(f"The Scrambled word is : {"".join(letter)}")