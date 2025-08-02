"""
Pegar a maior substring de uma string
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 1:
            return strs[0]

        smallest_word = min(strs, key=len)

        for i in range(len(smallest_word)):
            for word in strs:
                if i >= len(word) or word[i] != smallest_word[i]:
                    return smallest_word[:i]
        
        
        
        return smallest_word

# testes e estudos
# pode resolver horizontal ou vertical 
# horizontal - pega uma palavra e compara com outras 
# vertical - pega cada letra e compara com a próxima
## encontrar o prefixo de uma palavra (DEU CERTO)

palavra_1 = "teste"
palavra_2 = "testincas"
prefixo = ""

for i in range(len(palavra_1)):
    if palavra_1[i] == palavra_2[i]:
        prefixo += palavra_1[i]
    else:
        break

print(prefixo) 

# saber qual a menor palavra de todas na lista

palavras = ["chapeu", "chapeleira", "chapelinto"]
menor_palavra = min(palavras, key=len)
tam_menor_palavra = len(menor_palavra)

# iterar sobre cada item da lista
for palavra in palavras:
    print(palavra)
    for letra in palavra: 
        print(letra)

# juntar tudo

for i in range(tam_menor_palavra):
    for palavra in palavras:
        if palavra[i] != menor_palavra[i]:
            print(menor_palavra[:i])

print(menor_palavra)


# return "chape"