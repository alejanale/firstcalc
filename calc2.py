# this function adds 2 numbers
def add(x, y):
    return x + y

# this function subtracts 2 numbers
def subtract(x, y):
    return x - y

# this function multiplies 2 numbers
def multiply(x, y):
    return x * y

# this function divides 2 numbers
def divide(x, y):
    return x / y

# This function squares a number
def square(x):
      return x ** 2      

# This function multiplies to the power of
def power(x, y):
      return x ** y

print("Select operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square")
print("6. Power")

while True:
    # take input from user
     choice = input("Enter choice(1/2/3/4/5/6): ")

     # check if choice is one of the six operations
     if choice in ('1','2','3','4','6'):
         try:
           num1 = float(input("Enter first number: "))
           num2 = float(input("Enter second number: "))
         except ValueError:
               print("Invalid input. Please enter numeric values.")
               continue
     if choice in ('5'):
         try:
              num1 = float(input("Enter first number: "))
         except ValueError:
              print("Invalid input. Please enter numeric values.")
         if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

         elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2)) 

         elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

         elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

         elif choice == '5':
           print(num1, "^", "2", "=", square(num1))
     
         elif choice == '6':
           print(num1, "^", num2, power(num1, num2))

     next_calculation = input("Let's do next calculation? (yes/no): ")
     if next_calculation == "no":
                break
else:
    print("Invalid input")