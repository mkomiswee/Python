
def vehicle_records():
  fleet = [
    {
        "type": "car",
        "make": "Toyota",
        "model": "Camry",
        "year": 2018,
        "mileage": 74200,
        "status": "available"
    },
    {
        "type": "car",
        "make": "Honda",
        "model": "Civic",
        "year": 2020,
        "mileage": 38500,
        "status": "in_service"
    },
    {
        "type": "truck",
        "make": "Ford",
        "model": "F-150",
        "year": 2017,
        "mileage": 128400,
        "status": "needs_repair"
    },
    {
        "type": "truck",
        "make": "Chevrolet",
        "model": "Silverado",
        "year": 2019,
        "mileage": 90500,
        "status": "available"
    },
    {
        "type": "van",
        "make": "Mercedes",
        "model": "Sprinter",
        "year": 2021,
        "mileage": 41200,
        "status": "available"
    },
    {
        "type": "van",
        "make": "Ford",
        "model": "Transit",
        "year": 2016,
        "mileage": 167300,
        "status": "needs_repair"
    }
]
  for index, vehicle in enumerate(fleet, start=1):
    print(index, fleet["car"])

def add_vehicle(fleet, vehicle):
  fleet.append(vehicle)
  return fleet
  

def remove_vehicle(fleet, make, model):
  for index, vehicle in enumerate(fleet):
    if make 
      
      
  


