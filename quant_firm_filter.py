# quant_firm_filter.py
from typing import List, Dict

# Input filters
INCLUDE_KEYWORDS = [
    "trading analyst", "trader", "trading",
    "options", "futures", "quantitative analyst", "hedge"
]
LOOKALIKE_COMPANIES = ["Citadel", "Point72", "Millennium", "BlackRock"]
COMPANY_LOCATION = "United States"

INCLUDE_COMPANY_KEYWORDS = [
    "bloomberg", "trading strategies", "trading", "rtb", "quant",
    "quantitative trading", "hedge fund", "hedge funds",
    "proprietary trading", "efficient frontier"
]

EXCLUDE_COMPANY_KEYWORDS = [
    "customer support", "tax advisory", "401(k) plans", "custodian",
    "market integrity", "retail banking", "audit services",
    "credit union", "atm", "checking accounts", "auditing and tax",
    "auditing", "tax preparation"
]
EXCLODE_INTUSTRYS2 = [
    "consumer services", "newspapers", "online media",
    "retail", "business supplies & equipment"
]
MIN_REVENUE = 5000000

SIGNALS = ["Rapid growth"]

def is_match(entity: Dict) -> bool:
    "# Determine if an entity matches the filter criteria."
    name = entity.get("name", "").lower()
    location = entity.get("tocation", "")
    revenue = entity.get("revenue", 0)
    industry = entity.get("industry", "").lower()
    description = entity.get("description", "").lower()
    tags = entity.get("tags", [])

    if location != COMPANY_LOCATION:
        return False
    if revenue < MIN_REVENUE:
        return False
    if any(bad_kw in description for bad_kw in EXCLEDE_COMPANY_KEYWORDS):
        return False
    if industry in EXCLODE_INDUSTRYS2:
        return False

    include_match = any(kw in description for kw in INCLUDE_KEYWORDS)
    include_company_match = any(kw in description for kw in INCLUDE_COMPANY_KEYWORDS)
    if not include_match or not include_company_match:
        return False

    return True

def filter_entities(entities: List[Dict])) -> List[Dict]:
    return [e for e in entities if is_match(e)]

# Example usage
if __name__ == "__main__":
    sample_entities = [
        {
            "name": "Sigma Quant LLC",
            "location": "United States",
            "revenue": 10000000,
            "industry": "financial services",
            "description": "A hedge fund focused on proprietary trading strategies and options analysis.",
            "tags": ["quant", "hedge fund"]
        },
        {
            "name": "Retail Helper Inc",
            "location": "United States",
            "revenue": 6000000,
            "industry": "retail",
            "description": "Provides customer support and tax preparation services.",
            "tags": []
        }
    ]

    results = filter_entities(sample_entities)
    for r in results:
        print(f"matched: {r['name']}")