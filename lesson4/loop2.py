# Harvad Course, 02/11/24
  #Ask the user how many times the cat should meow

def main():
    number = get_number()
    meow(number)

# get the number
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n 

# print meow n times
def meow(n):
    for _ in range(n):
        print("meow")


main()