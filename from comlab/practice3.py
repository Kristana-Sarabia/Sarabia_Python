while True:
    word = input("Enter a word: ")
    character = input("Enter a character to search for: ")

    found = False

    for character in word:
        if character.lower() == character.lower():
            found = True
            break
    if found:
        print ("Character Found!")
    else:
        print ("Character not found.")
    again = input("Try again? (Y/N): ")
    if again.upper() != "Y":
        break