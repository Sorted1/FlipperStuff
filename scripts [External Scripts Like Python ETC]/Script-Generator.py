import os, time

banner = """Type Somthing In Notpad [1] | """

print(banner)
choice = input("Enter Choice: ")

if choice == "":
    print("Please Choose A Active Choice!")

if choice == "1":
    text = input("Enter Text You Want To Show: ")
    file = input("File you want to write to: ")
    print("Generating.")
    time.sleep(1)
    print("Generating..")
    time.sleep(1)
    print("Generating...")
    time.sleep(1)
    print(f"Generated You Can Find It In This Text File {file}")
    with open(f"{file}", "w") as file:
        file.write(f"GUI r\nDELAY 200\nSTRING notepad\nENTER\nDELAY 1000\nSTRING {text}\nENTER")