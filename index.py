#!/usr/bin/env python3
from YT_audio import yt_pobieracz
from flask import Flask, render_template, request, send_from_directory, send_file

app = Flask(__name__)

@app.route('/')
def index():
    # This is our page for Flask app!
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload_text():

    print('[x] Server uruchomiony.')
    link = str(request.form['link'])
    nowa_nazwa = str(request.form['nowa_nazwa'])
    print('[-] nazwa i link utworu zapisany do pobrania')

    if request.method == 'POST':
        print('[-] Uruchamianie programu konerwującego...')
        yt_pobieracz(link, nowa_nazwa)
        print('[-] Plik przekonwertowany, pobieranie na serwer.')
    filen = f'{nowa_nazwa}.mp3'
    print('[-] Przygotowanie pliku do sciągniecia na dysk.')
    print('')

 #   send_from_directory(directory='', path=filename, as_attachment=True)

    return download_file(filen)
@app.route('/download')
def download_file(filen):
    print('[-] Sciaganie pliku....')
    print(f"[-] Plik pobrano pomyślnie do folderu Downloads pod nazwa -> [{filen}]")
    return send_file(filen, as_attachment=True)



app.run(debug=True, host='0.0.0.0')