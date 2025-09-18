from crewai import Crew, Process
from task import analyze_financial_document
import os, sys

def run_crew(query: str, file_path: str):
    crew = Crew()
    process = Process(analyze_financial_document, {'query': query, 'file_path': file_path})
    result = crew.run(process)
    return result

if __name__ == '__main__':
    # Simple local test runner
    sample = os.path.join(os.path.dirname(__file__), 'data', 'TSLA-Q2-2025-Update.pdf')
    if len(sys.argv) > 1:
        sample = sys.argv[1]
    print('Running analysis on', sample)
    out = run_crew('Analyze financial document', sample)
    print('Result:\n', out)
