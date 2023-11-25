import wave
import numpy as np

def write_unit_impulse(filename, duration, sample_rate):
    """
    Creates a unit impulse signal and writes it to a WAV file.

    :param filename: The name of the output WAV file.
    :param duration: The duration of the signal in seconds.
    :param sample_rate: The sample rate of the audio signal.
    """
    # Number of samples
    num_samples = int(duration * sample_rate)

    # Generate a unit impulse signal (all zeros except for the first sample)
    signal = np.zeros(num_samples)
    signal[0] = 1.0  # Setting the first sample to 1

    # Ensure signal is in 16-bit format
    signal = np.int16(signal * 32767)

    # Open a WAV file for writing
    with wave.open(filename, 'w') as wav_file:
        # Set parameters: 1 channel (mono), 2 bytes per sample, sample rate, number of samples
        wav_file.setparams((1, 2, sample_rate, num_samples, 'NONE', 'not compressed'))

        # Write the signal to the WAV file
        wav_file.writeframes(signal.tobytes())

if __name__ == "__main__":
    write_unit_impulse("unit_impulse.wav", 1, 44100)

