n = [64, 74, 57, 90] # note MIDI: mi, re, sol, fa#
# voglio riordinarle in ordine di pitch class
# -> [74, 64, 90, 57]: re, mi, fa#, sol
"""
def midi2pitch(m):
    return m % 12

n.sort(key = midi2pitch)
print(n)
"""

n.sort(key = lambda x: x % 12)
print(n)

