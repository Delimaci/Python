# Harvad Course, 01/11/24. Ask the user their name and say which house

name = input("What's your name? ")

match name:
    case "Harry" :
        print("Gryffindor")
    case "Hermoine":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")