import time

def basic_func(x):
    if x == 0:
        return "zero"
    elif x % 2 == 0:
        return "even"
    else:
        return "odd"

starttime = time.time()
for i in range(4, 10):
    y = i + 1
    time.sleep(2)
    print("{} squared results in a(n) {} number".format(i, basic_func(y)))

print("That took {} seconds".format(time.time() - starttime))
