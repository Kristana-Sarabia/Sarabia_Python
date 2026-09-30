from typing import Sized

name = (input("Name: "))
coffeeSize = (input("\nChoose Coffee Size:\nSmall\nMedium\nLarge\n\n").strip().capitalize())
extraShot = (input("\nExtra Shot?\nYes\nNo\n\n").strip().capitalize())

if coffeeSize == "Small".strip().capitalize():
    smallPrice: int = 80
    if extraShot == "Yes".strip().capitalize():
        extraShotPrice: int = 30
    else:
        extraShotPrice: int = 0
elif coffeeSize == "Medium".strip().capitalize():
    mediumPrice: int = 100
    if extraShot == "Yes".strip().capitalize():
        extraShotPrice: int = 30
    else:
        extraShotPrice: int = 0
elif coffeeSize == "Large".strip().capitalize():
    largePrice: int = 120
    if extraShot == "Yes".strip().capitalize():
        extraShotPrice: int = 30
    else:
        extraShotPrice: int = 0
else:
    print("Please choose a coffee size")



print ("===== COFFEE RECEIPTS =====")
print ("Customer: ", name)
print ("Coffee Size: ", coffeeSize)
print ("Extra Shot: ", extraShot)
print ("Total: ",)
