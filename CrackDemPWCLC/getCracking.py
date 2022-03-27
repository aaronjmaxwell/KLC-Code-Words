"""Set up the Cracking Codes.

@author: Bilal Qadar
@organization: Canada Learning Code
"""
__author__ = "AJMax"
__version__ = "1.0.0"
import random
from datetime import datetime
from .getCommonWords import fetchWords

treasure = fetchWords()


def bruteForce(pword, method=0):
    """A brute force method for randomly guessing passwords.

    :arg pword: the password to be forced :type str

    :param method: the character range to use :type int

    :return t: time to crack :type datetime.timedelta
    """
    # We only set the seed because we want timing to be repeatable.
    random.seed(sum(map(ord, "CLC")))
    if method == 0:
        # The ASCII range for only the ten numbers.
        i, j = 48, 58
    elif method == 1:
        # The ASCII range for only uppercase letters.
        i, j = 65, 91
    elif method == 2:
        # The ASCII range for only lowercase letters.
        i, j = 97, 123
    elif method == 3:
        # TODO figure out a mix of upper and lowercase letters.
        i, j = None, None
    else:
        # Use all ASCII characters.
        i, j = 33, 127

    # We use a simple loop to generate random characters. We could also cycle but we want to make
    # this easy, so we cheat because the length of the password known.
    cracked, t, q, k = False, datetime.now(), datetime.now(), 0
    while not cracked:
        k += 1
        guess = "".join([chr(random.randrange(i, j, 1)) for _ in range(len(pword))])
        if guess == pword:
            cracked = True
            t = datetime.now() - t
        else:
            if (datetime.now() - q).total_seconds() >= 10:
                print("{:0f} seconds, {} guesses so far ...".format((datetime.now() - t).total_seconds(), k))
                q = datetime.now()

    return "Cheap brute force cracked password {} in {} using {} guesses!".format(pword, t, k)


def dictionAttack(pword):
    """Use the dictionary fetched from the internet.

    :arg pword: the password to be forced :type str

    :return t: time to crack :type datetime.timedelta
    """
    # Start yer engines.
    t = datetime.now()
    for guess in treasure:
        # For some reason Bilal strips out whitespace.
        if guess.strip(" ") == pword:
            t = datetime.now() - t
            return "Dictionary attack cracked password {} in {}!".format(pword, t)
    return "Dictionary of {} did not contain password {}! Only takes {} for all tries!".format(
            len(treasure), pword, datetime.now() - t)


def attack(password):
    if password.isdigit():
        return bruteForce(password, method=0)
    else:
        return dictionAttack(password)
#    if password.isascii():
#        if password.isalnum():
#            if password.isdigit():
#                return bruteForce(password, method=0)
#            elif password.isupper():
#                return bruteForce(password, method=1)
#            elif password.islower():
#                return bruteForce(password, method=2)
#            else:
#                return "Cracker not implemented yet."
#        else:
#            return bruteForce(password, method=4)
#    else:
#        return "Password not made of ASCII - cannot crack at this time."
