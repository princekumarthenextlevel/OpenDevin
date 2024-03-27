from typing import List

from opendevin.agent import Agent
from opendevin.llm.llm import LLM
from opendevin.state import State
from opendevin.action import Action

class PlannerAgent(Agent):
    def __init__(self, llm: LLM):
        super().__init__(llm)

    def step(self, state: State) -> Action:
        pass

    def search_memory(self, query: str) -> List[str]:
        pass

Agent.register("PlannerAgent", PlannerAgent)