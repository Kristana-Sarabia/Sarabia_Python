Borresname = input("Enter student's name: ")

Borresmath = float(input("Enter Math grade: "))
Borresscience = float(input("Enter Science grade: "))
Borresenglish = float(input("Enter English grade: "))

Borrestotal = Borresmath + Borresscience + Borresenglish
Borresaverage = Borrestotal / 3

print()
print("STUDENT GRADE REPORT")
print("Student Name:", Borresname)
print()
print("Math Grade:", Borresmath)
print("Science Grade:", Borresscience)
print("English Grade:", Borresenglish)
print()
print("Total Grade:", Borrestotal)
print("Average Grade:", Borresaverage)
