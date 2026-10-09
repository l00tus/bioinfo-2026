mrna = "ACAAAUGGUAAUCCAGCAUUAUUAA"
full_aa = ""

codon_to_three = {
    "UUU": "Phe", "UUC": "Phe",
    "UUA": "Leu", "UUG": "Leu",
    "CUU": "Leu", "CUC": "Leu",
    "CUA": "Leu", "CUG": "Leu",
    "AUU": "Ile", "AUC": "Ile", 
    "AUA": "Ile", "AUG": "Met",
    "GUU": "Val", "GUC": "Val",
    "GUA": "Val", "GUG": "Val",
    "UCU": "Ser", "UCC": "Ser",
    "UCA": "Ser", "UCG": "Ser",
    "AGU": "Ser", "AGC": "Ser",
    "CCU": "Pro", "CCC": "Pro",
    "CCA": "Pro", "CCG": "Pro",
    "ACU": "Thr", "ACC": "Thr",
    "ACA": "Thr", "ACG": "Thr",
    "GCU": "Ala", "GCC": "Ala",
    "GCA": "Ala", "GCG": "Ala",
    "UAU": "Tyr", "UAC": "Tyr",
    "UAA": "Stop", "UAG": "Stop",
    "CAU": "His", "CAC": "His",
    "CAA": "Gln", "CAG": "Gln",
    "AAU": "Asn", "AAC": "Asn",
    "AAA": "Lys", "AAG": "Lys",
    "GAU": "Asp", "GAC": "Asp",
    "GAA": "Glu", "GAG": "Glu",
    "UGU": "Cys", "UGC": "Cys",
    "UGA": "Stop", "UGG": "Trp",
    "CGU": "Arg", "CGC": "Arg",
    "CGA": "Arg", "CGG": "Arg",
    "AGA": "Arg", "AGG": "Arg",
    "GGU": "Gly", "GGC": "Gly",
    "GGA": "Gly", "GGG": "Gly",
}

three_to_one = {
    'Ala': 'A',        
    'Arg': 'R',
    'Cys': 'C',
    'Asp': 'D',
    'Glu': 'E',
    'Phe': 'F',
    'Gly': 'G',
    'His': 'H',
    'Ile': 'I',
    'Lys': 'K',
    'Leu': 'L',
    'Met': 'M',
    'Pro': 'P',
    'Gln': 'Q',
    'Ser': 'S',
    'Thr': 'T',
    'Val': 'V',
    'Trp': 'W',
    'Tyr': 'Y',
}

for i in range(len(mrna)):
    if mrna[i : i + 3] == 'AUG':
        start = i

mrna = mrna[start : ]        
length = len(mrna)

for i in range(length):
    codon = mrna[3 * i : 3 * (i + 1)]
    aa_three = codon_to_three[codon]
    full_aa += aa_three

    if aa_three == 'Stop':
        break

print(f"mRNA: {mrna}")
print(f"Aminoacid (three letter abbr): {full_aa}")
