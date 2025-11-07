# 🎓 Tutorial: Jak Rozwiązać Zadanie Phishing

## 🔍 Krok 1: Analiza Strony

### 1.1 Otwórz stronę w przeglądarce
```bash
# Uruchom lokalny serwer
python -m http.server 8000
# Lub otwórz bezpośrednio plik login_page.html
```

### 1.2 Sprawdź wygląd strony
- Czy wygląda jak prawdziwa strona banku?
- Czy logo wygląda na autentyczne?
- Czy URL wygląda podejrzanie?

## 🛠️ Krok 2: Inspekcja Kodu Źródłowego

### 2.1 Otwórz narzędzia deweloperskie
- **Chrome/Edge**: F12 lub Ctrl+Shift+I
- **Firefox**: F12 lub Ctrl+Shift+I
- **Safari**: Cmd+Option+I

### 2.2 Przejdź do zakładki "Sources" lub "Źródła"
- Sprawdź plik login_page.html
- Przejrzyj style.css
- Sprawdź czy jest jakiś JavaScript

### 2.3 Szukaj komentarzy HTML
```html
<!-- To jest komentarz HTML -->
<!-- CTF{phish_detected_2024} -->
```

## 🔎 Krok 3: Znajdowanie Flagi

### 3.1 Metody ukrywania flagi:
1. **Komentarze HTML**: `<!-- flag -->`
2. **Zmienne JavaScript**: `var flag = "CTF{...}"`
3. **Atrybuty HTML**: `<div data-flag="CTF{...}">`
4. **Ukryte elementy**: `<input type="hidden" value="flag">`
5. **Kod zakodowany**: Base64, ROT13, etc.

### 3.2 Praktyczne wskazówki:
- Użyj funkcji "Find" (Ctrl+F) i szukaj: `CTF{`
- Sprawdź każdy plik osobno
- Nie zapominaj o plikach CSS!
- Sprawdź komentarze w każdym pliku

## 🎯 Krok 4: Identyfikacja Elementów Phishingowych

### 4.1 Wizualne oznaki:
- **Logo**: Nieznana marka "SecureBank"
- **URL**: Podejrzany adres strony
- **Błędy**: Literówki, złe formatowanie
- **Brak certyfikatu**: Brak https://

### 4.2 Techniczne oznaki:
- **Proste formularze**: Bez walidacji
- **Brak zabezpieczeń**: CAPTCHA, 2FA
- **Słaba jakość kodu**: Błędy JavaScript
- **Ukryte elementy**: Podejrzane divy

## 📝 Krok 5: Dokumentowanie Znalezionych Elementów

### 5.1 Zapisz swoje obserwacje w phishing_indicators.txt:
```
Element: Logo
Lokalizacja: login_page.html, linia 15
Opis: Używa "SecureBank" zamiast prawdziwej nazwy banku
Powód podejrzenia: Podmiana marki
```

## 🚨 Najczęstsze Pułapki

1. **Nie szukaj tylko w jednym pliku** - sprawdź wszystkie
2. **Nie ignoruj komentarzy** - często tam są ukryte flagi
3. **Sprawdzaj uważnie** - flaga może być podzielona
4. **Użyj narzędzi** - funkcja "Find" w edytorze
5. **Myśl kreatywnie** - flaga może być w nietypowych miejscach

## 💡 Dodatkowe Wskazówki

### Narzędzia pomocnicze:
- **Edytory**: VS Code, Sublime Text
- **Przeglądarki**: Chrome, Firefox z DevTools
- **Hex edytor**: Do sprawdzenia plików binarnych
- **Terminal**: grep, find do wyszukiwania

### Komendy terminala:
```bash
# Szukaj flagi w plikach
grep -r "CTF{" .

# Znajdź komentarze HTML
grep -r "<!--" .

# Sprawdź wszystkie pliki
find . -type f -name "*.html" -o -name "*.css" -o -name "*.js"
```

## 🎉 Kiedy Znalazłeś Flagę?

1. **Sprawdź format**: `CTF{phish_detected_2024}`
2. **Dokumentuj** gdzie ją znalazłeś
3. **Przeanalizuj** jak była ukryta
4. **Zapisz** w pliku flag.txt

## 📚 Dalsza Nauka

Po ukończeniu zadania:
- Przeczytaj artykuły o phishingu
- Naucz się rozpoznawać prawdziwe strony banków
- Sprawdź jak działają narzędzia anty-phishing
- Eksperymentuj z własnymi przykładami

---

**Powodzenia! 🚀🔍**