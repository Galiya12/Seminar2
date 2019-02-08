class Error(Exception):
   """Base class for other exceptions"""
   pass

class ValueTooSmallError(Error):
   """Raised when the input value is too small"""
   pass

class ValueTooLargeError(Error):
   """Raised when the input value is too large"""
   pass

class ValueIsZero(Error):
   """Raised when the input value is zero"""
   pass

def guessNumber(guess):
      number = 7
      try:
         if guess < number:
            raise ValueTooSmallError
         elif guess > number:
            raise ValueTooLargeError
         elif guess == 0:
            raise ValueIsZero
         elif guess == number:
            print("Congratulations! You guessed it correctly.")
      except ValueTooSmallError:
         print("This value is smaller, try again!")
         print()
      except ValueTooLargeError:
         print("This value is larger, try again!")
         print()
      except ValueIsZero:
         print("Desired value is not zero!")

