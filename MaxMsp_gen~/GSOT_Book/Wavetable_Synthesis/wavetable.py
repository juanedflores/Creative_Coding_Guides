import numpy as np
import scipy.io.wavfile as wav


def lerp(wave_table, index):
    truncated_index = int(np.floor(index))
    next_index = (truncated_index + 1) % wave_table.shape[0]

    next_index_weight = index - truncated_index
    truncated_index_weight = 1 - next_index_weight

    return (
        truncated_index_weight * wave_table[truncated_index]
        + next_index_weight * wave_table[next_index]
    )


def main():
    sample_rate = 44100
    f = 440
    t = 3

    wavetable_length = 64
    wave_table = np.zeros((wavetable_length,))

    for n in range(wavetable_length):
        wave_table[n] = np.sin(2 * np.pi * n / wavetable_length)

    output = np.zeros((t * sample_rate,))

    index = 0
    index_increment = f * wavetable_length / sample_rate
    print(index_increment)

    for n in range(output.shape[0]):
        # output[n] = wave_table[int(np.floor(index))]
        output[n] = lerp(wave_table, index)
        index += index_increment
        index %= wavetable_length

    output *= 0.3

    # wav.write("sine240Hz_scaled_lerp.wav", sample_rate, output.astype(np.float32))


if __name__ == "__main__":
    main()
