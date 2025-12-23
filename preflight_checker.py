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
        return "NO-GO: Oil pressure critically low"
    elif oil < 40:
        return "WARNING: Oil pressure low"
    elif oil <= 80:
        return "OK: Oil pressure normal"
    elif oil <= 115:
        return "WARNING: Oil pressure high"
    else:
        return "NO-GO: Oil pressure dangerously high"


def preflight_fuel(fuel):
    if fuel == 0:
        return "NO-GO: Fuel critically low"
    elif 0 < fuel < 20:
        return "WARNING: Fuel level low"
    elif 20 <= fuel <= 100:
        return "OK: Fuel level normal"
    else:
        return "NO-GO: Fuel reading out of expected range"


def prelflight_temp(temp):
    if temp < 100:
        return "NO-GO: Engine temperature too cold for safe operation"
    elif 100 <= temp <= 180:
        return "WARNING: Engine warming up"
    elif 180 <= temp <= 245:
        return "OK: Engine temperature normal"
    elif 245 <= temp <= 260:
        return "WARNING: Engine temperature high"
    elif temp > 260:
        return "NO-GO: Engine overheating"
    else:
        return "NO-GO: Temperature reading out of expected range"


def preflight_hydrualic_pressure(hydrualic_pressure):
    if hydrualic_pressure == 0:
        return "NO-GO: No hydraulic power"
    elif 1 <= hydrualic_pressure <= 2500:
        return "WARNING: Hydraulic pressure low"
    elif 2500 <= hydrualic_pressure <= 3000:
        return "OK: Hydraulic pressure normal"
    elif 3000 <= hydrualic_pressure <= 5000:
        return "WARNING: Hydraulic pressure high"
    elif hydrualic_pressure > 5000:
        return "NO-GO: Hydraulic pressure dangerously high"
    else:
        return "NO-GO: Hydraulic pressure reading out of expected range"


def evaluation_report(fuel, temp, hydrualic_pressure,oil, battery_voltage,brakes):
    fuel_status = preflight_fuel(fuel)
    hydrualic_status = preflight_hydrualic_pressure(hydrualic_pressure)
    temp_status = prelflight_temp(temp)
    oil_status = preflight_oil(oil)
    electrical_status = electrical_system_check(battery_voltage)
    brake_status = brake_pressure_check(brakes)

    statuses = [temp_status, fuel_status, hydrualic_status, oil_status, electrical_status, brake_status]

    if any("NO-GO" in s for s in statuses):
        overall = "NO-GO"
    elif any("WARNING" in s for s in statuses):
        overall = "WARNING"
    else:
        overall = "OK"

    return {
        "fuel_status": fuel_status,
        "hydrualic_status": hydrualic_status,
        "oil_status": oil_status,
        "temp_status": temp_status,
        "electrical_status": electrical_status,
        "brake_status": brake_status,
        "overall_status": overall
    } 
def electrical_system_check(battery_voltage):
    if battery_voltage < 22.0:
        return "NO-GO: TOO LOW, UNSAFE TO DISPATCH"
    elif 22.0 <= battery_voltage <=24.0:
        return "WARNING: LOW, WEAK BATTERY/MARGINAL POWER"
    elif 24.0 <= battery_voltage <= 28.0:
        return "OK"
    elif battery_voltage > 28.0:
        return "NO-GO: OVERVOLTAGE, RISK TO AVIONICS/ELECTRONICS"
    else:
        return "NO-GO: BATTERY VOLTAGE READING OUT OF EXPECTED RANGE..."
def brake_pressure_check(brakes):
    if brakes < 500:
        return "NO-GO: BRAKE PRESSURE CRITICALLY LOW"
    elif 500 <= brakes <= 800:
        return "WARNING: BRAKE PRESSURE LOW"
    elif 800 <= brakes <= 1200:
        return "OK: BRAKE PRESSURE NORMAL"
    elif 1200 <= brakes <= 1500:
        return "WARNING: BRAKE PRESSURE HIGH"
    elif brakes > 1500:
        return "NO-GO: BRAKE PRESSURE DANGEROUSLY HIGH (RISK OF LINE RUPTURE)"
    else:
        return "NO-GO: BRAKE PRESSURE READING OUT OF EXPECTED RANGE"


    




     






        

    
    
    
        








