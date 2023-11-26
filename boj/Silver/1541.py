s = input()

minus = list(s.split("-"))
acc = 0
for m in minus:
    acc -= sum(map(int, m.split("+")))

acc += sum(map(int, minus[0].split("+"))) * 2

print(acc)