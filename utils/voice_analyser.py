# import os
# import struct
# import sys
# import time
#
# import pyaudio
# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib.animation import FuncAnimation
#
# CHUNK = 1024 * 4
# RATE = 44100
# FORMAT = pyaudio.paInt16
# CHANNELS = 1
#
# p = pyaudio.PyAudio()
#
# stream = p.open(
#     format=FORMAT,
#     rate=RATE,
#     channels=1,
#     frames_per_buffer=CHUNK,
#     input=True
# )
#
#
# fig, ax = plt.subplots()
# line, = ax.plot(1, 100)
#
# while True:
#     data = np.frombuffer(stream.read(CHUNK), dtype=np.int16)
#     print('#' + '#' * int(np.average(data)))
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
