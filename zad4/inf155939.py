import numpy as np
import scipy.io.wavfile
import sys

maleRange = [85,180]
femaleRange = [165,255]

def cepstral(signal):
    spectrum = np.fft.fft(signal)
    log_spectrum = np.log(np.abs(spectrum) + 1e-10)
    cepstrum = np.fft.fft(log_spectrum).real
    return cepstrum

def findFrequency(cepstrum,sampleRate):
    minimum = maleRange[0]
    maximum = femaleRange[1]
    min_quefrency = int(sampleRate / maximum)
    max_quefrency = int(sampleRate / minimum)

    relevant = cepstrum[min_quefrency:max_quefrency]
    peak = np.argmax(relevant) + min_quefrency

    found_frequency = sampleRate / peak
    return found_frequency

def ifWoman(rawData,sampleRate):
    Male = False
    Female = False

    cepstrumData = cepstral(rawData)

    fr = findFrequency(cepstrumData,sampleRate)

    if maleRange[0] <= fr <= maleRange[1]:
        Male = True
    elif femaleRange[0] <= fr <= femaleRange[1]:
        Female = True
    
    if Female:
        return 'K'
    elif Male:
        return 'M'
    else:
        return 'M'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    filename = sys.argv[1]
    
    verdict = 'K'

    try:
        rate, signal = scipy.io.wavfile.read(filename)
        verdict = ifWoman(signal,rate)
    finally:
        print(verdict)
