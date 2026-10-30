import time
from multiprocessing import Pool

def basic_func(x):
    if x == 0:
        return "zero"
    elif x % 2 == 0:
        return "even"
    else:
        return "odd"

def calc_square(i):
    y = i + 1
    time.sleep(2)
    print("{} squared results in a(n) {} number".format(i, basic_func(y)))

if __name__ == "__main__":
    starttime = time.time()
    p = Pool()
    p.map(calc_square, range(4, 10))
    p.close()
    p.join()
    print("That took {} seconds".format(time.time() - starttime))
