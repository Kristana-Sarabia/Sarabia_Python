SarabiaSalary = {"E104": {
                    "Employee Name": "Cheijay Loberiza",
                    "Daily Hours": [8, 9, 8.5, 10, 8]
},
                "E601": {
                    "Employee Name": "Datrell Falcon",
                    "Daily Hours": [9, 10, 8, 8, 9]
    }
}

SarabiaEmpInfo = ""
SarabiaOT = 0
SarabiaWeeklyBasic = 9000
SarabiaRateperHour = SarabiaWeeklyBasic/40

for SarabiaEmp_ID, SarabiaEmpInfo in SarabiaSalary.items():
    print(f"ID: {SarabiaEmp_ID} | Name: {SarabiaEmpInfo['Employee Name']} | Hours: {SarabiaEmpInfo['Daily Hours']}")
    print()

SarabiaSearch = input("Search for Employee ID: ").upper()
print("Running Employee ID match for: ", SarabiaSearch)

Sarabiafound = False

for SarabiaEmp_ID, SarabiaEmpInfo in SarabiaSalary.items():
    if SarabiaSearch == SarabiaEmp_ID:
        print(f"Name: {SarabiaEmpInfo['Employee Name']}"
              f"\nDuty Hours: {', '.join(map(str, SarabiaEmpInfo['Daily Hours']))}")
        Sarabiafound = True

        SarabiaOT = 0
        for hours in SarabiaEmpInfo['Daily Hours']:
            if hours > 8:
                SarabiaOT += (hours - 8) * (1.5 * SarabiaRateperHour)
                print(f"\nExcess Hours: {(hours - 8)}"
                      f"\nRate per Hour: {SarabiaRateperHour}")
        GrossPay = (40 * SarabiaRateperHour) + SarabiaOT
        print(f"\nTotal overtime pay: {SarabiaOT:,.2f}"
              f"\nWeekly Basic: {SarabiaWeeklyBasic}"
              f"\nGross Pay: {GrossPay:,.2f}")

if not Sarabiafound:
    print("Invalid Employee ID.")
