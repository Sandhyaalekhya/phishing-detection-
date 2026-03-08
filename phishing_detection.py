# Phishing Detection & Risk Assessment System

import re

# Sample phishing keywords
phishing_keywords = [
    "verify", "urgent", "login", "update", "password",
    "bank", "account", "click", "suspend", "confirm"
]

# Function to detect URLs
def has_url(text):
    url_pattern = re.compile(r'https?://|www\.')
    return bool(url_pattern.search(text))

# Risk assessment function
def assess_email(email_text):
    score = 0

    # Keyword check
    for word in phishing_keywords:
        if word.lower() in email_text.lower():
            score += 1

    # URL check
    if has_url(email_text):
        score += 2

    # Risk classification
    if score >= 5:
        return "High Risk 🚨"
    elif score >= 3:
        return "Medium Risk ⚠️"
    else:
        return "Low Risk ✅"

# Input from user
email = input("Enter email content:\n")
risk = assess_email(email)

print("\nCyber Risk Assessment Result:")
print("Risk Level:", risk)