import time
list_time_hits=[]

def key_hits(precision):
    key = input()
    get_time(key,precision)
    return key

def get_time(key,precision):
    if key=="":
        time_hits=round(time.clock(),precision)
        list_time_hits.append(time_hits)
    else:
        pass
