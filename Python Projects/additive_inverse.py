from operator import mod


element = int(input("enter element number: "))
modulus = int(input("enter modulus: "))


ai_set = []
index = 0
while (index<modulus):
    ai_set.append(index)
    index += 1

if (element not in ai_set):
    print("Invalid Element selection! Restart the program and Please select a number between 0 to " + str(ai_set[len(ai_set)-1]))
else:
    for number in ai_set:
        ai = number + element
        if mod(ai, modulus)== 0:
            print("Additive inverse of " + str(element) + " is " + str(number) + ".")
            break
            