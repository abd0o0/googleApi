import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def extract_email(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:112.0) Gecko/20100101 Firefox/112.0'
    }
    email_regex = r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"

    if not url.startswith('http'):
        url = 'https://' + url

    try:
        response = requests.get(url, headers=headers, verify=False)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            email_match = re.search(email_regex, response.text)
            if email_match:
                return email_match.group()

            impressum_link = soup.find('a', string=re.compile(r'impressum', re.I))
            if impressum_link:
                impressum_url = impressum_link.get('href')
                if impressum_url and not impressum_url.startswith('http'):
                    impressum_url = url + impressum_url

                response = requests.get(impressum_url, headers=headers, verify=False)
                if response.status_code == 200:
                    impressum_soup = BeautifulSoup(response.content, 'html.parser')
                    new_emails = set(re.findall(email_regex, response.text))
                    new_emails = [email for email in new_emails if email.endswith('.com') or email.endswith('.net') or email.endswith('.de')]
                    if new_emails:
                        email = new_emails[0]
                        return email

            contact_link = soup.find('a', string=re.compile(r'contact', re.I))
            if contact_link:
                contact_url = contact_link.get('href')
                if contact_url and not contact_url.startswith('http'):
                    contact_url = url + contact_url

                response = requests.get(contact_url, headers=headers, verify=False)
                if response.status_code == 200:
                    contact_soup = BeautifulSoup(response.content, 'html.parser')
                    new_emails = set(re.findall(email_regex, response.text))
                    new_emails = [email for email in new_emails if email.endswith('.com') or email.endswith('.net') or email.endswith('.de')]
                    if new_emails:
                        email = new_emails[0]
                        return email

    except requests.exceptions.RequestException as e:
        print(f"Error accessing URL: {url}")
        print(f"Error message: {str(e)}")
        
    return None


def main():
    df = pd.read_excel("Leadquelle.xlsx")
    for index, row in df.head(30).iterrows():
        if pd.notnull(row['Website']):
            url = row['Website']
            email = extract_email(url)
            df.at[index, 'Email1'] = email
            print(f"Processed row {index + 1}")
    df.to_excel("Leadquelle.xlsx", index=False)


if __name__ == "__main__":
    main()