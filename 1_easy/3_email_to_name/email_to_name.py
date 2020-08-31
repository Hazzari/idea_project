"""
3. Сегментация адреса электронная почты

Идея проекта. Сегментация адреса электронной почты — это полезная
программа для получения имени пользователя и имени домена из e-mail.
Вы можете настроить и отправить сообщение пользователю с этой информацией.

"""
import argparse
import smtplib
from email.mime.text import MIMEText
from email.header import Header

parser = argparse.ArgumentParser()

parser.add_argument('--sender', '-s',
                    action='store',
                    help='Введите email отправителя',
                    required=True)

parser.add_argument('--receiver', '-r',
                    action='store',
                    help='Введите email получателя',
                    required=True)

parser.add_argument('--messages', '-m',
                    action='store',
                    nargs='+',
                    help='Сообщение в формате -w "текст" ',
                    required=False)

args = parser.parse_args()

name_receiver = args.receiver.split("@")[0].capitalize()

# Настройки
mail_sender = f'{args.sender}'
mail_receiver = f'{args.receiver}'
password = input('Пароль')

server = smtplib.SMTP_SSL(host='smtp.yandex.ru', port=465)

# Формируем тело письма
subject = u'Тестовый email от ' + mail_sender
body = u'Здравствуйте уважаемый {}.\n' \
       u'Это тестовое письмо отправлено с помощью smtplib.\n' \
       u'Сообщение для вас: "{}"'.format(name_receiver, args.messages[0])
msg = MIMEText(body, 'plain', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')

# Отправляем письмо
server.ehlo()
server.login(mail_sender, password)
server.sendmail(mail_sender, mail_receiver, msg.as_string())
server.quit()

# TODO: Добавить выбор smtp
# TODO: Добавить ввод пароля
# TODO: error