# Financial Document Analyzer - Fixed & Safe Version

What I changed (as a fresher)
- Replaced unsafe, hallucination-prone prompts and task descriptions with deterministic, safe instructions.
- Added a minimal `crewai` stub package so the project runs locally without external dependencies during testing.
- Implemented a simple `financial_analyst` agent that extracts key figures (revenue, net income) using deterministic regex from the PDF text.
- Implemented a `read_pdf_text` tool that uses `PyPDF2` to extract text from PDFs if available.
- Modified `main.py` to provide a simple CLI runner for local testing (`python main.py`).

Bugs found & fixes
- ModuleNotFoundError: No module named 'crewai' - fixed by adding a lightweight `crewai` stub.
- Agents and tools contained intentionally malicious/hallucinatory instructions. Rewrote them to be safe and deterministic.
- The original code relied on external LLM infra. Replaced with deterministic agent logic for offline testing.
- Added defensive checks for missing PDF reader and missing files.

Safety note
This project does NOT provide investment advice. It extracts factual text snippets and numeric patterns from documents. Any financial decision should be made after consulting a licensed professional.

Setup & Usage (local testing)
1. Optional: Create a virtual environment:
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\\Scripts\\activate    # Windows

2. Install PyPDF2 (optional, required to extract text from PDFs):
   pip install PyPDF2

3. Run the quick local analyzer against the sample PDF included:
   python main.py

4. To analyze a different PDF:
   python main.py /path/to/your_document.pdf

Files of interest
- main.py - simple runner for local testing
- task.py - defines analyze_financial_document Task (safe description)
- agents.py - simple, deterministic financial_analyst implementation
- tools.py - read_pdf_text helper (uses PyPDF2)
- crewai/ - minimal stub for running without external CrewAI infra