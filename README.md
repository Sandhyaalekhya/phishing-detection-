# Phishing URL Detection System 🛡️

A Python-based security tool designed to analyze and identify malicious URLs to protect users from phishing attacks.

## 🚀 Key Features
- **URL Analysis:** Scans links for common phishing indicators (e.g., long URLs, unusual subdomains, or suspicious character encoding).
- **Heuristic Engine:** Uses a rule-based system to calculate a "risk score" for any given website address.
- **Domain Verification:** Checks the age and validity of domains against security databases.
- **Detailed Reporting:** Provides users with a clear "Safe" or "Phishing" verdict with a breakdown of detected threats.

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:** `requests`, `BeautifulSoup4` (for web scraping), `re` (Regular Expressions), and `socket`.
- **Data Source:** (Optional: Mention if you used datasets like PhishTank or Kaggle).

## 🧠 Technical Highlights
- **Feature Extraction:** Developed custom logic to extract 15+ features from raw URLs, such as presence of '@' symbols, prefix/suffix usage, and HTTPS status.
- **Pattern Matching:** Implemented advanced Regular Expressions to detect obfuscated links and typosquatting.
- **Network Validation:** Used the `socket` library to perform DNS lookups and verify the IP reputation of the hosting server.
- **Accuracy Optimization:** Refined the detection algorithm to minimize false positives while maintaining high sensitivity to zero-day phishing attempts.

## 📧 Contact
- **Email:** jsandhyaalekhya@gmail.com
- **LinkedIn:** [Sandhya Alekhya Jampana](https://www.linkedin.com/in/sandhya-alekhya-jampana-b22500348/)
