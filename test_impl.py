import time
from Test import MyHTMLParser


CNT_LIMIT = 1000
DURATION_LIMIT = 1000
SITE = "http://python.org"


def count_case():
    start = time.time()
    for _ in range(CNT_LIMIT):
        MyHTMLParser(SITE)
    end = time.time()
    duration = end - start
    mean_time = duration / CNT_LIMIT
    return duration, mean_time

print("Stress-test for count-based case")
duration, mean_time = count_case()
print("\tTotal time: " + str(duration))
print("\tMean time: " + str(mean_time))


def time_case():
    start = time.time()
    limit = start + DURATION_LIMIT
    cnt = 0
    while True:
        MyHTMLParser(SITE)
        if (time.time() <= limit):
            cnt += 1
        else:
            break
    end = time.time()
    mean_time = DURATION_LIMIT / cnt
    return cnt, mean_time

print("Stress-test for time-based case")
cnt, mean_time = time_case()
print("\tTest counts: " + str(cnt))
print("\tMean time: " + str(mean_time))

