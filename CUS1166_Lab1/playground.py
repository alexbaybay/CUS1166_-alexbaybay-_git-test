#regular print statement
print("Hello world")

#variables
a = 25
print(f"\n\nThe value of a is {a}")

a = 3.87
print("The new value of a is " + str(a))

a = "Samantha"
print(f"The new value of a is {a}")

a = True
print(f"a now has a value of {a} and is type {type(a)}")

n = 15

if(n > 0):
    print("\n\nThe number you entered is positive.")

elif(n < 0):
    print('The number you entered is negative.')

else:
    print("The number you entered is zero.")

my_name = input("\n\nWhat is your name? ")
print("End of Practice " + my_name)
