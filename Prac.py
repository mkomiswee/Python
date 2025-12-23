import math



data = ["apple", 12, "banana", -3, "carrot", 7.5, ["pear", 0, "grape", 4]]

def inventory_counter(item, index=0):
    if isinstance(item, str):
        return item.upper()
    elif isinstance(item, (int, float)):
          if item >= 0:
              if isinstance(item, float):
                  return math.floor(item)
              else:
                  return item
          else:
              return "NEGATIVE QUANTITY"
    elif isinstance(item, list):
        return [inventory_counter(sub_item, sub_index)
                for sub_index, sub_item in enumerate(item)]
    else:
         return "unknown type"
    
results = []
for index, item in enumerate(data):
        results.append(inventory_counter(item , index))


print(results)








































data = ["Soda", 1.25, "Chips", -2, "Candy", True, ["Water", 0, "Juice", "error", None]]

def vending_machine(item, index=0):
     if isinstance(item, str):
          if item.lower() == "error":
               return "MISSING ITEM"
          else:
               return item.upper()
     elif isinstance(item, (int, float)):
          if item >= 0:
               if isinstance(item, float):
                    return math.floor(item)
               else:
                    return item
          else:
               return "INVALID PRICE"
     elif isinstance(item, bool):
          return not item    
     elif isinstance(item, list):
          return [vending_machine(sub_item, sub_index)
                  for sub_index, sub_item in enumerate(item)]
     else:
          return "unknown type"
     
results = []
for index, item in enumerate(data):
     results.append(vending_machine(item, index))
print(results)      

     














data = [
    "Alice", 20, "Bob", -3, "Charlie", None,
    ["Dana", 18.5, "Raj", "error", True, ["Eve", 22, "Sam", "missing"]]
]

def student_system(item, index=0):
     if isinstance(item, str):
          if item.lower() == "error":
               return "MISSING NAME"
          if item.lower() == "missing":
               return "NO DATA"
          else:
               return item.upper()
     elif isinstance(item, (int, float)):
          if item >= 0 and item <= 120:
               if isinstance(item, float):
                    return math.floor(item)
               else:
                    return item
          else:
               return "INVALID AGE"   
     elif isinstance(item, bool):
          return not item
     
     elif isinstance(item, list):
          return [student_system(sub_item, sub_index)
                  for sub_index, sub_item in enumerate(item)]
     
     else:
          return "unknown type"
     
results = []
for index, item in enumerate(data):
     results.append(student_system(item, index))
print(results)          

          
          
   
               
     
            
        

        
       
          

    
