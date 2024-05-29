import requests
import json
import os

class ChatSession:
    def __init__(self, url, model, stream=False, markdown=True, options=None):
        self.url = url
        self.model = model
        self.stream = stream
        self.markdown = markdown
        self.options = options if options else {}
        self.history = []

    def _send_request(self, prompt):
        # Konversationsverlauf in den Kontext einbeziehen
        context = [entry['user'] + "\n" + entry['bot'] for entry in self.history]
        context.append(prompt)
        full_prompt = "\n".join(context)
        
        payload = {
            "prompt": full_prompt,
            "model": self.model,
            "stream": self.stream,
            "markdown": self.markdown,
            "options": self.options  # Standardmäßig leer, es sei denn, im Menü gesetzt
        }
        response = requests.post(self.url, json=payload)
        response.raise_for_status()
        return response.json()

    def send_message(self, message):
        response = self._send_request(message)
        if 'response' in response:
            self.history.append({"user": message, "bot": response["response"]})
            return response["response"]
        else:
            error_message = "Error: 'response' key not found in the response."
            self.history.append({"user": message, "bot": error_message})
            return error_message

    def get_history(self):
        return self.history

    def export_history(self, filename):
        # Kontext in die Datei einbeziehen
        context = [entry['user'] + "\n" + entry['bot'] for entry in self.history]
        full_context = "\n".join(context)

        data = {
            "history": self.history,
            "context": full_context
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def load_history(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                data = json.load(f)
                self.history = data.get("history", [])
        else:
            print(f"File {filepath} does not exist.")

    def toggle_markdown(self, enable):
        self.markdown = enable
