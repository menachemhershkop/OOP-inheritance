class Agent:
    '''Agent code, and clearance level'''
    total_agents=0
    def __init__(self,code_name:str, clearance_level:int):
        self.code_name=code_name
        self._clearance_level=clearance_level
        Agent.total_agents+=1
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
    @staticmethod
    def get_total_agents():
        print("Sum of all agents is: ",Agent.total_agents)
