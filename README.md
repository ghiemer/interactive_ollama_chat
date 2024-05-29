# Interaktiver Chat mit KI-Modell

Dieses Projekt ermöglicht interaktive Unterhaltungen mit einem KI-Modell. Es unterstützt das Laden und Speichern von Konversationen sowie das Anpassen von Modelloptionen.

## Installation

1. **Klonen Sie das Repository:**
   ```sh
   git clone https://github.com/your-repo/interactive-chat.git
   cd interactive-chat
   ```

2. **Installieren Sie die erforderlichen Pakete:**
   ```sh
   pip install -r requirements.txt
   ```

3. **Erstellen Sie eine `.env`-Datei im Projektverzeichnis:**
   ```plaintext
   # .env
   SERVER_URL=http://your_api_endpoint
   ```

## Konfigurationsdateien

### config.json

Diese Datei enthält die grundlegenden Einstellungen wie die URL des Endpunkts und den Modellnamen.

```json
{
    "model": "llama3",
    "stream": false,
    "markdown": true
}
```

### options.json

Diese Datei enthält spezifische Optionen für die Modellgenerierung. Nur die Optionen, die hier definiert sind, werden verwendet.

```json
{
    "num_predict": 100,
    "top_k": 20,
    "top_p": 0.9,
    "temperature": 0.8
}
```

## Nutzung

### Starten des Chats

Führen Sie das Hauptskript aus, um den interaktiven Chat zu starten:

```sh
python chat_console.py
```

### Befehle

- **/quit**: Beendet die Chat-Sitzung.
- **/export 'filename'**: Exportiert die aktuelle Konversation in eine Datei.
- **/load 'filepath'**: Lädt eine gespeicherte Konversation aus einer Datei.
- **/options**: Öffnet das Menü zum Ändern der Modelloptionen und speichert die Änderungen.
- **/settings**: Öffnet das Menü zum Ändern der Modelloptionen während der Sitzung.
- **/markdown true|false**: Aktiviert oder deaktiviert die Markdown-Unterstützung.

### Anpassung der Optionen

#### Vor der Sitzung

1. Geben Sie `/options` ein, um das Menü zur Anpassung der Optionen zu öffnen.
2. Geben Sie den Namen der Option ein, die Sie ändern möchten.
3. Geben Sie den neuen Wert für die Option ein.
4. Geben Sie `done` ein, um das Menü zu verlassen und die Änderungen zu speichern.

#### Während der Sitzung

1. Geben Sie `/settings` ein, um das Menü zur Anpassung der Optionen während der Sitzung zu öffnen.
2. Geben Sie den Namen der Option ein, die Sie ändern möchten.
3. Geben Sie den neuen Wert für die Option ein.
4. Geben Sie `done` ein, um das Menü zu verlassen und die Änderungen anzuwenden.

### Beispiel einer Chat-Sitzung

```
Willkommen im interaktiven Chat. Geben Sie Ihre Nachrichten ein.
Verwenden Sie /quit zum Beenden, /export 'name' zum Exportieren, /load 'pfad_zur_datei' zum Laden, /options zum Ändern der Optionen, /settings zum Ändern der Einstellungen während der Sitzung und /markdown true|false zum Umschalten von Markdown.
Sie: Hallo
Bot: Hallo! Wie kann ich Ihnen heute helfen?
```

## Farbliche Darstellung

- **Du:** Eingaben des Benutzers werden grün dargestellt.
- **Bot:** Antworten des Bots werden gelb dargestellt.
- **Settings:** Das Menü zur Anpassung der Optionen wird in Gelb dargestellt.

## Anpassung der Optionen

Hier sind die verfügbaren Optionen mit ihren Standardwerten:

- **num_predict**: 50
- **top_k**: 0
- **top_p**: 1.0
- **temperature**: 1.0
- **repeat_penalty**: 1.0
- **presence_penalty**: 0.0
- **frequency_penalty**: 0.0
- **mirostat**: 0
- **penalize_newline**: False
- **stop**: []
- **num_ctx**: 1024
- **num_batch**: 1
- **num_gpu**: 0
- **low_vram**: False
- **f16_kv**: False
- **vocab_only**: False
- **use_mmap**: False
- **use_mlock**: False
- **num_thread**: 1

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert. Weitere Informationen finden Sie in der LICENSE