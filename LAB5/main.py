import random
import math

def read_fasta(filename):
    sequence = ""

    with open(filename, "r") as file:
        for line in file:
            line = line.strip()

            if not line.startswith(">"):
                sequence += line

    return sequence.upper()


dna = read_fasta("sequence.fasta")

print("DNA sequence length:", len(dna))

samples = []

for i in range(10):

    length = random.randint(100, min(3000, len(dna)))

    start = random.randint(0, len(dna) - length)

    fragment = dna[start:start + length]

    samples.append({
        "id": i + 1,
        "start": start,
        "length": length,
        "sequence": fragment
    })


for sample in samples:
    print(
        f"Sample {sample['id']}: "
        f"{sample['length']} bp"
    )

gel_length = 30

sizes = [sample["length"] for sample in samples]

min_size = min(sizes)
max_size = max(sizes)



for sample in samples:

    size = sample["length"]

    # smaller fragments migrate farther.
    migration = 1000 / size

    print(
        f"Sample {sample['id']}: "
        f"{size} bp -> "
        f"Migration value: {migration:.4f}"
    )
    

# ex2

repetitions = []

for unit_length in range(3, 6):

    i = 0

    while i <= len(dna) - 2 * unit_length:

        unit = dna[i:i + unit_length]

        count = 1

        while True:

            next_start = i + count * unit_length
            next_end = next_start + unit_length

            if next_end > len(dna):
                break

            if dna[next_start:next_end] == unit:
                count += 1
            else:
                break

        total_length = count * unit_length

        if count >= 2 and 6 <= total_length <= 10:

            repetitions.append({
                "position": i + 1,
                "unit": unit,
                "copies": count,
                "length": total_length,
                "sequence": dna[i:i + total_length]
            })

            i += total_length

        else:
            i += 1
            

if repetitions:

    for rep in repetitions:

        print(
            f"Position: {rep['position']} | "
            f"Unit: {rep['unit']} | "
            f"Copies: {rep['copies']} | "
            f"Length: {rep['length']} bp | "
            f"Sequence: {rep['sequence']}"
        )

else:
    print("No repetitions found.")

print("\nTotal repetitions found:", len(repetitions))