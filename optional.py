import os
def save_epoch(my_epoch):
    f = open("latest_epoch.txt", "w")
    f.write(str(my_epoch))
    f.close()

def load_epoch(filename):
    f = open(filename, "r")
    line = f.readline()
    print("line : ", line)
    cnt = (int)(line.strip())
    print("cnt : ", cnt)
    return cnt