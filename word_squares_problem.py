#!/usr/bin/env python

class WordSquares():
    import collections
    def __init__(self):
        pass

    def findWordSquares(self,words):
        """
        Find word squares
        
        Parameters :
        -----------------------
        words: List(str)
        
        Returns :
        -----------------------
        ans: List(List(str))
        
        eg.
        word_squares = WordSquares()
        word_squares.findWordSquares(words=["abat","baba","atan","atal"])
        [['baba', 'abat', 'baba', 'atan'], ['baba', 'abat', 'baba', 'atal']]
        
        """
        # create mappings
        mdict = collections.defaultdict(set)
        
        m = len(words)
        n = len(words[0]) if m else 0
        
        for i in range(n):
            for word in words:
                mdict[word[:i]].add(word)
         
        ws = []   
        ans = []
        line = 0
       
        def findNextWord(word,line):
            ws.append(word)
            if len(ws) == n:
                ans.append(ws[:])        
           
            else:
                prefix = "".join([w[line + 1] for w in ws[:line + 1]])
                for word in mdict[prefix]:
                    findNextWord(word,line + 1)
            ws.pop()
             
        for word in words:
            findNextWord(word,line)

        return ans
