def valid_preflight_values(fuel, hydrualic_pressure, oil,temp):
    if isinstance(fuel, (int, float)):
        fuel = float(fuel)
    else:
        raise ValueError("Fuel must be numeric")    
    if fuel < 0:  
        raise ValueError("Fuel cannot be a negative")
    if fuel == 0:
        pass
    if fuel > 0:
        pass


    MAX_HYDRUALIC_PRESSURE = 6000
    if isinstance(hydrualic_pressure, (int, float)):
        hydrualic_pressure = float(hydrualic_pressure)
    else:
        raise ValueError("hydrualic pressure must be numeric")
    if hydrualic_pressure < 0:
        raise ValueError("Hydrualic pressure cannot be negative")
    if hydrualic_pressure == 0:
        pass
    if hydrualic_pressure > 0:
        pass

    if hydrualic_pressure > MAX_HYDRUALIC_PRESSURE:
        raise ValueError("Hydrualic pressure reading is unrealistically high")  

    MAX_OIL_PRESSURE = 120

    if isinstance(oil, (int,float)):
        oil = float(oil)
    else:
        raise ValueError("Oil must be numeric")
    if oil < 0:
        raise ValueError("Oil level cannot be negative")
    if oil == 0:
        pass
    if oil > 0:
        pass
    if oil > MAX_OIL_PRESSURE:
        raise ValueError("Oil is unrealistically high")
    
    MAX_ENGINE_TEMP = 600

    if isinstance(temp, (int, float)):
        temp = float(temp)
    else:
        raise ValueError("Temp must be numeric")
    if temp == 0:
        pass
    if temp > 0:
        pass
    if temp > MAX_ENGINE_TEMP:
        raise ValueError("Engine tempature is unrealstically high")    
def preflight_oil(oil):
    if oil < 25:
        return ("NO-GO: Oil pressure critically low", 2)
    elif oil < 40:
        return ("WARNING: Oil pressure low",1)
    elif oil <= 80:
        return ("OK: Oil pressure normal", 0)
    elif oil <= 115:
        return ("WARNING: Oil pressure high",1)
    else:
        return ("NO-GO: Oil pressure dangerously high",2)


def preflight_fuel(fuel):
    if fuel == 0:
        return ("NO-GO: Fuel critically low",2)
    elif 0 < fuel < 20:
        return ("WARNING: Fuel level low", 1)
    elif 20 <= fuel <= 100:
        return ("OK: Fuel level normal", 0)
    else:
        return ("NO-GO: Fuel reading out of expected range",2)


def prelflight_temp(temp):
    if temp < 100:
        return ("NO-GO: Engine temperature too cold for safe operation",2)
    elif 100 <= temp <= 180:
        return ("WARNING: Engine warming up",1)
    elif 180 <= temp <= 245:
        return ("OK: Engine temperature normal",0)
    elif 245 <= temp <= 260:
        return ("WARNING: Engine temperature high", 1)
    elif temp > 260:
        return ("NO-GO: Engine overheating", 2)
    else:
        return ("NO-GO: Temperature reading out of expected range",2)


def preflight_hydrualic_pressure(hydrualic_pressure):
    if hydrualic_pressure == 0:
        return ("NO-GO: No hydraulic power",2)
    elif 1 <= hydrualic_pressure <= 2500:
        return ("WARNING: Hydraulic pressure low",1)
    elif 2500 <= hydrualic_pressure <= 3000:
        return ("OK: Hydraulic pressure normal",0)
    elif 3000 <= hydrualic_pressure <= 5000:
        return ("WARNING: Hydraulic pressure high",1)
    elif hydrualic_pressure > 5000:
        return ("NO-GO: Hydraulic pressure dangerously high",2)
    else:
        return ("NO-GO: Hydraulic pressure reading out of expected range",2)


