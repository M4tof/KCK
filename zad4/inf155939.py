import numpy as np
import scipy.io.wavfile
import sys

unsureCutOff = 170
maleRange = [85, 180]
femaleRange = [165, 255]

def normalize(signal):
    return signal / np.max(np.abs(signal))

def apply_window(signal):
    beta = 14
    window = np.kaiser(len(signal),beta) #0
    return signal * window

def preprocess(signal, sample_rate):
    # If stereo, convert to mono
    if len(signal.shape) > 1:
        signal = np.mean(signal, axis=1)
    signal = normalize(signal)
    signal = apply_window(signal)
    return signal

def cepstral(signal):
    spectrum = np.fft.fft(signal)
    log_spectrum = np.log(np.abs(spectrum) + 1e-10)
    cepstrum = np.fft.fft(log_spectrum).real
    return cepstrum

def findFrequency(cepstrum, sampleRate):
    minimum = maleRange[0]
    maximum = femaleRange[1]
    min_quefrency = int(sampleRate / maximum)
    max_quefrency = int(sampleRate / minimum)

    relevant = cepstrum[min_quefrency:max_quefrency]
    peak = np.argmax(relevant) + min_quefrency

    found_frequency = sampleRate / peak
    return found_frequency

def ifWoman(rawData, sampleRate):

    cepstrumData = cepstral(rawData)
    fr = findFrequency(cepstrumData, sampleRate)

    if fr <= unsureCutOff:
        return 'M'

    return 'K'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    filename = sys.argv[1]

    verdict = 'K'

    try:
        rate, signal = scipy.io.wavfile.read(filename)
        signal = preprocess(signal, rate)
        verdict = ifWoman(signal, rate)
    finally:
        print(verdict)
