constNumerals = ["I", "V", "X", "L", "C", "D", "M"]
constValues = [1, 5, 10, 50, 100, 500, 1000]


def roman(inputString):
    ecNotNumeral = "Error: Non-Roman numeral found, please try again."
    ecNonValidOrder = "Error: The Roman numerals are not in a valid order, please try again."
    index = 0
    total = 0
    for currentNumeral in inputString:

        # Check if all characters are letters of roman numerals

        if currentNumeral not in constNumerals:
            return ecNotNumeral
        else:
            # Check if the order of the numerals makes sense

            constIndex = constNumerals.index(currentNumeral)  # Get the index of x in the constNumerals

            if index != len(inputString) - 1:
                nextConstIndex = constNumerals.index(inputString[index + 1])

                # Check if the numeral following the current one is not larger than two numerals up
                if constIndex + 2 < nextConstIndex:
                    return ecNonValidOrder

                elif constIndex < nextConstIndex and constIndex % 2 != 0:  # no VX or LC etc.
                    return ecNonValidOrder

                elif (index != 0 and constIndex >= constNumerals.index(inputString[index - 1])
                      and nextConstIndex > constIndex):  # no IIV or IIX or IXL, etc.
                    return ecNonValidOrder
                elif currentNumeral == inputString[index + 1]:
                    if constIndex % 2 != 0:  # no VV or LL or DD
                        return ecNonValidOrder

                    elif (index <= len(inputString) - 4 and currentNumeral == inputString[index + 2] and
                          currentNumeral == inputString[index + 3]):  # no IIII or XXXX etc.
                        return ecNonValidOrder

                    else:
                        total += constValues[constIndex]
                else:
                    if constIndex < nextConstIndex:
                        total -= constValues[constIndex]
                    else:
                        total += constValues[constIndex]
            elif constIndex % 2 != 0 and index > 1 and constIndex >= constNumerals.index(inputString[index - 2]): #No IXV or XCL
                    return ecNonValidOrder
            else:
                total += constValues[constIndex]
        index += 1

    # End "for currentNumeral in numerals" loop
    return total


# ******************************* END roman function *******************************


def decimal(inputString):
    # Error Codes:
    ecNonInt = "Error: Non-integer found, please try again."
    ecNotInRange = "Error: Enter a valid integer between 1 and 3999."

    # Check for int
    try:
        inputInt = int(inputString)
    except TypeError:
        return ecNonInt

    # check for between 1 and 3999
    if inputInt < 1 or inputInt > 3999:
        return ecNotInRange

    # Go by each decimal place and calculate the roman numeral(s) based on that
    decimalPlace = 0
    final = ""
    for dec in reversed(inputString):
        newNumeral = ""
        dec = int(dec)  # Could throw error, but shouldn't since checked earlier
        if dec <= 3:
            newNumeral = dec * constNumerals[2 * decimalPlace]
        elif dec == 4:
            newNumeral = constNumerals[2 * decimalPlace] + constNumerals[(2 * decimalPlace) + 1]
        elif dec == 5:
            newNumeral = constNumerals[(2 * decimalPlace) + 1]
        elif dec <= 8:
            newNumeral = constNumerals[(2 * decimalPlace) + 1] + constNumerals[2 * decimalPlace] * (dec - 5)
        elif dec == 9:
            newNumeral = constNumerals[2 * decimalPlace] + constNumerals[2 * decimalPlace + 2]
        # if dec == 0, keep newNumeral as ""

        final = newNumeral + final
        decimalPlace += 1

    return final


# ******************************* END decimal function *******************************


if __name__ == '__main__':

    while True:
        print("\nEnter a valid Roman Numeral or Integer from 1 to 3999 or enter q to quit.")
        newInput = input().upper()

        if newInput == "Q" or newInput == "QUIT":  # Leave program
            break

        if newInput.isalpha():
            print(roman(newInput))
        elif newInput.isdecimal():
            print(decimal(newInput))
        else:
            print("Error: Neither Roman Numeral or Integer entered")
