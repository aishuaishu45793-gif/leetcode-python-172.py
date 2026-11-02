numbers = list(map(int, input("Enter numbers: ").split()))

unique_numbers = sorted(set(numbers))

if len(unique_numbers) >= 2:
    print("Second smallest number:", unique_numbers[1])
else:
    print("Second smallest number does not exist.")