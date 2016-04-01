import hashlib
import threading
import sys
import time

prefix = 'iwrupvqb'

stopped = False

def dohash(suffix_start, num_threads):
    print "starting thread", suffix_start
    global stopped
    suffix = suffix_start

    while not stopped:
        m = hashlib.md5()
        m.update(prefix + str(suffix))

        if m.hexdigest()[0:6] == '000000':
            print suffix
            stopped = True
            break

        suffix += num_threads

    print "stopping thread", suffix_start

num_threads = 10

threads = []

for n in range(1, num_threads+1):
    t = threading.Thread(target=dohash, args=(n, num_threads))
    t.daemon = True
    t.start()
    threads.append(t)


try:
    for t in threads: t.join()
    time.sleep(100)
except (KeyboardInterrupt, SystemExit):
    print '\n! Received keyboard interrupt, quitting threads.\n'
    stopped = True
    sys.exit()
