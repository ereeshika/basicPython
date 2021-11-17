print("Simpla Calculator")
print(" ")
print("Funtions:")
print("SUM = +")
print("SUBSTRACT = -")
print("DIVISION = /")
print("MULTIPLICATION = *")
print(" ")
operation = input("Select a function : ")
num1 = input("Enter First Number : ")
num2 = input("Enter Second Number : ")
if(operation == "+"):
    answer = int(num1)+int(num2)
elif(operation == "-"):
    answer = int(num1)-int(num2)
elif(operation == "/"):
    answer = int(num1)/int(num2)
elif(operation == "*"):
    answer = int(num1)*int(num2)
else:
    answer = ("Invalid operation")
print(" ")
print("Answer : " + str(answer))