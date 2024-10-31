#31/10/24 - Python Lesson 1 (Harvard Course)
  # Ask the user for their name!
name = input("What's your name? ").strip().title()

#Split user's name into first name and last name
first, last = name.split(" ")

print(f"I have awakened, {first}")