class number:
	def _init_(self,a,b):
        self.a=2
        self.b=3
        def _add_(self,other):
            self.a+self.b
            return self.a,self.b
a,b=2,3
print a._add_(b)
