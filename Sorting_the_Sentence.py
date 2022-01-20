class Solution:
    def sortSentence(self, s: str) -> str:
        

        list_of_words = s.split()

        result = [0] * len(list_of_words)

    
        for word in list_of_words:
            index = int(word[-1])
            result[index - 1] = word
        
        result_str = ''

        for word in result:
            result_str += word[:-1] + " "
        
        return result_str[:-1]


Sol = Solution()
print(Sol.sortSentence("is2 sentence4 This1 a3"))