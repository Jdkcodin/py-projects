import random

print(" MUSIC RECOMMENDER")
genre = {
    "Pop": [
        "Taylor Swift",
        "Ed Sheeran",
        "Ariana Grande",
        "Billie Eilish",
        "Dua Lipa",
        "Harry Styles",
        "Olivia Rodrigo",
        "The Weeknd",
        "Justin Bieber",
        "Bruno Mars"
    ],
    "Rock": [
        "Foo Fighters",
        "Imagine Dragons",
        "Coldplay",
        "Red Hot Chili Peppers",
        "Green Day",
        "Muse",
        "Arctic Monkeys",
        "The Killers",
        "Linkin Park",
        "Metallica"
    ],
    "Hip Hop / Rap": [
        "Drake",
        "Kendrick Lamar",
        "J. Cole",
        "Travis Scott",
        "Lil Baby",
        "Eminem",
        "Nicki Minaj",
        "Doja Cat",
        "21 Savage",
        "Future"
    ],
    "R&B / Soul": [
        "Beyoncé",
        "The Weeknd",
        "SZA",
        "HER",
        "Frank Ocean",
        "Chris Brown",
        "Giveon",
        "Brent Faiyaz",
        "Alicia Keys",
        "Usher"
    ],
    "country": [
        "Morgan Wallen",
        "Luke Combs",
        "Carrie Underwood",
        "Chris Stapleton",
        "Kane Brown",
        "Zach Bryan",
        "Blake Shelton",
        "Miranda Lambert",
        "Kelsea Ballerini",
        "Thomas Rhett"
    ],
    "electronic / EDM": [
        "Calvin Harris",
        "David Guetta",
        "Marshmello",
        "Skrillex",
        "Diplo",
        "Kygo",
        "Zedd",
        "Martin Garrix",
        "Alan Walker",
        "Deadmau5"
    ],
    "jazz": [
        "Herbie Hancock",
        "Esperanza Spalding",
        "Wynton Marsalis",
        "Diana Krall",
        "Chick Corea",
        "Norah Jones",
        "Kamasi Washington",
        "Pat Metheny",
        "Christian McBride",
        "Brad Mehldau"
    ],
    "classical": [
        "Lang Lang",
        "Yo-Yo Ma",
        "Martha Argerich",
        "Joshua Bell",
        "Gustavo Dudamel",
        "Anne-Sophie Mutter",
        "Hilary Hahn",
        "Itzhak Perlman",
        "Daniel Barenboim",
        "Renée Fleming"
    ],
    "reggae": [
        "Bob Marley & The Wailers",
        "Burning Spear",
        "Jimmy Cliff",
        "Toots and the Maytals",
        "Ziggy Marley",
        "Damian Marley",
        "Shaggy",
        "Sean Paul",
        "Protoje",
        "Chronixx"
    ],
    "latin": [
        "Bad Bunny",
        "J Balvin",
        "Karol G",
        "Rosalía",
        "Maluma",
        "Ozuna",
        "Luis Fonsi",
        "Shakira",
        "Daddy Yankee",
        "Anitta"
    ]
}
choice = input("what genre do like to listen (Latin,Reggae,classical,R&B,Pop,Rock,EDM)")
if choice not in genre:
    print("Sorry i dont know that genre lyk tf you listening to lmao!!")
else:
    print(f"Please listen to these recommended artist/Bands :{random.choice(genre[choice])}")
