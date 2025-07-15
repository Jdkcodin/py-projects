while(True):
    print("\n 🔎 WEBSITE CHECKER 🔎")
    url=input("\n Enter the website URL :")

    if url.startswith("https://"):
        print("\n 🔒The website is secure (uses HTTPS)")
        exit()
    elif url.startswith("http://"):
        print("\n The Website may not be secure (uses HTTP)")
        exit()
    else:
        print("\n This doesn't seems like a valid URL")
        print("\n enter the valid one please ")