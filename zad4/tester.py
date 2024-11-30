import os
import subprocess

def test_wav_files(folder_path, script_name):
    """
    Tests the infXYZ.py script against .wav files in the given folder.
    Assumes filenames contain the expected result, e.g., '123_K.wav' or '456_M.wav'.
    
    Args:
        folder_path (str): Path to the folder containing the .wav files.
        script_name (str): Name of the Python script to run, e.g., 'inf123456.py'.

    Returns:
        None
    """
    # Get all .wav files in the folder
    wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    
    total_files = len(wav_files)
    correct = 0
    incorrect = 0
    error = 0

    for wav_file in wav_files:
        # Extract the expected output (last character before '.wav')
        expected_output = wav_file.split('_')[-1][0]

        # Construct the command to run the script
        cmd = ['python', script_name, os.path.join(folder_path, wav_file)]

        try:
            # Run the script and capture its output
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
            actual_output = result.stdout.strip()

            # Compare the script's output with the expected result
            if actual_output == expected_output:
                correct += 1
                print(f"PASSED: {wav_file} -> Expected: {expected_output}, Got: {actual_output}")
            else:
                incorrect += 1
                print(f"FAILED: {wav_file} -> Expected: {expected_output}, Got: {actual_output}")
        except subprocess.CalledProcessError as e:
            error += 1
            print(f"ERROR: {wav_file} -> Could not execute script. Error: {e}")

    print("\nTesting Summary:")
    print(f"Total Files Tested: {total_files}")
    print(f"Correctly Classified: {correct}")
    print(f"Incorrectly Classified: {incorrect}")
    print(f"Not Classified: {error}")
    print("\n Precentage: ",  round(correct/total_files,2) * 100,"%")

# Example usage:
test_wav_files('./train', 'inf155939.py')
