# Tariff Risk Disclosure Trends

This note summarizes the tariff-risk disclosure patterns in the EDGAR 10-K Risk Factors dataset. Counts are based on exact keyword hits in extracted Item 1A Risk Factors text, using the terms in `config/tariff_terms.txt`.

The figures below should be read as a disclosure-intensity measure, not a semantic severity score. A higher count means a filing used more tariff/trade-restriction language in Item 1A, but it does not by itself measure financial exposure or expected impact.

## Main Takeaways

1. 2025 is the clear break point. Tariff-related mentions were stable from 2022 through 2024, then increased materially in 2025.
2. The 2025 increase is broad. Zero-hit filings fell, and the increase appears in tech hardware, manufacturing, and retail.
3. Tech hardware shows the sharpest 2025 jump, led by HP, HPE, Apple, Qualcomm, NVIDIA, and Dell.
4. Apparel and retail names were already high before 2025. Nike and Lululemon are cumulative leaders, but their 2025 change is less dramatic because their baseline was already elevated.
5. 2025 language is more policy-specific. Terms such as trade restrictions, trade barriers, retaliatory tariffs, import restrictions, export restrictions, and Liberation Day appear alongside generic tariff language.
6. The 2015 comparison shows how sparse tariff disclosure was before the recent policy cycle. The same firms from the key tables had only 32 tariff mentions in filing-year 2015 versus 248 in filing-year 2025.

## Overall Trend, 2022-2025

| Filing year | Filings | Total tariff mentions | Avg / filing | Mentions / 10k words | % with zero hits |
|---:|---:|---:|---:|---:|---:|
| 2022 | 34 | 220 | 6.5 | 5.41 | 5.9% |
| 2023 | 34 | 210 | 6.2 | 4.88 | 5.9% |
| 2024 | 34 | 206 | 6.1 | 4.90 | 5.9% |
| 2025 | 35 | 352 | 10.1 | 7.84 | 2.9% |

Interpretation: 2022-2024 look like a flat baseline. 2025 rises sharply on both raw and normalized counts, so the increase is not only a function of longer Risk Factors sections.

## Industry Bucket Trend

The bucket view uses firms with an assigned bucket in `config/trade_exposed_firms.csv`.

| Bucket | Year | Filings | Total mentions | Avg / filing | Mentions / 10k words |
|---|---:|---:|---:|---:|---:|
| Manufacturing | 2022 | 15 | 72 | 4.8 | 4.48 |
| Manufacturing | 2023 | 15 | 72 | 4.8 | 5.01 |
| Manufacturing | 2024 | 15 | 71 | 4.7 | 4.59 |
| Manufacturing | 2025 | 15 | 116 | 7.7 | 6.99 |
| Retail | 2022 | 9 | 87 | 9.7 | 9.56 |
| Retail | 2023 | 9 | 86 | 9.6 | 8.86 |
| Retail | 2024 | 9 | 84 | 9.3 | 8.46 |
| Retail | 2025 | 9 | 98 | 10.9 | 9.65 |
| Tech hardware | 2022 | 10 | 61 | 6.1 | 3.95 |
| Tech hardware | 2023 | 10 | 52 | 5.2 | 2.74 |
| Tech hardware | 2024 | 10 | 51 | 5.1 | 3.06 |
| Tech hardware | 2025 | 10 | 118 | 11.8 | 7.10 |

Interpretation: retail had the highest baseline, but tech hardware had the strongest inflection in 2025. Manufacturing also moved up meaningfully.

## Most Mentions, 2022-2025

| Rank | Ticker | Company | Filings | Total mentions | Avg / filing |
|---:|---|---|---:|---:|---:|
| 1 | NKE | Nike Inc. | 4 | 103 | 25.8 |
| 2 | LULU | Lululemon Athletica Inc. | 4 | 80 | 20.0 |
| 3 | NVDA | NVIDIA Corp. | 4 | 46 | 11.5 |
| 4 | DE | Deere & Co. | 4 | 45 | 11.2 |
| 5 | INTC | Intel Corp. | 4 | 44 | 11.0 |
| 6 | HON | Honeywell International Inc. | 4 | 43 | 10.8 |
| 7 | LOW | Lowe's Companies Inc. | 4 | 39 | 9.8 |
| 8 | HD | Home Depot Inc. | 4 | 38 | 9.5 |
| 9 | JCI | Johnson Controls International plc | 4 | 35 | 8.8 |
| 10 | AMD | Advanced Micro Devices Inc. | 4 | 35 | 8.8 |

Interpretation: cumulative leadership is concentrated in apparel, retail, semiconductors/hardware, industrials, and home improvement. Nike and Lululemon stand out because tariff and trade policy disclosure was already prominent in their Risk Factors before 2025.

## Highest 2025 Mentions

