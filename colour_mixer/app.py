print("welcome to colour mixer\n")
colour_mixes={
    ("red", "blue"): "purple",
    ("red", "yellow"): "orange",
    ("blue", "yellow"): "green",
    ("red", "white"): "pink",
    ("blue", "white"): "light blue",
    ("yellow", "white"): "light yellow",
    ("red", "black"): "dark red",
    ("blue", "black"): "navy",
    ("yellow", "black"): "olive",
    ("white", "black"): "grey",
    ("red", "green"): "brown",
    ("blue", "green"): "teal",
    ("yellow", "green"): "lime",
    ("red", "purple"): "magenta",
    ("blue", "purple"): "violet",
    ("yellow", "purple"): "mauve"
}
while True:
    color1=input("\n Enter the first color : ")
    color2=input("\n Enter the second color : ")
    
    mix=None

    if (color1,color2) in colour_mixes:
        mix=colour_mixes[(color1,color2)]

    elif (color2,color1) in colour_mixes:
        mix = colour_mixes[(color2,color1)]
        
    if mix:
        print(f"When we mix {color1} and {color2} we get : {mix}")
    else:
        print("Those colour combination is not known to me :( ")
    
    if not input("Continue mixing colour's (Y/n): ").lower().startswith("y"):
        print("GOODBYE RAINBOW BOY")
        break
