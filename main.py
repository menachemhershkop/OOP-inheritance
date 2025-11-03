from classes.agent import Agent
from classes.cyber import CyberAgent
from classes.field_agent import FieldAgent


def list_agent():
    agent1=Agent("meni",3)
    agent2=FieldAgent("dani",7,"iran")
    agent3=CyberAgent("yossi",2,"hacker")

    agent1.report()
    agent2.report()
    agent3.report()
    Agent.get_total_agents()
if __name__=='__main__':
    list_agent()