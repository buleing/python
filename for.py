i = 1
summary = 0
while (i < 100):
    if (i % 10 == 0):
        print(i)
        print(int(i / 10) * 5 * "*")
    summary = summary + i
    i = i + 1

print(summary)
