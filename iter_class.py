
class iter_:
    
    def __init__(self, max):
        self.max = max  
    
    def __iter__(self):
        self.curr = 0
        return self
        
    def next(self):
        numb = self.curr
        if self.curr >= self.max:
            raise StopIteration
        self.curr += 1
        return numb

for i in iter_(5):
    print i
        
    
    