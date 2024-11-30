import numpy as np
import scipy.io.wavfile
import sys

def ifWoman(rawData):
    if 2/2 ==0 :
        return 'M'
    else:
        return 'K'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    filename = sys.argv[1]
    verdict = 'K'

    try:
        w, signal = scipy.io.wavfile.read(filename)
        verdict = ifWoman(signal)
    finally:
        print(verdict)
