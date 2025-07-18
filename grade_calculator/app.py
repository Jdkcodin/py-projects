print(" GRADE CALCULATOR ")
scores=[]

while True:
    score=input("Enter the test score:")
    if score.lower() == "done":
        print(" GOODBYE ")
        break
    score=float(score)
    scores.append(score)
    average = sum(scores) / len(scores)
    print("Average score is : {average:.1f}")
    if average >= 90:
        print ("Grade:A") 
    elif average >= 80:
        print ("Grade:B") 
    elif average >= 70:
        print ("Grade:C") 
    elif average >= 60:
        print ("Grade:D") 
    elif average >= 50:
        print ("Grade:E") 