| Rank | Ticker | Company | Filing date | Mentions | Main matched terms |
|---:|---|---|---|---:|---|
| 1 | NKE | Nike Inc. | 2025-07-17 | 25 | trade restrictions, import duties, protectionism, tariffs |
| 2 | HPQ | HP Inc. | 2025-12-10 | 22 | import restrictions, trade restrictions, tariffs |
| 3 | HPE | Hewlett Packard Enterprise Co. | 2025-12-18 | 20 | export restrictions, trade restrictions, tariffs |
| 4 | AMRK | A-Mark Precious Metals, Inc. | 2025-09-11 | 20 | liberation day, retaliatory tariffs, trade war, tariffs |
| 5 | DE | Deere & Co. | 2025-12-18 | 19 | retaliatory tariffs, trade restrictions, trade barriers |
| 6 | LULU | Lululemon Athletica Inc. | 2025-03-27 | 19 | trade restrictions, tariffs, duties |
| 7 | JCI | Johnson Controls International plc | 2025-11-14 | 17 | trade restrictions, protectionist, tariffs |
| 8 | NVDA | NVIDIA Corp. | 2025-02-26 | 15 | export restrictions, trade restrictions, trade barriers |
| 9 | SWK | Stanley Black & Decker Inc. | 2025-02-18 | 14 | retaliatory tariffs, trade restrictions, section 301 |
| 10 | HON | Honeywell International Inc. | 2025-02-14 | 13 | retaliatory tariffs, trade restrictions, trade barriers |

Interpretation: 2025 leaders include both firms with longstanding tariff exposure language and firms with newly intensified policy language. AMRK is the clearest direct reference to the April 2, 2025 Liberation Day tariff announcement.

## Largest 2025 Increases Versus 2022-2024 Average

| Ticker | Company | 2025 mentions | 2022-2024 avg | Change |
|---|---|---:|---:|---:|
| HPQ | HP Inc. | 22 | 3.0 | +19.0 |
| HPE | Hewlett Packard Enterprise Co. | 20 | 1.7 | +18.3 |
| JCI | Johnson Controls International plc | 17 | 6.0 | +11.0 |
| DE | Deere & Co. | 19 | 8.7 | +10.3 |
| SWK | Stanley Black & Decker Inc. | 14 | 6.0 | +8.0 |
| AAPL | Apple Inc. | 11 | 3.3 | +7.7 |
| QCOM | Qualcomm Inc. | 11 | 4.7 | +6.3 |
| NVDA | NVIDIA Corp. | 15 | 10.3 | +4.7 |

Interpretation: the most striking 2025 acceleration is in tech hardware and industrial names, especially HP, HPE, Apple, Qualcomm, NVIDIA, Deere, Johnson Controls, and Stanley Black & Decker.

## 2015 Comparison

To benchmark against an earlier period, the 2015 10-Ks were downloaded for the firms that appeared in the key 2022-2025 trend tables. Filing-year 2015 is sparse relative to 2025.

| Ticker | Company | 2015 mentions | 2025 mentions | Change |
|---|---|---:|---:|---:|
| HPQ | HP Inc. | 0 | 22 | +22 |
| AMRK | A-Mark Precious Metals Inc. | 0 | 20 | +20 |
| HPE | Hewlett Packard Enterprise Co. | 0 | 20 | +20 |
| LULU | Lululemon Athletica Inc. | 1 | 19 | +18 |
| NKE | Nike Inc. | 7 | 25 | +18 |
| JCI | Johnson Controls International plc | 2 | 17 | +15 |
| NVDA | NVIDIA Corp. | 0 | 15 | +15 |
| DE | Deere & Co. | 5 | 19 | +14 |
| HON | Honeywell International Inc. | 1 | 13 | +12 |
| INTC | Intel Corp. | 0 | 12 | +12 |
| QCOM | Qualcomm Inc. | 0 | 11 | +11 |
| SWK | Stanley Black & Decker Inc. | 4 | 14 | +10 |
| LOW | Lowe's Companies Inc. | 2 | 11 | +9 |
| AAPL | Apple Inc. | 3 | 11 | +8 |
| HD | Home Depot Inc. | 4 | 11 | +7 |
| AMD | Advanced Micro Devices Inc. | 3 | 8 | +5 |

Summary across these firms:

| Period | Firms | Total mentions |
|---|---:|---:|
| 2015 | 16 | 32 |
| 2025 | 16 | 248 |

Interpretation: tariff-risk language was present in 2015, but mostly limited and generic. By 2025, the same set of firms shows a much broader and more explicit tariff-risk disclosure footprint.

## Caveats

- Counts are exact keyword hits, not model-classified risk severity.
- The same business risk can be disclosed with different wording across companies.
- Generic terms such as duties can occasionally reflect customs/tax context rather than tariffs specifically, although the keyword list prioritizes longer non-overlapping phrases where possible.
- Filing-year comparisons use calendar filing dates, not fiscal year-end, unless otherwise specified in the pipeline.
- The 2025 dataset includes one SEC full-text search result for Liberation Day language. That row is part of the analysis dataset; source fields are retained only for auditability.
