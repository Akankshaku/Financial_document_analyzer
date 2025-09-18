
# Minimal safe stub for crewai used by the project for offline testing.
class Task:
    def __init__(self, description='', expected_output='', agent=None, tools=None, async_execution=False):
        self.description = description
        self.expected_output = expected_output
        self.agent = agent
        self.tools = tools or []
        self.async_execution = async_execution

class Process:
    def __init__(self, task, inputs):
        self.task = task
        self.inputs = inputs
    def run(self):
        # Simple deterministic processing: call agent if callable, else summarize inputs
        agent = getattr(self.task, 'agent', None)
        if callable(agent):
            return agent(self.inputs)
        return {'summary': str(self.inputs)}

class Crew:
    def __init__(self):
        pass
    def run(self, process):
        return process.run()
