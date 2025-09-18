
from crewai import Task
from agents import financial_analyst

analyze_financial_document = Task(
    description='Extract key facts from the provided financial document. Do NOT fabricate information or provide investment advice.',
    expected_output='A dict with keys like revenue, net_income, summary_snippet, disclaimer.',
    agent=financial_analyst,
    tools=[],
    async_execution=False
)
