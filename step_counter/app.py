
print("🚶🏻‍♂️ Steps Counter🚶🏻")
daily_goal=int(input("What is your daily step goal??\n"))
while(True):
    steps_taken=int(input("How many steps have you taken today??\n"))
    if steps_taken > daily_goal:
        print("😃 Wow!! YOU HAVE EXCEEDED YOUR GOAL.\n")
        exit()
    elif steps_taken == daily_goal:
        print("🎉 Superb!! You've got your daily steps in good work.\n")
        exit()
    elif steps_taken < daily_goal:
        print("🫵🏽 HEY you , yes YOU Go walk outside and touch grass so that you can get those steps")


