import random

random.seed(42)

def random_dna(length):
    return ''.join(random.choice("ATCG") for _ in range(length))


def reverse_complement(sequence):
    complement = str.maketrans("ATCG", "TAGC")
    return sequence.translate(complement)[::-1]


left_tirs = [
    "TGTTACCG",
    "AAGCTTGA",
    "CCGTAAGT",
    "GATCCGTA"
]

tsds = ["GAC", "TTA", "CGG", "ATA"]

dna_parts = [random_dna(20)]

for i in range(4):
    left_tir = left_tirs[i]
    right_tir = reverse_complement(left_tir)
    internal_region = random_dna(24)

    transposon = left_tir + internal_region + right_tir

    dna_parts.append(tsds[i])
    dna_parts.append(transposon)
    dna_parts.append(tsds[i])

    if i < 3:
        dna_parts.append(random_dna(20))

dna_parts.append(random_dna(20))

dna_sequence = ''.join(dna_parts)

print("DNA sequence:", dna_sequence)
print("DNA length:", len(dna_sequence), "bp")


def detect_transposons(dna, tir_length=8,
                       min_internal=20, max_internal=30,
                       tsd_length=3):

    results = []

    for left_start in range(len(dna)):

        left_tir = dna[left_start:left_start + tir_length]
        right_tir = reverse_complement(left_tir)

        for internal_length in range(min_internal,
                                     max_internal + 1):

            right_start = left_start + tir_length + internal_length
            right_end = right_start + tir_length

            if right_end > len(dna):
                continue

            if dna[right_start:right_end] != right_tir:
                continue

            if left_start < tsd_length:
                continue

            if right_end + tsd_length > len(dna):
                continue

            left_tsd = dna[left_start-tsd_length:left_start]
            right_tsd = dna[right_end:right_end+tsd_length]

            if left_tsd == right_tsd:

                results.append({
                    "Start": left_start + 1,
                    "End": right_end,
                    "Length": right_end - left_start,
                    "Left_TIR": left_tir,
                    "Right_TIR": right_tir,
                    "TSD": left_tsd
                })

    return results


results = detect_transposons(dna_sequence)

print("\nDetected transposable elements:")
print("Element\tStart\tEnd\tLength\tTSD")

for i, result in enumerate(results, 1):
    print(
        f"TE{i}\t"
        f"{result['Start']}\t"
        f"{result['End']}\t"
        f"{result['Length']}\t"
        f"{result['TSD']}"
    )

    print("Left TIR:", result["Left_TIR"])
    print("Right TIR:", result["Right_TIR"])

print("\nTotal elements detected:", len(results))

print("DNA length validation:",
      "PASSED" if 200 <= len(dna_sequence) <= 400 else "FAILED")

print("TE detection validation:",
      "PASSED" if len(results) == 4 else "FAILED")