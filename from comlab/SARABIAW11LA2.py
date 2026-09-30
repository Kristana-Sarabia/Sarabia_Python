print(f"{'STUDENT PROGRAM FILTER0':=^40}")

students = [("Jonah Perez", "BSCS", 1),
            ("Alex Santos", "BSMT", 1),
            ("Micah Mendoza", "BSCS", 1),
            ("Allen Torres", "BSMT", 1),
            ("Cheijay Paul Loberiza", "BSCS", 3),
            ("Dean MisaBustamante", "BSMT", 3),
            ("Datrell Quistadio", "BSCS", 4),
            ("Cat Dela Cruz", "BSMT", 4)]

print("Student Information")
for student in students:
    print("Name: ", student[0])
    print("Program: ", student[1])
    print("Year Level: ", student[2])
    print()

program = input("Search program: ")
print("Students in ", program.upper(), " program: ")

found = False
for student in students:
     if program == student[1].lower():
         print("Name: ", student[0])
         print("Program: ", student[1])
         print("Year Level: ", student[2])
         print()
         found = True

if not found:
    print("No students.")