
import re
from tools import read_pdf_text

def financial_analyst(inputs):
    file_path = inputs.get('file_path')
    text = read_pdf_text(file_path)
    if not text:
        return {'error': 'No text extracted from document.'}
    findings = {}
    rev = re.search(r'(Revenue|Total revenue|Revenues)[:\s\$]*([0-9,\.]+)', text, re.IGNORECASE)
    np = re.search(r'(Net profit|Net loss|Net income)[:\s\$]*([0-9,\.\-]+)', text, re.IGNORECASE)
    if rev: findings['revenue'] = rev.group(2)
    if np: findings['net_income'] = np.group(2)
    findings['summary_snippet'] = text[:500]
    findings['disclaimer'] = 'This analysis is informational only. Not financial advice.'
    return findings
