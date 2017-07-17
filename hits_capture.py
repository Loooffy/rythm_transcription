import time
list_time_hits=[]

def key_hits(f):
    key = input("?")
    get_time(f)
    return key

def get_time(f):
    time_hits=round(time.clock(),f)
    list_time_hits.append(time_hits)
    #print(list_time_hits)
    return list_time_hits

#print(List_time_keyprs[:])
