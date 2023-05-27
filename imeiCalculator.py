###########################################################################
#                                                                         #
#   Name:        imeiCalculator.py                                        #
#   Purpose:     Display the 15th digit of an IMEI using Luhn algorithm   #
#                                                                         #
#   Author:      Seb2lyon                                                 #
#                                                                         #
#   Created:     01/05/2023                                               #
#   Version:     2023.05                                                  #
#   Licence:     GNU General Public License v3.0                          #
#                                                                         #
###########################################################################

import sys
import argparse

#----------------------------#

# FUNCTIONS

# User's input verification : must be 14 digits (and nothing else)
def inputVerification(user_input):
    if len(user_input) != 14 or not user_input.isdigit():
        sys.exit("Error...\nYou need to provide the 14 first digits of an IMEI.\nSee 'help' page for more details.")
    else:
        return user_input

# The Luhn algorithm calculation to obtain the exact key (IMEI's 15th number)
def luhnAlgorithm(imei):
    odd_list = []
    even_list = []
    i = 13
    j = 12

    # Loop on the evens numbers (number * 2 -> if the result is > 9 => result - 9)
    while i >=0:
        even = int(imei[i]) * 2
        if even > 9:
            even = even - 9

        # Add the result in the list of evens numbers
        even_list.append(even)
        i = i - 2

    # Loop on the odds numbers
    while j >= 0:
        odd = int(imei[j])

        # Add the number in the list od odds numbers
        odd_list.append(odd)
        j = j - 2

    # Calculate the sum of all the numbers in the 2 lists
    total = sum(even_list) + sum(odd_list)

    for n in range(0,10):

        # Calculate the sum + the Luhn key. Result divided by 10 must produce a modulo at 0
        if (total+n)%10 != 0:

            # Print all the possible numbers with match result (only if verbose mode is enable) ---> Number didn't match (modulo is not 0)
            if args.verbose:
                print("Luhn key = " + str(n) + " ---> no match")
        else:

            # Print all the possible numbers with match result (only if verbose mode is enable) ---> Number match (modulo is 0)
            if args.verbose:
                print("Luhn key = " + str(n) + " ---> MATCH !!")

            # Matched number is the Luhn key
            key = n

    return key

#----------------------------#

# MAIN CODE

# Arguments parser + create the "help" instructions
parser = argparse.ArgumentParser(description="This script is made to find and display the 15th digit of an IMEI.", epilog="imeiCalculator - version 2023.05 (GNU General Public License v3.0) - Seb2lyon")
parser.add_argument("imei", help="provide the 14 first digits of an IMEI.")
parser.add_argument("-v", "--verbose", action='store_true', help="display the analysis of the Luhn algorithm.")

args=parser.parse_args()

# User's input verification : must be 14 digits (and nothing else)
verifiedInput = inputVerification(args.imei)

# The Luhn algorithm calculation to obtain the exact key (IMEI's 15th number)
key = luhnAlgorithm(verifiedInput)

# Display the key found and the complete IMEI number
print("\nThe 15th IMEI digit is : " + str(key) + "\nThe complete IMEI number is : " + verifiedInput + str(key))
