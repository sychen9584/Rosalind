
dict = {"F": 2, "L": 6, "I": 3, "M": 1, "V": 4, "S": 6,
        "P": 4, "T": 4, "A": 4, "Y": 2, "*": 3, "H": 2,
        "Q": 2, "N": 2, "K": 2, "D": 2, "E": 2, "C": 2,
        "W": 1, "R": 6, "G": 4}

with open("rosalind_mrna.txt", "r") as f:
    protein = f.readline().strip()

num = 3 # stop condon
for aa in protein:
    num *= dict[aa]

with open("ouput.txt", "w+") as o:
    o.write(str(num%1000000))
