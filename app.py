from email import message
from flask import Flask, render_template, request
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

def get_gspread_client():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    client = gspread.authorize(creds)
    return client

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        client = get_gspread_client()
        sheet = client.open('JUSC').sheet1
        row = [request.form['name'], request.form['email'], request.form['phone'], request.form['message']]

        sheet.append_row(row)
        return render_template('home.html', msg='Thank you for your message!')
    return render_template('contact.html')

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)