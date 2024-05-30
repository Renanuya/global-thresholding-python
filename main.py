import numpy as np

histogram = {
    100: 12, 101: 18, 102: 32, 103: 48, 104: 52, 105: 65, 106: 55, 107: 42,
    108: 32, 109: 16, 110: 10, 140: 5, 141: 18, 142: 25, 143: 32, 144: 40,
    145: 65, 146: 43, 147: 32, 148: 20, 149: 10, 150: 4
}

intensities = np.array(list(histogram.keys()))
pixel_counts = np.array(list(histogram.values()))

T0 = 100
threshold = 1

while True:

    G1 = intensities[intensities > T0]
    G2 = intensities[intensities <= T0]

    m1 = np.sum(G1 * pixel_counts[intensities > T0]) / np.sum(pixel_counts[intensities > T0])
    m2 = np.sum(G2 * pixel_counts[intensities <= T0]) / np.sum(pixel_counts[intensities <= T0])

    T1 = (m1 + m2) / 2

    if abs(T1 - T0) < threshold:
        break

    T0 = T1

optimum_threshold = T1
print(f"Optimum Threshold Value: {optimum_threshold}")
