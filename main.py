from hits_capture import *
from time_to_span import *

while key_hits(4)=="":
        pass

print("time_hits:", list_time_hits)
list_timespans=spans(list_time_hits,4)
print("tima_spans:", list_timespans)

min=min(list_timespans)
rythm_raw=[]

for t in list_timespans:
    rythm_raw.append(int(t/min))

print(rythm_raw)
