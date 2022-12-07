import re 
number=input("Enter the contact number: ")

def checkValid(num):
    expected= re.compile("[+]?[0-9]?[' '|-]?[(]?[0-9]{3}[)]?[-|.|' ']?[0-9]{3}[-|.|' ']?[0-9]{4}")
    return expected.match(num)

if (checkValid(number)):
    print("Contact number is valid")
else:
    print("Contact number is invalid")