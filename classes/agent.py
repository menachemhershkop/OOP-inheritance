class Agent:
    '''Agent code, and clearance level'''
    def __init__(self,code_name:str, clearance_level:int):
        self.code_name=code_name
        self._clearance_level=clearance_level
    def report(self):
        print(f'Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}')
    def getter_clearance(self):
        print(self._clearance_level)
    def setter_clearance(self,level):
        if level<10 and level > 1:
            self._clearance_level=level
            print("Update is secces")
        else:
            print("the clearance number is incorrect")
