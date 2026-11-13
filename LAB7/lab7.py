ENZYMES = [
    "EcoRI,GAATTC,G^AATTC",
    "BamHI,GGATCC,G^GATCC",
    "HindIII,AAGCTT,A^AGCTT",
    "TaqI,TCGA,T^CGA",
    "HaeIII,GGCC,GG^CC",
]


def read_fasta(path):
    with open(path) as f:
        lines = [l.strip() for l in f if l.strip() and not l.startswith(">")]
    return "".join(lines).upper()

seq = read_fasta('sequence.fasta')

results = {}
for e in ENZYMES:
    name, site, cleavage = [p.strip() for p in e.split(",")]
    offset = cleavage.index("^")
 
    # cut positions
    cuts = []
    i = seq.find(site)
    while i != -1:
        cuts.append(i + offset)
        i = seq.find(site, i + 1)
 
    # split the sequence at the cuts
    fragments = []
    prev = 0
    for c in cuts:
        fragments.append(seq[prev:c])
        prev = c
    fragments.append(seq[prev:])
 
    results[name] = fragments
    print(f"{name} ({site}): {len(cuts)} cleavages")
    print("cut positions:", cuts)
    print("fragment lengths:", [len(f) for f in fragments])