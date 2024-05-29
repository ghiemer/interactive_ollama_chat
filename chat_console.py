import json
from chat_session import ChatSession

def load_config(filepath):
    with open(filepath, 'r') as f:
        config = json.load(f)
    return config

def load_options(filepath):
    with open(filepath, 'r') as f:
        options = json.load(f)
    return options

def save_config(filepath, config):
    with open(filepath, 'w') as f:
        json.dump(config, f, indent=4)

def display_options(options):
    for key, value in options.items():
        print(f"{key}: {value}")

def modify_options(options):
    while True:
        print(print_colored("Settings:", "yellow"))
        display_options(options)
        user_input = input("Geben Sie den Namen der Option ein, die Sie ändern möchten (oder 'done' zum Beenden): ")

        if user_input.lower() == 'done':
            break

        if user_input in options:
            new_value = input(f"Geben Sie den neuen Wert für {user_input} ein: ")
            try:
                # Versuchen, den Wert in den richtigen Typ umzuwandeln
                if isinstance(options[user_input], bool):
                    options[user_input] = new_value.lower() in ('true', '1', 'yes')
                elif isinstance(options[user_input], int):
                    options[user_input] = int(new_value)
                elif isinstance(options[user_input], float):
                    options[user_input] = float(new_value)
                else:
                    options[user_input] = new_value
            except ValueError:
                print("Ungültiger Wert. Bitte versuchen Sie es erneut.")
        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")

def print_colored(text, color):
    colors = {
        "green": "\033[92m",
        "yellow": "\033[93m",
        "reset": "\033[0m"
    }
    return f"{colors[color]}{text}{colors['reset']}"

def main():
    config = load_config('config.json')
    options = load_options('options.json')
    chat = ChatSession(url=config['url'], model=config['model'], stream=config.get('stream', False), markdown=config.get('markdown', True), options=options)

    print("Willkommen im interaktiven Chat. Geben Sie Ihre Nachrichten ein.")
    print("Verwenden Sie /quit zum Beenden, /export 'name' zum Exportieren, /load 'pfad_zur_datei' zum Laden, /options zum Ändern der Optionen, /settings zum Ändern der Einstellungen während der Sitzung und /markdown true|false zum Umschalten von Markdown.")

    while True:
        user_input = input(print_colored("Sie: ", "green"))

        if user_input.startswith("/quit"):
            print("Chat beendet.")
            break
        elif user_input.startswith("/export"):
            _, filename = user_input.split(maxsplit=1)
            chat.export_history(filename)
            print(f"Konversation in {filename} exportiert.")
        elif user_input.startswith("/load"):
            _, filepath = user_input.split(maxsplit=1)
            chat.load_history(filepath)
            print(f"Konversation von {filepath} geladen.")
        elif user_input.startswith("/options"):
            modify_options(options)
            save_config('options.json', options)
            print("Optionen aktualisiert.")
        elif user_input.startswith("/settings"):
            modify_options(options)
            print("Optionen während der Sitzung aktualisiert.")
        elif user_input.startswith("/markdown"):
            _, state = user_input.split(maxsplit=1)
            if state.lower() == "true":
                chat.toggle_markdown(True)
                print("Markdown aktiviert.")
            elif state.lower() == "false":
                chat.toggle_markdown(False)
                print("Markdown deaktiviert.")
            else:
                print("Ungültiger Befehl. Verwenden Sie true oder false.")
        else:
            response = chat.send_message(user_input)
            print(print_colored("Bot: " + response, "yellow"))

if __name__ == "__main__":
    main()
