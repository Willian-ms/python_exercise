s1 = input("Digite uma frase: ")
s2 = input("Digite outra frase: ")

s1_1 = s1[0] + s1[len(s1) // 2] + s1[-1]
s2_2 = s2[0] + s2[len(s2) // 2] + s2[-1]

s3 = s1_1 + s2_2
print(s3)
