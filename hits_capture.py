import time
list_time_hits=[]

def key_hits(precision):
    key = input("?")
    get_time(precision)
    return key

def get_time(precision):
    time_hits=round(time.clock(),precision)
    list_time_hits.append(time_hits)
    #print(list_time_hits)
    return list_time_hits

#print(List_time_keyprs[:])
