import time

def uptoN(n):
    total = 0
    for i in range(n + 1):
        total += i
    print(f"for n={n}, total={total}")
    return total

start_time = time.time()
print("Start time:", start_time)
uptoN(100000)
end_time = time.time()
print("End time:", end_time)
diff = end_time - start_time
print("Diff:", diff)
