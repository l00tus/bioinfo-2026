import random
import csv

in_file = "GCF_000853865.1_ViralProj14960_genomic.fna"
out_file = "samples.csv"
n_samples = 20000

with open(in_file, 'r', encoding="utf-8") as file:
    genome = "".join(
        line.strip()
        for line in file
        if line.strip() and not line.lstrip().startswith(">")
    )
        
genome = genome.upper()
rng = random.Random()

with open(out_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["sample_id", "start", "end", "length", "sequence"])
    
    for i in range(1, n_samples + 1):
        length = rng.randint(100, 150)
        start = rng.randint(0, len(genome) - length)
        sequence = genome[start:start + length]
        
        writer.writerow([
            i,
            start + i,
            start + length,
            length,
            sequence
            ])
        
print(f"genome length: {len(genome)} nucleotides")
print(f"samples generated: {n_samples}")
print(f"results saved to: {out_file}")

sequences = []
min_overlap = 9

with open(out_file, 'r', newline="") as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        sequence = row['sequence'].strip().upper()
        if sequence:
            sequences.append(sequence)

sequences = list(set(sequences))

sequences.sort(key=len, reverse=True)
filtered_sequences = []

for sequence in sequences:
    if not any(sequence in existing for existing in filtered_sequences):
        filtered_sequences.append(sequence)
        
sequences = filtered_sequences

while True:
    best_overlap = min_overlap - 1
    best_i = -1
    best_j = -1
    best_merged = None
    
    for i in range(len(sequences)):
        for j in range(len(sequences)):
            if i == j:
                continue
            
            max_overlap = min(len(sequences[i]), len(sequences[j]))
            
            for overlap in range(max_overlap, min_overlap - 1, -1):
                if sequences[i][-overlap] == sequences[j][:overlap]:
                    if overlap > best_overlap:
                        best_i = i
                        best_j = j
                        best_merged = (
                            sequences[i] + sequences[j][overlap:] 
                        )
                    break
    
    if best_i == -1:
        print('no more overlaps meeting the min threshold')
        break
    
    sequences[best_i] = best_merged
    del sequences[best_j]
    
    print(
        f"merged wiith overlap {best_overlap}"
        f"{len(sequences)} contigs remain"
    )

reconstr_file = 'reconstructed_genome.fasta'
with open(reconstr_file, 'w') as file:
    file.write(f">contiig_{i} length={len(sequence)}\n")
    
    for start in range(0, len(sequence), 80):
        file.write(sequence[start:start + 80] + "\n")
        
print("\nassembly complete")
print(f"contigs: {len(sequences)}")
print(f"total assembled bases: {sum(len(s) for s in sequences)}")
print(f"longest contig: {max(len(s) for s in sequences)}")
print(f"output recontr file: {reconstr_file}")