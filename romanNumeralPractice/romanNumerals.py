

def roman():
    while True:
        print("\nEnter a number in Roman numerals or enter q to quit.")
        numerals = input().upper()

        if numerals == "Q" or numerals == "QUIT":       #Leave program
            break


        # Check for numbers
        if not numerals.isalpha():
            print("Error: Decimal number found, please try again.")


        else:
            constNumerals = ["I", "V", "X", "L", "C", "D", "M"]
            constValues = [1, 5, 10, 50, 100, 500, 1000]

            isNumeral = True
            validOrder = True
            index = 0
            total = 0
            for currentNumeral in numerals:

                # Check if all characters are letters of roman numerals

                if currentNumeral not in constNumerals:
                    isNumeral = False
                    break
                else:
                    # Check if the order of the numerals makes sense
                    #

                    constIndex = constNumerals.index(currentNumeral)         #Get the index of x in the constNumerals


                    if index != len(numerals) - 1:
                        nextConstIndex = constNumerals.index(numerals[index + 1])

                        # Check if the numeral following the current one is not larger than two numerals up
                        if constIndex + 2 < nextConstIndex:
                            validOrder = False
                            break
                        elif constIndex < nextConstIndex and constIndex % 2 != 0:               #no VX or LC etc.
                            validOrder = False
                            break
                        elif index != 0 and currentNumeral >= numerals[index - 1] and nextConstIndex > constIndex:       #no IIV or IIX or IXL, etc.
                            validOrder = False
                            break
                        elif currentNumeral == numerals[index + 1]:
                            if constIndex % 2 != 0:     #no VV or LL or DD
                                validOrder = False
                                break
                            elif (index <= len(numerals) - 4 and currentNumeral == numerals[index + 2] and
                                    currentNumeral == numerals[index + 3]):          #no IIII or XXXX etc.
                                validOrder = False
                                break
                            else:
                                total += constValues[constIndex]
                        else:
                            if constIndex < nextConstIndex:
                                total -= constValues[constIndex]
                            else:
                                total += constValues[constIndex]
                    else:
                        total += constValues[constIndex]
                index += 1

            # End "for currentNumeral in numerals" loop

            if not isNumeral:
                print("Error: Non-Roman numeral found, please try again.")
            elif not validOrder:
                print("Error: The Roman numerals are not in a valid order, please try again.")
            else:
                print(total)
    # End while True loop

# ******************************* END roman function *******************************








if __name__ == '__main__':
    roman()



