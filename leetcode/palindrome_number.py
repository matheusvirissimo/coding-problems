## a ideia é pegar o número e inverter ele. Se ele continuar igual, ainda sim,
## é palindromo



class Solution(object):
    def isPalindrome(self, x):
        s = str(x)
        if s == s[::-1]:
            return True
        else:
            return False

        
# x = 123
# y, dividir = x
# count = 1
# z = 0
     
# while dividir/10 > 1:
#     dividir = dividir/10
#     count += 1

# while count > 0:
#     z = y % 10

# while x > 0:
#     y = y * 10 + x % 10  # Adiciona o último dígito ao número invertido
#     x //= 10  # Remove o último dígito de x

    
x = 123
while x > 0:
    ultimoDigito = x % 10
    numeroReverso = numeroReverso * 10 + ultimoDigito
    x //= 10

# for i in range(x, 0, -1): ## vou andar de trás para frente nesse caso
#     print(i)
