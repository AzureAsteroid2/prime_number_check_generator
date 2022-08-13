"""This program will create a HORRENDOUS prime.py file that can be run to check prime numbers up to a number of your choosing. It is pure pain"""
import os
from sympy import isprime
def main():
  numbers = input("How many numbers should be checked? ")
  try:
    if int(numbers) <= 0:
      print(numbers)
      raise ValueError("Only put positive whole numbers!")
    else:
      numbers = int(numbers)
      file = open("prime.py", 'w')
      file.write(f"input('what number do you want to check? (input 1 or above up to {numbers})') #asks the user for number input")
  except:
    print("Only put positive whole numbers!")
  for i in range(numbers):
    i += 1
    if isprime(i) is False:
      file.write(f"\nif number == {i}: #checks if number {i} is prime\n   print(f'{i} is not a prime number') #prints that {i} is not a prime number")
    else:
      file.write(f"\nif number == {i}: #checks if number {i} is prime\n   print(f'{i} is a prime number') #prints that {i} is a prime number")
  file.close()
if __name__ == '__main__':
  main()