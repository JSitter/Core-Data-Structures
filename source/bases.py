#!python

import string
import math

# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""

    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # TODO: Decode digits from binary (base 2)

    if base == 2:
        accumulator = 0
        stop = len(digits)
        for x in range(0,stop):
            inc = 2 ** x
            accumulator += inc * int(digits[-1 - x])

    # TODO: Decode digits from hexadecimal (base 16)
    if base == 16:

        accumulator = 0
        stop = len(digits)
        multiplier = 0
        for x in range(0, stop):
            inc = 16 ** x
            if digits[-1 - x].isalpha():
                multiplier = int(ord(digits[-1 - x].lower()) - 87)
            else:
                multiplier = int(digits[-1 - x])

            accumulator += inc * multiplier

    # TODO: Decode digits from any base (2 up to 36)
    else:
        accumulator = 0
        stop = len(digits)
        multiplier = 0
        for x in range(0,stop):
            inc = base ** x

            if digits[-1 - x].isalpha():
                multiplier = int(ord(digits[-1 - x].lower()) - 87)
            else:
                multiplier = int(digits[-1 - x])

            accumulator += inc * multiplier
            

    return accumulator

def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    encoded = ""

    if number == 0:
        return 0

    # TODO: Encode number in binary (base 2)
    
    #Get exponent to start
    exponent = str( math.log(number, base)).split('.')
    accumulator = 0
    
    print("Exponent", exponent[0])

    #loop until accumulator equals number
    remainder = number

    if base ==2:
        for x in range(int(exponent[0]), 0, -1):
            cur_power = base ** x
            if accumulator + cur_power <= number:
                encoded += "1"
                accumulator += cur_power
            else:
                encoded += "0"

    # TODO: Encode number in hexadecimal (base 16)
    if number == 16:
       for x in range(int(exponent[0])): 
           pass
    # TODO: Encode number in any base (2 up to 36)

    return encoded
    


def convert(digits, base1, base2):
    """Convert given digits in base1 to digits in base2.
    digits: str -- string representation of number (in base1)
    base1: int -- base of given number
    base2: int -- base to convert to
    return: str -- string representation of number (in base2)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base1 <= 36, 'base1 is out of range: {}'.format(base1)
    assert 2 <= base2 <= 36, 'base2 is out of range: {}'.format(base2)
    # TODO: Convert digits from base 2 to base 16 (and vice versa)
    # 
    # TODO: Convert digits from base 2 to base 10 (and vice versa)
    # ...
    # TODO: Convert digits from base 10 to base 16 (and vice versa)
    # ...
    # TODO: Convert digits from any base to any base (2 up to 36)
    # ...


def main():
    """Read command-line arguments and convert given digits between bases."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 3:
        digits = args[0]
        base1 = int(args[1])
        base2 = int(args[2])
        # Convert given digits between bases
        result = convert(digits, base1, base2)
        print('{} in base {} is {} in base {}'.format(digits, base1, result, base2))
    else:
        print('Usage: {} digits base1 base2'.format(sys.argv[0]))
        print('Converts digits from base1 to base2')


if __name__ == '__main__':
    main()
