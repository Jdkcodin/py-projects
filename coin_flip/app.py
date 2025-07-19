
import random
print("COIN FLIP GAME")
while True:
    guess=input("Enter your guess heads or tails:").lower()
    if guess != "heads" and guess != "tails":
        print("Please enter heads or tails")
        continue
    flip=random.choice(["heads","tails"])
    print(f"Coin shows: {flip}")
    if guess == flip:
        print("yoo right guess buddy , you win") 
    else:
        print("wrong guess bro, better luck next time")
    
    again=input("wanna play again ??(y/n)").lower()
    if not again.endswith("y"):
        break