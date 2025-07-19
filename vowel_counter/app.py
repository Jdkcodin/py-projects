print("vowel counter")

while True:
    text=input("Enter the word: ")
    if text.lower() == "quit":
        print("goodbye")
        break
    vowel_count=0
    for letter in text.lower():
        if letter in ["a","e","i","o","u"]:
            vowel_count+=1
    print(f"The following word consist of :{vowel_count} ")