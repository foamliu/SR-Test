import os
import time

import librosa
import soundfile

filename = 'test.mp3'
print('loading {}...'.format(filename))
start = time.time()
y, sr = librosa.load(filename, mono=True)
print('elapsed {} sec'.format(time.time() - start))

print('y.shape: ' + str(y.shape))
print('sr: ' + str(sr))
duration = librosa.get_duration(y, sr)
print('duration: ' + str(duration))
print('{:.4f} hours'.format(duration / 3600))

print('splitting...')
start = time.time()
intervals = librosa.effects.split(y, top_db=60)
print('elapsed {} sec'.format(time.time() - start))

print('intervals.shape: ' + str(intervals.shape))
# print(intervals)

print('saving...')
start = time.time()
for i, inter in enumerate(intervals):
    yt = y[inter[0]:inter[1]]
    filename = os.path.join('audios', 'clip_{}.wav'.format(i))
    soundfile.write(filename, yt, samplerate=sr)
print('elapsed {} sec'.format(time.time() - start))
print('done')
