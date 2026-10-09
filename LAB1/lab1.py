import matplotlib.pyplot as plt

seq = "ATGTAATAGCGGAATTCGAGCGTAATCGAATTT"
freq = dict()
freq2 = dict()
freq3 = dict()

for symbol in seq:
    freq[symbol] = freq.get(symbol, 0)  + 1

for index in range(0, len(seq) - 1):
    freq2[seq[index] + seq[index + 1]] = freq2.get(seq[index] + seq[index + 1], 0) + 1
    
for index in range(0, len(seq) - 2):
    freq3[seq[index] + seq[index + 1] + seq[index + 2]] = freq3.get(seq[index] + seq[index + 1] + seq[index + 2], 0) + 1
    
print(freq)
print(freq2)
print(freq3)

plt.subplot(2, 1, 1)
plt.bar(freq2.keys(), freq2.values())

plt.subplot(2, 1, 2)
plt.bar(freq3.keys(), freq3.values())

plt.show()
