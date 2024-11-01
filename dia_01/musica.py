@swim(snap=8, until=2)
def pluck(p=1, i=0):
    N('A4 G4', i=i, chan=2, dur=.4)
    again(pluck, p=.5, i=i + 1)
@swim(snap=1)
def bass(p=1, i=0):
    N('D1!4 A1!4 G1!4 ....', i=i, chan=1, dur=.4)
    again(bass, p=.5, i=i + 1)
@swim(snap=1)
def base(p=1, i=0):
    N('C1 C1 C1 .', i=i)
    N('C3 A2 C3 .', i=i)
    again(base, p=2, i=i + 1)
@swim(until=3)
def intro(p=1, i=0):
    N('A1 G1 C1', i=i)
    again(intro, p=1/8, i=i + 1)
clock.tempo = 80
