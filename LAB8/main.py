import numpy as np

def s(s1, s2):
    if s1 == s2:
        return match
    else:
        return mmatch


s1 = np.array(list("ACTGGGTAACCGATACGCTACTA"))
s2 = np.array(list("ACTGGACTACCGAAGCTACTA"))

matrix = np.zeros((len(s1) + 1, len(s2) + 1))

gap = -2
match = 1
mmatch = -1

for i in range(len(s1) + 1):
    matrix[i, 0] = i * gap

for i in range(len(s2) + 1):
    matrix[0, i] = i * gap
    
for i in range(1, len(s1) + 1):
    for j in range(1, len(s2) + 1):

        if s1[i-1] == s2[j-1]:
            score = match
        else:
            score = mmatch

        diagonal = matrix[i-1, j-1] + score
        up = matrix[i-1, j] + gap
        left = matrix[i, j-1] + gap

        matrix[i, j] = max(diagonal, up, left)

alligned_s1 = ""
alligned_s2 = ""

i, j = len(s1), len(s2)

while i > 0 or j > 0:
    if matrix[i, j] == matrix[i - 1, j - 1] + s(s1[i - 1], s2[j - 1]):
        alligned_s1 = s1[i - 1] + alligned_s1
        alligned_s2 = s2[j - 1] + alligned_s2
        i -= 1
        j -= 1
    elif matrix[i, j] == matrix[i - 1, j] + gap:
        alligned_s1 = s1[i - 1] + alligned_s1
        alligned_s2 = '-' + alligned_s2
        i -= 1
    else:
        alligned_s1 = "-" + alligned_s1
        alligned_s2 = s2[j-1] + alligned_s2
        j -= 1
        
print(matrix)
print(alligned_s1)
print(alligned_s2)