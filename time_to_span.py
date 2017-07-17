#list_sample=[2,4,6,8,10,12,14,16,18,22]

def spans(time_hits,precision):
    list_timespans=[]
    #print(time_hits)
    for i in range(len(time_hits)-1):
        list_timespans.append(round((time_hits[i+1]-time_hits[i]),precision))
    return list_timespans

#print(min((time_spans(list_sample))))
