import random
import time

word_pairs = {
    "sky": ["blue", "cloud", "birds", "fly", "sun"],
    "ocean": ["water", "waves", "fish", "blue", "boat"],
    "forest": ["trees", "leaves", "animals", "green", "birds"],
    "fire": ["heat", "burn", "flame", "smoke", "danger"],
    "mountain": ["peak", "climb", "rock", "snow", "hiking"],
    "desert": ["sand", "hot", "cactus", "dunes", "dry"],
    "rain": ["water", "cloud", "wet", "umbrella", "storm"],
    "river": ["water", "flow", "fish", "bridge", "current"],
    "sun": ["bright", "hot", "day", "light", "shine"],
    "moon": ["night", "light", "crater", "orbit", "tide"],
    "star": ["night", "shine", "sky", "twinkle", "constellation"],
    "snow": ["cold", "white", "winter", "ice", "flake"],
    "wind": ["air", "blow", "breeze", "storm", "gust"],
    "flower": ["petal", "bloom", "garden", "fragrance", "bee"],
    "bee": ["honey", "buzz", "hive", "flower", "sting"],
    "cat": ["pet", "fur", "purr", "whiskers", "meow"],
    "dog": ["pet", "bark", "tail", "loyal", "bone"],
    "book": ["read", "pages", "cover", "author", "library"],
    "music": ["song", "melody", "sound", "instrument", "rhythm"],
    "car": ["drive", "engine", "wheel", "road", "speed"],
}

print("\n*** SIMILAR WORD GUESS *** ")
print("Enter related word to the given word QUICKLY UwU")

score=0
rounds=0

while True:
    prompt= random.choice(list(word_pairs.keys()))
    related_word = word_pairs[prompt]

    print(f"prompt word : {prompt}")
    print("Quick Type a word related to the prompt :")

    start_time=time.time()
    response=input("> ".lower().lstrip())
    response_time=time.time()-start_time

    if response in related_word:
        points=max(1,5-int(response_time))
        score += points
        print(f" Good connection +{points} points (answered in {response_time:.1f}seconds)")
    else:
        print(f"Not really a close relation . Related words include:{', '.join(related_word)}")

    rounds += 1
    print(f"Score : {score}/{rounds * 5} possible rounds")
    if input("do you wanna play again?(y/n): ").lower().startswith("n"):
        print("Final Score :{score}. Thanks for playing")
        break



