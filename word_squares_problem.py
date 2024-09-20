#!/usr/bin/env python

class WordSquares():
    import collections
    def __init__(self):
        pass

    def findWordSquares(self,words):
        """
        Given a set of words (without duplicates), find all word squares you can build from them.
        A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).
        For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.
        b a l l
        a r e a
        l e a d
        l a d y

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

# TODO: implement alternative solution with Trie
# https://algo.monster/liteproblems/425
