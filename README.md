# Tariff Risk Disclosure Dataset

Exploratory EDGAR pipeline for collecting 10-K `Item 1A. Risk Factors` text
from trade-exposed public firms and identifying tariff-related language, 2022–2025.

For the cleaner balanced report-year panel, see
`kamran-py/tariff-risk-disclosures-v2`.

## Data Sources

The pipeline uses SEC EDGAR public endpoints:

- Company ticker to CIK lookup: `https://www.sec.gov/files/company_tickers.json`
- Company submissions history: `https://data.sec.gov/submissions/CIK##########.json`
- Filing documents from `https://www.sec.gov/Archives/edgar/data/...`
- SEC full-text search for supplemental 2025 10-K hits: `https://efts.sec.gov/LATEST/search-index`

The pipeline enumerates 10-Ks for a fixed firm universe and can supplement them
with an SEC-wide search for 2025 "Liberation Day" disclosures.

SEC access rules:

- Set a descriptive contact-bearing `User-Agent`.
- Keep requests at or below 10/second (the default is 8).
- Responses are cached in `data/cache`.

## Quick Start

```powershell
$env:SEC_USER_AGENT = "TariffRiskStudy/0.1 contact@example.com"
python scripts/build_tariff_risk_dataset.py
```

The default output is:

```text
data/risk_factors_2022_2025.csv
```

Useful options:

```powershell
# Preview selected filings without downloading documents.
python scripts/build_tariff_risk_dataset.py --dry-run --output data/dry_run_filings.csv

# Test a small sample.
python scripts/build_tariff_risk_dataset.py --limit-firms 2 --output data/sample.csv

# Use fiscal report year instead of calendar filing year.
python scripts/build_tariff_risk_dataset.py --date-basis report --output data/risk_factors_report_year_2022_2025.csv

# Use only the fixed firm universe.
python scripts/build_tariff_risk_dataset.py --no-include-sec-search
```

## Output

The CSV includes firm and filing metadata, Item 1A text, counts, matched terms,
and short excerpts. Analyze all rows as one dataset; `sample_source`,
`sec_search_query`, and `sec_search_display_name` are provenance fields.

Filters default to calendar `filing_date` year. Use `--date-basis report` to align with fiscal year-end.

## Firm Universe

`config/trade_exposed_firms.csv` contains the seed universe of manufacturing,
retail, and technology-hardware firms. Edit it to change the sample.

## Tariff Terms

`config/tariff_terms.txt` holds the term list. The script uses word-boundary
matches and stores up to five excerpts per filing.

The list includes `liberation day` and `liberation day tariff`. Supplemental
queries in `config/sec_search_queries.txt` search 2025 10-Ks, retaining only
filings whose Item 1A text contains one of those terms.

The current supplemental search adds one 2025 10-K: A-Mark Precious Metals
(`AMRK`), filed September 11, 2025, matching `liberation day`. No filing
exactly matches `liberation day tariff`.

## Tests

```powershell
python -m unittest discover -s tests
```
