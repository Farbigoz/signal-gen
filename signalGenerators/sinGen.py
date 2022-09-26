import math
import numpy


class SinusGenerator:
    def __init__(self, samplerate: int):
        self.samplerate = samplerate

        self.freq = 0.0
        self.amp = 0.0

        self.x = 0

    def setFreq(self, freq: float):
        if freq > 0.0:
            self.freq = freq
        else:
            self.freq = 0.0

    def setAmp(self, amp: float):
        if amp > 1.0:
            self.amp = 1.0
        elif amp < 0.0:
            self.amp = 0.0
        else:
            self.amp = amp

    def resetX(self):
        self.x = 0

    def gen(self, sampleCount: int):
        if self.freq == 0 or self.amp == 0:
            out = numpy.zeros(sampleCount)

        else:
            omega = float(self.freq) * (math.pi * 2) / self.samplerate

            xs = numpy.arange(self.x, self.x + sampleCount)
            out = self.amp * numpy.sin(xs * omega)

            self.x += sampleCount

            # Сброс угла в 0, чтобы не хранить большие цифры
            if self.x > 0xffffffff:
                self.x = 0

        return out

    def genClear(self, sampleCount: int):
        dumpX = self.x
        self.x = 0
        out = self.gen(sampleCount)
        self.x = dumpX

        return out
