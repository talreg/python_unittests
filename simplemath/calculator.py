class Calculator(object):
    """docstring for Calculator"""
    def __init__(self):
        super(Calculator, self).__init__()
        self.value=0
    def mul(self,x,y):
        self.value=x*y
        return self.value;
    def div(self,x,y):
        if y==0:
            raise ValueError("can't diving in 0.")
        self.value=x/y;
        return self.value
    def get_last_results():
        return self.value;
