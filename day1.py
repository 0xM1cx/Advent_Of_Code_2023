def addEverything(calibrations):
    sum = 0
    for values in calibrations.values():
        digit = int("".join(values))
        sum += digit

    return sum


def main():
    lines = []
    with open("day1Input", "r") as f:
        for i in f:
            lines.append(i.strip())
    counter = 0
    line_calibValues = {}

    numbers = "1234567890"
    for line in lines:
        for letter in line:
            if letter in numbers:
                line_calibValues[counter] = [letter]
                break
        
        # for reading the last digit
        for i in range(-1, (0 - len(line))-1, -1):
            if line[i] in numbers:
                line_calibValues[counter].append(line[i])
                counter += 1
                break

    sum = addEverything(line_calibValues)
    print(sum)


main()

