Sarabianame = input("Name: ")

Sarabiacalculation = input('''Choose from below to calculate:\n|Power|\n|Voltage|\n|Current|\n\n''').strip().capitalize()

if Sarabiacalculation == "Power":
    Sarabiacurrent = float(input("Current: "))
    Sarabiavoltage = float(input("Voltage: "))
    Sarabiapower = Sarabiacurrent * Sarabiavoltage
    print (f"Power is {Sarabiapower:.2f}")
elif Sarabiacalculation == "Current":
    Sarabiapower = float(input("Power: "))
    Sarabiavoltage = float(input("Voltage: "))
    Sarabiacurrent = Sarabiapower / Sarabiavoltage
    print(f"Current is {Sarabiacurrent:.2f}")
elif Sarabiacalculation == "Voltage":
    Sarabiapower = float(input("Power: "))
    Sarabiacurrent= float(input("Current: "))
    Sarabiavoltage = Sarabiapower / Sarabiacurrent
    print(f"Voltage is {Sarabiavoltage:.2f}")
else:
    print("Invalid input")


