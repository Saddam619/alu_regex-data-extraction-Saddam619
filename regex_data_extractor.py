#!/usr/bin/python3
import re

# Load text content from file
with open("sample_data.txt", "r") as f:
    content = f.read()

# 1. Extract Email Addresses
email_regex = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_regex, content)

# 2. Extract URLs
url_regex = r'https?://[^\s<>"\']+'
urls = re.findall(url_regex, content)

# 3. Extract Phone Numbers
phone_regex = r'\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
phones = re.findall(phone_regex, content)

# 4. Extract Credit Card Numbers
card_regex = r'\b(?:\d{4}[- ]?){3}\d{4}\b'
credit_cards = re.findall(card_regex, content)

# 5. Extract Time (24h and 12h formats)
time_regex = r'\b(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[AaPp][Mm])?\b'
times = re.findall(time_regex, content)

# 6. Extract HTML Tags
html_regex = r'<[^>]+>'
html_tags = re.findall(html_regex, content)

# 7. Extract Hashtags
hashtag_regex = r'#\w+'
hashtags = re.findall(hashtag_regex, content)

# 8. Extract Currency Values
currency_regex = r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'
currency_amounts = re.findall(currency_regex, content)

# -------------------------------------
# Displaying Extracted Information
# -------------------------------------
print("Extracted Emails:", emails)
print("Extracted URLs:", urls)
print("Extracted Phone Numbers:", phones)
print("Extracted Credit Cards:", credit_cards)
print("Extracted Time Values:", times)
print("Extracted HTML Tags:", html_tags)
print("Extracted Hashtags:", hashtags)
print("Extracted Currency Amounts:", currency_amounts)
