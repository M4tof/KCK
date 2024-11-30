import numpy as np
import scipy.io.wavfile
import sys



if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(1)

    filename = sys.argv[1]

    try:
        w, signal = scipy.io.wavfile.read(filename)


    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

    except Exception as e:
        print(f"An error occurred: {e}")
