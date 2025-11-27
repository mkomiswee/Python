def get_scores():
    score = input("Enter Student Score(Seperate by space): ")
    return [int (x) for x in score.split()]

def convert_scores(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"   


def min_grades(scores):
    return min(scores)


def max_grades(scores):
    return max(scores)


def average_scores(total):
    return sum(total) /len(total)

def filter_grades(student):
    failing = []
    passing = []

    for s in student:
        if s < 60:
            failing.append(s)
        else:
            passing.append(s)   

    return failing, passing        



scores = get_scores()

while(True):
   print("\n1. Show Grades") 
   print("2. Highest Grade")
   print("3. Lowest Grade")
   print("4. Class Average")
   print("5 Enter New Scores")
   print("6. Filter Grades")
   print("7. Quit")

   choice = input("Pick an option: ")


   if choice == "1":
       print("Current Grades:", [convert_scores(s) for s in scores])
   elif choice == "2":
       print("Highest Grade:", max_grades(scores))   
   elif choice == "3":
       print("Lowest Grade:", min_grades(scores))    
   elif choice == "4":
       print("Class Average:", average_scores(scores))  
   elif choice == "5":
       scores = get_scores()
   elif choice == "6":
       failing, passing = filter_grades(scores)
       print("Failing Grades:", failing)
       print("Passing Grades:", passing)
   elif choice == "7":
       print("GoodBye")
   else:
       print("Invalid choice. Please choose an option.")         