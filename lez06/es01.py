import os
import aa_soundfile as sf

files = os.listdir()

for f in files:
    print(f)
    s = os.path.splitext(f)
    if s[1] == '.aif' or s[1] == '.aiff':
        n = s[0] + '-6dB'
        snd, meta = sf.read(f)
        soft = snd / 2
        sr = meta['sr']
        sf.write(soft, n + '.aif', sr)



