arr = [3, 2, 0, -4]
seen = set()
i = 0
while i < len(arr):
    if i in seen:
        print("cycle!")
        break
    seen.add(i)
    i = arr[i]  # simulating pointer jumps