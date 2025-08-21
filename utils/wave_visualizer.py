import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import sounddevice as sd
import numpy as np
import threading
import matplotlib.pyplot as plt
import librosa
import librosa.display
import soundfile as sf
import io


class WaveformVisualizer:
    def __init__(self, parent_frame, duration=5, rate=44100):
        self.duration = duration
        self.rate = rate
        self.running = False
        self.fig = Figure(figsize=(5.5, 2), dpi=100)
        self.ax = self.fig.add_subplot(111)
        self.line, = self.ax.plot([], [])
        self.ax.set_ylim(-1, 1)
        self.ax.set_xlim(0, 1024)
        self.ax.axis('off')

        self.canvas = FigureCanvasTkAgg(self.fig, master=parent_frame)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack()

    def update_plot(self, data):
        self.line.set_ydata(data)
        self.line.set_xdata(np.arange(len(data)))
        self.canvas.draw()

    def audio_callback(self, indata, frames, time, status):
        if self.running:
            volume_norm = indata[:, 0]
            self.update_plot(volume_norm)

    def start(self):
        self.running = True
        self.stream = sd.InputStream(callback=self.audio_callback, channels=1, samplerate=self.rate, blocksize=1024)
        self.stream.start()

    def stop(self):
        self.running = False
        if hasattr(self, 'stream'):
            self.stream.stop()
            self.stream.close()


# ✅ Function outside the class now
def display_waveform(audio_path, title="Waveform"):
    y, sr = librosa.load(audio_path)
    plt.figure(figsize=(10, 3))
    librosa.display.waveshow(y, sr=sr)
    plt.title(title)
    plt.tight_layout()

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close()
    buf.seek(0)
    return buf

#########################################################################################

# utils/wave_visualizer.py
