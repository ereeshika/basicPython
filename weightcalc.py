weight = float(input("What is your weight ? "))
option = input("Do you want in (K)g or (L)bs : ")
if (option.upper == "k"):
    answer = weight/2.2
elif (option.upper == "l"):
    answer = weight*2.2
else:
    answer = ("Invalid option")

print (answer)
