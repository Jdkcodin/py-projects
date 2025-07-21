import time
print("\nCOUNTDOWN TIMER")
print("Countdown from your choice of seconds\n")

while True:

    seconds=int(input("\nEnter the seconds to countdown from: "))
    if seconds <= 0:
        print("Please enter a positive number lol")
        continue

    print(f"Starting Countdown from {seconds} seconds")
    
    for i in range(seconds,0,-1):
        print(f"{i} seconds remaining")
        time.sleep(1)
    
    print("\nCOUNTDOWN COMPLETE")
    
    if not input("\nWanna continue countdown ??(y/n):").lower().startswith("y"):
        print("GOODBYE")
        break
    