"""This program will create a HORRENDOUS prime.py file that can be run to check prime numbers up to a number of your choosing. It is pure pain"""
import os
from sympy import isprime
def main():
  numbers = input("How many numbers should be checked? ")
  try:
    #sends a message if the user does not input a number correctly
    #how do you mess that up though?
    if int(numbers) <= 0:
      print(numbers)
      raise ValueError("Only put positive whole numbers!")
    else:
      numbers = int(numbers)
      file = open("prime.py", 'w')
      file.write("\ntry:")
      file.write(f"\n number = input('what number do you want to check? (input whole numbers 1 or above up to {numbers})') #asks the user for number input")
      file.write("\n number = int(number)")
      
  except:
    print("Only put positive whole numbers!")
    exit(0)
  for i in range(numbers):
    i += 1
    if isprime(i) is False:
      file.write(f"\n if number == {i}: #checks if number {i} is prime\n   print('{i} is not a prime number') #prints that {i} is not a prime number")
    else:
      file.write(f"\n if number == {i}: #checks if number {i} is prime\n   print('{i} is a prime number') #prints that {i} is a prime number")
  file.write(f"\n if number <= 0 or number > {numbers}:\n   print('You didn\\'t put a number in the range specified! perish!')")
  file.write("\nexcept ValueError:\n print('Don\\'t be stupid')")
  file.close()
  print("done!")
if __name__ == '__main__':
  main()