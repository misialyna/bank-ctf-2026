# 🎣 Zadanie Phishing - Fałszywy Bank "SecureBank"

## 📋 Opis Zadania

Otrzymałeś podejrzaną wiadomość e-mail z linkiem do strony logowania banku. Podejrzewasz, że to może być phishing. Twoim zadaniem jest:

1. **Zidentyfikowanie elementów phishingowych** w podanej stronie
2. **Znalezienie ukrytej flagi** w kodzie strony
3. **Analiza bezpieczeństwa** strony logowania

## 🎯 Cel Zadania

- Poziom: **Średni-Trudny**
- Znajdź flagę ukrytą w kodzie HTML/JavaScript
- Zidentyfikuj wszystkie oznaki phishingu
- Czas wykonania: 30-45 minut

## 🚀 Instrukcje Uruchomienia

### Opcja 1: Serwer Lokalny (Python)
```bash
# W katalogu phishing_bank/
python -m http.server 8000
# Otwórz: http://localhost:8000/login_page.html
```

### Opcja 2: GitHub Pages
1. Utwórz nowe repozytorium na GitHub
2. Wgraj wszystkie pliki z katalogu `phishing_bank/`
3. Włącz GitHub Pages w ustawieniach repozytorium
4. Strona będzie dostępna pod: `https://username.github.io/nazwa-repozytorium/login_page.html`

### Opcja 3: Serwer HTTP (Node.js)
```bash
# Instaluj http-server globalnie
npm install -g http-server

# W katalogu phishing_bank/
http-server -p 8000
# Otwórz: http://localhost:8000/login_page.html
```

## 🔍 Zadanie CTF

### Część 1: Analiza Strony
1. Otwórz plik `login_page.html` w przeglądarce
2. Sprawdź źródło strony (F12 → Sources/Źródła)
3. Przeanalizuj elementy wskazujące na phishing
4. Zapisz swoje obserwacje w pliku `phishing_indicators.txt`

### Część 2: Znajdowanie Flagi
- Flaga jest ukryta w kodzie HTML/JavaScript
- Może być w komentarzach, atrybutach, funkcjach
- Sprawdź wszystkie pliki: HTML, CSS, JS
- Wzór flagi: `CTF{phish_detected_2024}`

## 🛠️ Wskazówki do Rozwiązania

1. **Inspektor Elementów**: Użyj F12 aby sprawdzić kod źródłowy
2. **Komentarze HTML**: Szukaj komentarzy z flagą
3. **JavaScript**: Sprawdź funkcje i zmienne
4. **Ukryte elementy**: Sprawdź ukryte divy, inputy
5. **Atopybuty**: Zwróć uwagę na nietypowe atrybuty

## ✅ Kompletne Rozwiązanie

### Oznaczenia Phishingu Znalezione w Stronie:

1. **Logo banku**: Używa "SecureBank" zamiast prawdziwej nazwy banku
2. **URL podejrzany**: Brak https i prawdziwego certyfikatu
3. **Forma danych**: Proste formularze bez zabezpieczeń
4. **Brak informacji o bezpieczeństwie**: Brak certyfikatów SSL
5. **Język**: Puste komunikaty po polsku z błędami
6. **Ukryty kod**: Flagę znaleziono w komentarzu HTML

### Flaga:
```
CTF{phish_detected_2024}
```

### Gdzie znaleziono flagę:
- W komentarzu HTML w sekcji `<head>` strony
- Ukryta między tagami meta
- Maskowana jako część kodu

## 📁 Struktura Plików

```
phishing_bank/
├── README.md                    # Ten plik
├── README_tutorial.md           # Dodatkowe wskazówki
├── flag.txt                     # Flaga CTF
├── login_page.html              # Główna strona phishingowa
├── style.css                    # Style CSS strony
├── phishing_indicators.txt      # Lista elementów phishingowych
└── securebank_logo.png          # Logo "SecureBank"
```

## 🎓 Wiedza Edukacyjna

Ten projekt ma na celu edukację w zakresie:
- **Rozpoznawanie phishingu**
- **Bezpieczeństwo internetowe**
- **Analiza kodu źródłowego**
- **Metody ataków socjotechnicznych**

## ⚠️ Ostrzeżenie

Ta strona jest stworzona wyłącznie w celach edukacyjnych dla CTF.
**NIE UŻYWAJ** do celów przestępczych!

---

**Powodzenia w rozwiązywaniu zadania! 🔍🔐**