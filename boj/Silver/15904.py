string = input()
arr = ["U", "C", "P", "C"]
pointer = 0

for s in string:
    if s == arr[pointer]:
        pointer += 1

    if pointer == 4:
        break

if pointer == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
