from math import gcd

def calculate_result(command, numbers):
    if command == "sum":
        return sum(numbers)
    elif command == "average":
        result = sum(numbers) / len(numbers)
        return round(result, 2)
    elif command == "min":
        return min(numbers)
    elif command == "max":
        return max(numbers)
    elif command == "gcd":
        result = gcd(numbers[0], numbers[1])
        for i in range(2, len(numbers)):
            result = gcd(result, numbers[i])
        return result
    elif command == "lcd":
        result = numbers[0]
        for i in range(1, len(numbers)):
            result = (result * numbers[i]) // gcd(result, numbers[i])
        return result

while True:
    line = input()
    if line == "end":
        break
    elif line in ["sum", "average", "min", "max", "gcd", "lcd"]:
        numbers = []
        while True:
            user_number = input()
            if user_number == "end":
                break
            numbers.append(int(user_number))
        result = calculate_result(line, numbers)
        print(result)
    else:
        print("Invalid command")
        break
