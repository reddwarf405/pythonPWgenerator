import random
import string

# Lists of the possible characters that could be in the password
possibleAlpha = list(string.ascii_letters)
possibleNumSym = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "="]

# Function for generating the passwords
def generatePW():
    newPW = ""
    
    for u in range(12):
        # Attempt at guaranteeing a semi-even split between num/special chars and alpha chars
        if random.randint(1, 2) == 1:
            newPW = newPW + possibleAlpha[random.randint(0, len(possibleAlpha)-1)]
        else:
            newPW = newPW + possibleNumSym[random.randint(0, len(possibleNumSym)-1)]
    return newPW


print("Here are ten randomly-generated passwords:")
for i in range(10):
    print(generatePW())