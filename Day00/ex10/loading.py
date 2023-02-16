import decimal
from time import sleep
from timeit import default_timer as timer


def ft_progress(listy):
    y = len(listy)
    step = y / 100
    count = step
    progress = 0
    start = 0
    timestamp = 0
    while True:
        if progress == 100:
            break
        if y == 0:
            progress = 100
        else:
            progress = round((count * 100) / y)
        if progress == 0:
            start = timer()
        end = timer()
        print("ETA: %.2fs"
              % (((end - start) * (100 - progress)) / progress)
              + f"[{progress}%][{'=' * progress}>] {int(count)}/{y} "
              + "| elapsed time"
              + " %.2f s" % (end - start), end='\r')
        count += step
        yield progress


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    sleep(0.5)
print()
print(ret)
