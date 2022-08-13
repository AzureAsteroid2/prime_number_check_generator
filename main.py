"""This program will create a HORRENDOUS .py file that can be run to check prime numbers up to a certain point. It is pure pain"""
import os

def main():
  numbers = input("How many numbers should be checked? ")
  try:
    numbers = int(numbers)
    file = open("prime.py, 'w'")
  except:
    print("Only put positive whole numbers!")
  for i in len(numbers):
    if i%[2,3,5]:
      file += f"\nif number == {i}: #checks if number {i} is prime\n   print(f'{i} is not a prime number') #prints that {i} is not a prime number"
    else:
      file += f"\nif number == {i}: #checks if number {i} is prime\n   print(f'{i} is a prime number') #prints that {i} is a prime number"
if __name__ == '__main__':
  main()