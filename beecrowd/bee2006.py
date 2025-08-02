"""
A primeira linha contém um inteiro T representando o tipo de chá (1 ≤ T ≤ 4). 
A segunda linha contém cinco inteiros A, B, C, D e E, que indica a resposta dada por cada competidor (1 ≤ A, B, C, D, E ≤ 4).
"""

T = int(input())

A, B, C, D, E = map(int, input().split())

tea_list = [A, B, C, D, E]
count = 0

for i in range(len(tea_list)):
    if T == tea_list[i]:
        count += 1

print(count)