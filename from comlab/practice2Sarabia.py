students = {
    "Ana": [90, 85, 82],
    "Kirk": [72, 73, 78],
    "RobertJoshRas": [91, 92, 93],
    "ShemJudeAlexisSoriano": [90, 91, 92],
    "CaesarKennethDeGuia": [92, 93, 94],
    "JosiahDatrellQuistadio": [90, 91, 94]
}
highest = 0
namehighest = ""
name75 = []
for name, grade in students.items():
    average = sum(grade) / len(grade)
    print(name, *grade, "- Average:", round(average, 2))
    if average > highest:
        highest = average
        namehighest = name
    for g in grade:
        if g < 75:
            tally = tally + 1
            if name not in name75:
                name75.append(name)
print()
print("Highest average is", round(highest, 2))
print(f"Congratulations, {namehighest}!")
print(f"There are {tally} grades below 75. Owned by {', '.join(name75)}.")