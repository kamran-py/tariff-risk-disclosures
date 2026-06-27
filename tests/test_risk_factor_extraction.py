import unittest

from scripts.build_tariff_risk_dataset import count_terms, extract_item_1a, parse_display_name


class RiskFactorExtractionTests(unittest.TestCase):
    def test_chooses_long_item_1a_over_table_of_contents(self):
        body = " ".join(["Tariffs and import duties may affect margins."] * 90)
        html = f"""
        <html><body>
          <p>Table of Contents Item 1A. Risk Factors Item 1B. Unresolved Staff Comments</p>
          <h2>ITEM 1A. RISK FACTORS</h2>
          <p>{body}</p>
          <h2>Item 1B. Unresolved Staff Comments</h2>
        </body></html>
        """

        extracted = extract_item_1a(html)

        self.assertIn("Tariffs and import duties", extracted)
        self.assertGreater(len(extracted), 1000)

    def test_counts_multiword_terms(self):
        text = "Tariffs, import duties, and Section 301 tariffs are material."
        total, matched = count_terms(text, ["tariff", "tariffs", "import duties", "section 301"])

        self.assertEqual(total, 4)
        self.assertEqual(matched, ["tariffs", "import duties", "section 301"])

    def test_prefers_longest_non_overlapping_term(self):
        text = "Higher customs duties and import duties may increase costs."
        total, matched = count_terms(text, ["customs duties", "import duties", "duties"])

        self.assertEqual(total, 2)
        self.assertEqual(matched, ["customs duties", "import duties"])

    def test_parses_sec_display_name_with_optional_ticker(self):
        company, ticker = parse_display_name(
            "A-Mark Precious Metals, Inc.  (AMRK)  (CIK 0001591588)"
        )
        self.assertEqual(company, "A-Mark Precious Metals, Inc.")
        self.assertEqual(ticker, "AMRK")

        company, ticker = parse_display_name("Kingfish Holding Corp  (CIK 0001374881)")
        self.assertEqual(company, "Kingfish Holding Corp")
        self.assertEqual(ticker, "")


if __name__ == "__main__":
    unittest.main()
