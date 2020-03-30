#Exercise 3.3 Completed
score = input("Enter Score: ")
try:
    iscore = float(score)
except:
    iscore = -1

if iscore >0 and iscore <1:
    if iscore>=0.9:
        print("A")
    elif iscore>=0.8:
        print("B")
    elif iscore>=0.7:
        print("C")
    elif iscore>=0.6:
        print("D")a
    else:
        print("F")
else:
    print("Score is out of range. Please enter a number 0.0-1.0:")
