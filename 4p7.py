#Exercise 4.7 COMPLETED

def computeGrade(score):
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
            print("D")
        else:
            print("F")
    else:
        print("Bad Score")


computeGrade(score = input("Enter Score: "))
