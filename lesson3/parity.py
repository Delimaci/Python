 # Harvard Course, checking if number is even or odd (01/11/24
    # using % as mod operator
def main():
    x = int(input("What's x? "))
    # asume there is a function 
    if is_even(x): #parameter from is_even function
        print("Even")

    else:
        print("Odd")

# Function for checking if number is even/odd
def is_even(n): # parameter to pass
    return n % 2 == 0

main()