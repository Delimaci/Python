# Harvard course, 02/11/24
  # Creating mario kart

def main():
    print_square(3)

def print_square(size):
    
    #for each row in square
    for i in range(size):
        
        #for each break in row
        for j in range(size):
            
            # print brick
            print("#", end="")
        print()
        
main()