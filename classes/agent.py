class Agent:
    def __init__(self,code_name, clearance_level):
        self.code_name=str(code_name)
        self.clearance_level=int(clearance_level)
    def report(self):
        print(f'Agent {self.code_name} reporting. Clearance Level: {self.clearance_level}')