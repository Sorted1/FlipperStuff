#MADE BY SORTED
#MADE BY SORTED
#MADE BY SORTED
#MADE BY SORTED

with open("passcodes.txt", "w") as file:
    # Loop through all possible combinations of 4 digits
    for i in range(10000):
        # Convert the number to a 4-digit string, padded with leading zeros
        passcode = "{:04d}".format(i)
        # Write the passcode to the text file
        file.write(passcode + "\n")
