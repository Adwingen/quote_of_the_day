# controller.py

import smtplib
import datetime as dt
from model import DataModel
from view import View


class SendEmailController:
    def __init__(self):
        self.model = DataModel()
        self.view = View()
        self.today_date = dt.datetime.now().date()

    def send_quote_email(self, my_email, password, recipient_email):
        """Envia uma citação aleatória por e-mail."""
        quote_text, author = self.model.select_random_quote()

        if quote_text and author:
            # Formata a mensagem e envia o e-mail
            message = self.view.format_email(quote_text, author, self.today_date)
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=my_email, password=password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=recipient_email,
                                    msg=message)
            # Exibe no console
            self.view.display_quote(quote_text, author)
        else:
            print("All quotes have been used. No new quotes available.")
