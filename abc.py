#!/usr/bin/env python

from midiutil.MidiFile import MIDIFile
def createMidi(filename, sentence):
	track = 0
	channel = 0
	time = 0
	duration = 1
	tempo = 60
	volume = 100
	midi = MIDIFile(1)
	midi.addTempo(track,time,tempo)
	for i in sentence:
		print(ord(i))
		midi.addNote(track,channel,ord(i)-10,time, duration, volume);
		time += 1
	with open(filename,"wb") as output_file:
		midi.writeFile(output_file);
	print("success")
if __name__=="__main__":
	import sys
	filename = sys.argv[1]
	sentence = sys.argv[2]
	createMidi(filename,sentence)

"""
MyMIDI = MIDIFile(1) # One track, defaults to format 1 (tempo track
                     # automatically created)
MyMIDI.addTempo(track,time, tempo)

for pitch in degrees:
    MyMIDI.addNote(track, channel, pitch, time, duration, volume)
    time = time + 1

with open("major-scale.mid", "wb") as output_file:
    MyMIDI.writeFile(output_file)
    """
