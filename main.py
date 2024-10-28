# main.py

from controller import SendEmailController
import os
import schedule
import time
import datetime as dt

# Dados do e-mail
MY_EMAIL = "carlosmiguelromao@gmail.com"
PASSWORD = "fsem acem gxeq zxrq"
SEND_EMAIL = "cmromao@randstad.pt"


def job():
    # Verifica se é um dia útil
    today = dt.datetime.now().date()
    if today.weekday() < 5:  # 0 = Segunda-feira, 4 = Sexta-feira
        if MY_EMAIL and PASSWORD:
            controller = SendEmailController()
            controller.send_quote_email(my_email=MY_EMAIL,
                                        password=PASSWORD,
                                        recipient_email=SEND_EMAIL)
        else:
            print("Credenciais de e-mail ausentes. Configure as variáveis de ambiente MY_EMAIL e MY_PASSWORD.")


# Agendar para 09h30 de todos os dias úteis
schedule.every().monday.at("09:30").do(job)
schedule.every().tuesday.at("09:30").do(job)
schedule.every().wednesday.at("09:30").do(job)
schedule.every().thursday.at("09:30").do(job)
schedule.every().friday.at("09:30").do(job)

# Loop que mantém o agendamento ativo
if __name__ == "__main__":
    while True:
        schedule.run_pending()  # Verifica se há alguma tarefa agendada para executar
        time.sleep(60)          # Verifica a cada 60 segundos




