from flask import Flask, request, render_template
import os
import json
import urllib.request

app = Flask(__name__)

# File paths
breach_data_file = 'leakdataset.txt'
common_passwords_url = 'https://www.ncsc.gov.uk/static-assets/documents/PwnedPasswordsTop100k.json'
common_passwords_file = 'common_passwords.json'

def load_breach_data(file_path):
    breach_data = []
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                email, password = line.split(':')
                breach_data.append({'email': email, 'password': password})
    return breach_data

def download_and_load_common_passwords(url, file_path):
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(data)
        with open(file_path, 'r', encoding='utf-8') as file:
            common_passwords = json.load(file)
        return common_passwords
    except Exception as e:
        print(f"Error loading common passwords: {e}")
        return []

try:
    breach_data = load_breach_data(breach_data_file)
    common_passwords = download_and_load_common_passwords(common_passwords_url, common_passwords_file)
except Exception as e:
    print(f"Error loading data: {e}")
    breach_data = []
    common_passwords = []

def check_email_breach(email, breach_data, common_passwords):
    results = [entry for entry in breach_data if entry['email'] == email]
    for result in results:
        result['sensitive'] = result['password'] in common_passwords
    return results

@app.route('/')
def index():
    return render_template('index2.html')

@app.route('/check', methods=['POST'])
def check():
    email = request.form['email']
    breach_results = check_email_breach(email, breach_data, common_passwords)
    if breach_results:
        breach_count = len(breach_results)
        sensitive_count = sum(result['sensitive'] for result in breach_results)
        return render_template('index2.html', email=email, results=breach_results, breach_count=breach_count, sensitive_count=sensitive_count)
    else:
        return render_template('index2.html', email=email, results=None, breach_count=0, sensitive_count=0)

if __name__ == '__main__':
    app.run(debug=True, port=5005)
