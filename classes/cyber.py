from classes.agent import Agent


class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level, property):
        super().__init__(code_name,clearance_level)
        self.property=property
    def report(self):
        print(f'Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}, Property: {self.property}')
