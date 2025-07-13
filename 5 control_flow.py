#Control Flows in Loops using[For loop]
# break example
for i in range(1, 10):
    if i == 5:
        break
    print("Break example value:", i)

# continue example
for i in range(1, 6):
    if i == 3:
        continue
    print("Continue example value:", i)

# pass example
for i in range(1, 4):
    if i == 2:
        pass
    print("Pass example value:", i)
