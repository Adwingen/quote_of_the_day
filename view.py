# view.py

class View:
    @staticmethod
    def display_quote(quote_text, author):
        """Exibe a citação e o autor no console."""
        print(f"Quote of the Day:\n'{quote_text}' - {author}")

    @staticmethod
    def format_email(quote_text, author, date):
        """Formata a mensagem para envio por e-mail."""
        return f"Subject: Quote of the Day {date}\n\n{quote_text}\n\n- {author}"
