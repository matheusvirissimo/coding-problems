class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_list = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        integer = 0
        
        for i in range(len(s)):
            if i+1 < len(s) and roman_list[s[i]] < roman_list[s[i+1]]:
                integer -= roman_list[s[i]]
            else:
                integer += roman_list[s[i]]

        return integer


roman_list = ["I", "V", "X", "L", "C", "D", "M"]
roman = "III"
integer = 0

for i in range(len(roman)):
    if i + 1 < len(roman) and roman_list[i] > roman_list[i+1]:
        integer -= roman[i]
    else:
        integer += roman[i]

        


## TESTES E ESTUDO

roman = "LXV"
roman_list = []
numero_literal = 0
numeros_romanos = ["I", "V", "X", "L", "C", "D", "M"]

for roman_letter in roman:
    roman_list.append(roman_letter)

print(roman_list)

while len(roman_list) > 0:
    letra_romana = roman_list.pop()
    match letra_romana:
        case "L":
            numero_literal += 50
        case "X":
            numero_literal += 10
        case "V":
            numero_literal += 5
        case _:
            break

print(numero_literal)

print(numeros_romanos)
print(numeros_romanos.index("I"))
print(numeros_romanos.index("V"))

quatro = "IV"

for letra_romana in quatro:
    roman_list.append(letra_romana)

for i in len(roman_list):
    for j in len(roman_list):
        if roman_list[i] < roman_list[j]:
            print()

# while len(roman_list) > 0:
#     numero_atual = roman_list.pop()
#     if