def evaluation_report(fuel, temp, hydrualic_pressure,oil, battery_voltage,brakes):
    fuel_msg, fuel_status = preflight_fuel(fuel)
    hydrualic_msg, hydrualic_status = preflight_hydrualic_pressure(hydrualic_pressure)
    temp_msg, temp_status = prelflight_temp(temp)
    oil_msg, oil_status = preflight_oil(oil)
    electrical_msg, electrical_status = electrical_system_check(battery_voltage)
    brake_msg, brake_status = brake_pressure_check(brakes)

    statuses = [temp_status, fuel_status, hydrualic_status, oil_status, electrical_status, brake_status]

    highest = max(statuses)

    if highest == 2:
        overall = ("NO GO", 2)
    elif highest == 1:
        overall = ("WARNING", 1)
    else:
        overall = ("OK", 0)

    return {
        "fuel_status": (fuel_msg, fuel_status),
        "hydrualic_status": (hydrualic_msg, hydrualic_status),
        "oil_status": (oil_msg,oil_status),
        "temp_status": (temp_msg,temp_status),
        "electrical_status": (electrical_msg,electrical_status),
        "brake_status": (brake_msg, brake_status),
        "overall_status": overall
    } 
def electrical_system_check(battery_voltage):
    if battery_voltage < 22.0:
        return ("NO-GO: TOO LOW, UNSAFE TO DISPATCH",2)
    elif 22.0 <= battery_voltage <=24.0:
        return ("WARNING: LOW, WEAK BATTERY/MARGINAL POWER",1)
    elif 24.0 <= battery_voltage <= 28.0:
        return "OK",0
    elif battery_voltage > 28.0:
        return ("NO-GO: OVERVOLTAGE, RISK TO AVIONICS/ELECTRONICS",2)
    else:
        return ("NO-GO: BATTERY VOLTAGE READING OUT OF EXPECTED RANGE...",2)
def brake_pressure_check(brakes):
    if brakes < 500:
        return ("NO-GO: BRAKE PRESSURE CRITICALLY LOW",2)
    elif 500 <= brakes <= 800:
        return ("WARNING: BRAKE PRESSURE LOW",1)
    elif 800 <= brakes <= 1200:
        return ("OK: BRAKE PRESSURE NORMAL",0)
    elif 1200 <= brakes <= 1500:
        return ("WARNING: BRAKE PRESSURE HIGH",1)
    elif brakes > 1500:
        return ("NO-GO: BRAKE PRESSURE DANGEROUSLY HIGH (RISK OF LINE  RUPTURE",2)
    else:
        return ("NO-GO: BRAKE PRESSURE READING OUT OF EXPECTED RANGE",2)
    


def fleet():
    fleet = [
        {
            "tail_number": "N4821A",
            "fuel": 55,
            "oil": 72,
            "temp": 210,
            "hydrualic_pressure": 2900,
            "battery_voltage": 24.5,
            "brakes": 950
        },
        {
            "tail_number": "N7713Q",
            "fuel": 12,
            "oil": 38,
            "temp": 165,
            "hydrualic_pressure": 2400,
            "battery_voltage": 23.1,
            "brakes": 780
        },
        {
            "tail_number": "N9027K",
            "fuel": 0,
            "oil": 18,
            "temp": 95,
            "hydrualic_pressure": 500,
            "battery_voltage": 21.4,
            "brakes": 430
        },
        {
            "tail_number": "N3159X",
            "fuel": 88,
            "oil": 110,
            "temp": 255,
            "hydrualic_pressure": 4100,
            "battery_voltage": 26.7,
            "brakes": 1300
        },
        {
            "tail_number": "N6602M",
            "fuel": 102,
            "oil": 125,
            "temp": 240,
            "hydrualic_pressure": 5200,
            "battery_voltage": 29.1,
            "brakes": 1600
        }
    ]

    for index, airplane in enumerate(fleet, start=1):
        print(index, airplane["tail_number"])


def evalute_fleet(fleet):
    results = []

    for index, airplane in enumerate(fleet, start=1):
        report = (evaluation_report(airplane["fuel"], airplane["oil"], airplane["temp"], airplane["hydrualic_pressure"], airplane["battery_voltage"],airplane["brakes"]))
        results.append({"index": index, "tail_number": airplane["tail_number"], "report":[report]})



    




     






        

    
    
    
        








