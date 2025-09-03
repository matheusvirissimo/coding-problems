def mergeAlternately(word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """


        if len(word1) > len(word2):
            n1 = len(word2) # menor size
            n2 = len(word1) # maior size
            
            biggest_word = word1
        else: 
            n1 = len(word1) # menor size
            n2 = len(word2) # maior size
            biggest_word = word2

        merged_string = ''

        for i in range(n1):
            merged_string += word1[i]
            merged_string += word2[i]
        
        for i in range(n1, n2): 
            merged_string += biggest_word[i]

        return merged_string

word1 = "abcd"
word2 = "pqr"

print(mergeAlternately(word1, word2))