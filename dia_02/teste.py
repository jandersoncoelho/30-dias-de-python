from mido import MidiFile

mid = MidiFile('drum.mid')

for x in mid:
    print(x)

