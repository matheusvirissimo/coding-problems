def maxProfit(prices: list):
        """
        :type prices: List[int]
        :rtype: int
        """
        menor = min(prices)
        i = 0

        for i in range(len(prices)):
            if prices[i] == menor: 
                pos_menor = i
                break

        maior = max(prices[pos_menor:])
        for i in range(pos_menor, len(prices)):
            if maior == prices[i]:
                pos_maior = i

        if pos_menor == pos_maior:
            max_profit = 0
        else:
            max_profit = pos_maior+1
        
        return max_profit

# prices = [7,1,5,3,6,4]
# print(maxProfit(prices))
prices = [7,6,4,3,1]
print(maxProfit(prices))
# prices = [1,2,4]
# print(maxProfit(prices))
prices = [1,2]
print(maxProfit(prices))