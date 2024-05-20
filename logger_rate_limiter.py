"""
Problem statement:
Design a logger system that receives a stream of messages along with their timestamps. 
Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).
All messages will come in chronological order. Several messages may arrive at the same timestamp.

Return true if the message should be printed in the given timestamp, otherwise return false.

E.g., 
input: [[], [1, "foo"], [2, "bar"], [3, "foo"], [8, "bar"], [10, "foo"], [11, "foo"]]
Output: [null, true, true, false, false, false, true]
"""

class Logger:
    def __init__(self):
        self.memory = dict()
        
    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message is None:
            return False
        if message in self.memory:
            if timestamp - self.memory.get(message) >= 10:
                self.memory[message] = timestamp
                return True
            else:
                return False  
        else:
            self.memory[message] = timestamp
            return True    
        

if __name__ == "__main__":
    obj = Logger()
    param_1 = obj.shouldPrintMessage(timestamp,message)

