# app.py
import os
from flask import Flask, request, redirect, session, url_for, make_response
from markupsafe import escape
import sys

# Wczytujemy wartości z ENV — BEZ POLEGANIA na stałych w kodzie.
VALID_USERNAME = os.environ.get("CTF_VALID_USERNAME")
VALID_PASSWORD = os.environ.get("CTF_VALID_PASSWORD")
SERVER_FLAG = os.environ.get("CTF_SERVER_FLAG")
APP_SECRET = os.environ.get("FLASK_APP_SECRET")

if not (VALID_USERNAME and VALID_PASSWORD and SERVER_FLAG):
    sys.stderr.write(
        "ERROR: brak wymaganych zmiennych środowiskowych.\n"
        "Ustaw CTF_VALID_USERNAME, CTF_VALID_PASSWORD oraz CTF_SERVER_FLAG przed uruchomieniem.\n"
    )
    sys.exit(1)

# Jeśli nie ustawiono APP_SECRET, generujemy tymczasowy ale dokumentujemy, że lepiej ustawić go ręcznie.
if not APP_SECRET:
    import secrets
    APP_SECRET = secrets.token_urlsafe(32)
    sys.stderr.write("WARNING: FLASK_APP_SECRET nie ustawiony — używany tymczasowy sekret sesji.\n")

app = Flask(__name__, static_folder='.', static_url_path='')  # statyczne pliki są w tym samym katalogu
app.secret_key = APP_SECRET

INDEX_PAGE = "index.html"  # plik HTML w katalogu projektu

@app.route("/")
def index():
    # Zwracamy plik index.html z katalogu roboczego (gdzie uruchomisz app)
    if not os.path.exists(INDEX_PAGE):
        return "Brak pliku index.html w katalogu aplikacji.", 500
    with open(INDEX_PAGE, 'rb') as f:
        data = f.read()
    resp = make_response(data)
    resp.headers['Content-Type'] = 'text/html; charset=utf-8'
    return resp

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # Walidacja po stronie serwera — porównanie z ENV
    if username == VALID_USERNAME and password == VALID_PASSWORD:
        session['logged_in'] = True
        session['user'] = username
        return redirect(url_for('secret'))
    else:
        # brak limitów prób — po prostu przekierowujemy z parametrem informującym o błędzie
        return redirect(url_for('index') + "?error=1")

@app.route("/secret")
def secret():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    user = escape(session.get('user', ''))
    # FLAGA jest pobierana z ENV — nigdy nie jest zapisana w plikach frontu
    flag = SERVER_FLAG
    html = f"""<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SecureBank - Sekret</title>
<link rel="stylesheet" href="/style.css">
</head>
<body>
  <div class="login-container">
    <h1>Dostęp przyznany</h1>
    <p>Witaj, {user}. Pomyślnie zalogowano do ukrytej sekcji.</p>
    <div class="flag-box">
      <h2>Twoja flaga CTF (serwerowa):</h2>
      <pre style="font-size:18px; font-weight:600;">{flag}</pre>
    </div>
    <p><a href="{url_for('logout')}">Wyloguj</a></p>
  </div>
</body>
</html>"""
    resp = make_response(html)
    resp.headers['Content-Type'] = 'text/html; charset=utf-8'
    return resp

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == "__main__":
    # Domyślnie uruchom lokalnie
    app.run(host="127.0.0.1", port=5000, debug=False)
