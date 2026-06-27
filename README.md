# Tariff Risk Disclosure Dataset

This project builds a dataset of 10-K `Item 1A. Risk Factors` disclosure for trade-exposed public firms, focused on tariff-related language from 2022 through 2025.

It uses SEC EDGAR public endpoints:

- Company ticker to CIK lookup: `https://www.sec.gov/files/company_tickers.json`
- Company submissions history: `https://data.sec.gov/submissions/CIK##########.json`
- Filing documents from `https://www.sec.gov/Archives/edgar/data/...`
- SEC full-text search for supplemental 2025 10-K hits: `https://efts.sec.gov/LATEST/search-index`

The pipeline starts from a fixed firm universe, so it uses the company submissions endpoint to enumerate each firm's 10-Ks directly. It also runs a supplemental SEC-wide full-text search for 2025 10-Ks that may mention the April 2, 2025 "Liberation Day" tariff announcement.

SEC access notes:

- Set a descriptive `User-Agent` with contact information.
- Keep automated requests at or below 10 requests/second. The script defaults to 8 requests/second.
- Responses are cached under `data/cache` to avoid repeat downloads.

## Quick Start

```powershell
$env:SEC_USER_AGENT = "TariffRiskStudy/0.1 your.name@example.com"
python scripts/build_tariff_risk_dataset.py
```

The default output is:

```text
data/risk_factors_2022_2025.csv
```

Useful options:

```powershell
# Confirm which filings would be selected without downloading the documents.
python scripts/build_tariff_risk_dataset.py --dry-run --output data/dry_run_filings.csv

# Test one or two firms first.
python scripts/build_tariff_risk_dataset.py --limit-firms 2 --output data/sample.csv

# Use fiscal report year instead of calendar filing year.
python scripts/build_tariff_risk_dataset.py --date-basis report --output data/risk_factors_report_year_2022_2025.csv

# Rebuild only the fixed firm universe, without SEC-wide search supplements.
python scripts/build_tariff_risk_dataset.py --no-include-sec-search
```

## Dataset Fields

The CSV includes firm metadata, SEC filing metadata, extracted full Item 1A text, word and character counts, tariff-term hit counts, matched terms, and short tariff-related excerpts. Analyze all rows together as one dataset. The `sample_source`, `sec_search_query`, and `sec_search_display_name` fields are provenance/audit metadata only, not analytical grouping variables.

Year filters default to calendar `filing_date` year because most 10-Ks filed in 2022 discuss fiscal years ending in 2021. Use `--date-basis report` if the study should align by fiscal year-end instead.

## Firm Universe

The seed universe is in `config/trade_exposed_firms.csv` and includes manufacturing, retail, and tech hardware firms such as Caterpillar, Nike, Apple, Deere, Ford, 3M, and Intel. Edit that CSV to change the sample.

## Tariff Terms

The term list is in `config/tariff_terms.txt`. The script counts exact term matches with word boundaries and stores up to five context excerpts per filing.

The list includes `liberation day` and `liberation day tariff`. The supplemental search queries are in `config/sec_search_queries.txt`; by default they search 2025 10-Ks filed from `2025-01-01` through `2025-12-31`, then keep only filings whose extracted Item 1A text contains one of those exact Liberation Day terms.

Current SEC-wide supplemental result: one added 2025 10-K row, A-Mark Precious Metals (`AMRK`), filed September 11, 2025. Its Item 1A text matches `liberation day`. Treat this row the same as the other company rows in trend analysis. There were no exact Item 1A matches for `liberation day tariff` under the current exact-term matching rules.

## Tests

```powershell
python -m unittest discover -s tests
```
