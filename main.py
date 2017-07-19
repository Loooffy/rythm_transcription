from hits_capture import *
from time_to_span import *
from plot_the_notes import *

while key_hits(4)=="":
        pass

print("time_hits:", list_time_hits)
list_timespans=spans(list_time_hits,4)
print("tima_spans:", list_timespans)

min=min(list_timespans)
rhythm_raw=[0]

for t in list_timespans:
    rhythm_raw.append(int(t/min))

print(rhythm_raw)
plot_the_notes(rhythm_raw)
