import re
from typing import Tuple, List, Dict

def mask_pii(text: str) -> Tuple[str, List[Dict]]:
    entities = []
    patterns = {
        "full_name": r"\b[A-Z][a-z]+\s[A-Z][a-z]+\b",
        "email": r"[\w\.-]+@[\w\.-]+",
        "phone_number": r"\b\d{10}\b",
        "dob": r"\b\d{2}[-/]\d{2}[-/]\d{4}\b",
        "aadhar_num": r"\b\d{4}\s\d{4}\s\d{4}\b",
        "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
        "cvv_no": r"\b\d{3}\b",
        "expiry_no": r"\b(0[1-9]|1[0-2])/?([0-9]{2})\b"
    }

    for entity_type, pattern in patterns.items():
        for match in re.finditer(pattern, text):
            start, end = match.start(), match.end()
            entity_val = match.group()
            entities.append({
                "position": [start, end],
                "classification": entity_type,
                "entity": entity_val
            })
            text = text[:start] + f"[{entity_type}]" + text[end:]
            shift = len(f"[{entity_type}]") - (end - start)
            for e in entities:
                if e['position'][0] > start:
                    e['position'][0] += shift
                    e['position'][1] += shift

    return text, entities

#function to return masked text
def mask_pii_entities(text: str) -> str:
    masked_text, _ = mask_pii(text)
    return masked_text