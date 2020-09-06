'''
Sicong Leng
sleng1@binghamton.edu
Section B55
Assignment #1
'''

# This program outputs the total number of introductions possible if each
# person in a room introduces themselves to every other person in the room 
# once, given the number of people in the room

def main():
  # tell purpose of program to user

  print('This program tells you how many introductions need to make')

  print('When each person introduces once to everyone else')

  # Ask user to input number of people in room

  print('Type number of people')

  person_count_str = input()

  # Convert str data to int

  person_count_int = int(person_count_str)

  # Use the formula to compute the result

  introduction_int = (person_count_int * (person_count_int - 1)) // 2

  # Display how many people need how many intro

  print(person_count_int , 'people will need' , introduction_int, 'introductions.' )
  
if __name__ == '__main__':
  main()














