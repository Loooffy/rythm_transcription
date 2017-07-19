from hits_capture import *
from time_to_span import *
from plot_the_notes import *

while key_hits(4)=="":
        pass

print("time_hits:", list_time_hits)
list_timespans=spans(list_time_hits,4)
print("tima_spans:", list_timespans)

min=min(list_timespans)
list_beatspans=[1]

for t in list_timespans:
    list_beatspans.append(int(t/min))

print(list_beatspans)
plot_the_notes(list_beatspans[0:-1])
