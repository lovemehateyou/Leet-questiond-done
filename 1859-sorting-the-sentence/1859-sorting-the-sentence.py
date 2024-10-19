class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()  
        correct = [None] * len(words) 

        for word in words:
            index = int(word[-1]) - 1  
            correct[index] = word[:-1] 

        sentence = " ".join(correct) 
        return sentence
            