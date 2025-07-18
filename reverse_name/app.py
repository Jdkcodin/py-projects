print(" REVERSE YOUR NAME")
while True:
    inp_string=input("Enter a name: ")
    name=list(inp_string)
    new_name=name[::-1]
    print(f"your reversed name is :{new_name}")