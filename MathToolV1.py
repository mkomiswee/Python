import statistics


def get_numbers():
    num = input("Please Enter Numbers (Seperate By Space): ")
    parts = num.split()
    numbers = [int(x) for x in parts]
    return numbers



def numbers_filter(numbers, condition):
    return[num for num in numbers if condition(num)]
    
def add_num(numbers):
    return sum(numbers)    


def average_num(numbers):
    return sum(numbers) / len(numbers)

def min_num(numbers):
    return min(numbers)
   
def max_num(numbers):
    return max(numbers)
   
def median_num(numbers):
    return statistics.median(numbers)


numbers = get_numbers()
while(True):
    print("1. Evens")
    print("2. Odds")
    print("3. Find Average")
    print("4. Add Numbers")
    print("5. Min")
    print("6. Max")
    print("7. Median")
    print("8. Quit")
    print("9. Enter New Numbers")

    choice = input("Please Choose An Operation: ")

    if choice == "8":
        print("GoodBye!")
        break
    elif choice == "9":
       numbers = get_numbers()
    elif choice == "1":
       print("Evens:", numbers_filter(numbers, lambda x: x % 2 == 0))
    elif choice == "2":
      print("Odds:", numbers_filter(numbers, lambda x: x % 2 !=0))
    elif  choice == "3":
      print("Average:",average_num(numbers))
    elif choice == "4":
      print("Add:" ,add_num(numbers))
    elif choice == "5":
      print("Min:", min_num(numbers))    
    elif choice == "6":
     print("Max:", max_num(numbers))
    elif choice == "7":
     print("Median:", median_num(numbers))      
    else:
     print("Operation Not Completed. Please Try Again!")     










    