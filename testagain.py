name = input("Enter Employee Name: ")
category = input("Enter Employee Category:\n|A| for Regular Employee\n|B| for Part-Time Employee\n|C| for Contract Employee\n|D| for Manager\n")

match category.strip().capitalize():
    case "A":
        hoursWorked = int(input("Enter of hours worked: "))
        hourlyRate = float(input("Enter hourly rate: "))
        bonus = 2000
        desc = "Regular Employee"
        if hoursWorked > 40:
            OTrate = hourlyRate*1.5
            OTPay = (hoursWorked-40) * OTrate
        else:
            print("Invalid Input")

    case "B":
        hoursWorked = int(input("Enter of hours worked: "))
        hourlyRate = float(input("Enter hourly rate: "))
        bonus = 500
        desc = "Part-Time Employee"

    case "C":
        hoursWorked = int(input("Enter of hours worked: "))
        hourlyRate = float(input("Enter hourly rate: "))
        OTrate = 1.25
        bonus = 1000
        desc = "Contract Employee"
        if hoursWorked > 40:
            OTrate = hourlyRate*1.25
            OTPay = (hoursWorked-40) * OTrate

    case "D":
        hoursWorked = int(input("Enter of hours worked: "))
        hourlyRate = float(input("Enter hourly rate: "))
        bonus = 5000
        desc = "Manager"

    case _:
        print("Invalid Input")

if (hoursWorked >40):
    regularPay = 40*hourlyRate
else:
    regularPay = hoursWorked*hourlyRate

grossSalary = regularPay + OTPay + bonus

print(f"\nEmployee name: {name.title()}\nEmployee Category: {desc}\nNumber of hours worked: {hoursWorked}\nHourly Rate: {hourlyRate}\n",
f"\nRegular Pay: {regularPay}\nOvertime Pay: {OTPay}\nBonus: {bonus}\nGross Salary: {grossSalary}")

