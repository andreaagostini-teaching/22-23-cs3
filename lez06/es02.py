import librosa
import aa_soundfile as sf

snd, meta = sf.read('chopin.aif')
y = sf.flat(snd)
sr = meta['sr']

tempo, beat_frames = librosa.beat.beat_track(y = y, sr = sr)
beat_samps = librosa.frames_to_samples(beat_frames)

print(beat_samps)

start = 0
cnt = 1

for p in beat_samps:
    segm = y[start:p]
    start = p
    n = f'out{cnt}.aif'
    print('scrivo', n, 'da', start, 'a', p)
    sf.write(segm, n, sr)
    cnt += 1






