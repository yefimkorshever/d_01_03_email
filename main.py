import os
import smtplib

sample = """Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл. """

website = 'https://dvmn.org/referrals/EUfuXLkHgm9z02b0XHbzc4ar4PwWK4Gc49qeWf8K/'
friend_name = 'Денис'
sender_name = 'Ефим'

sample = sample.replace('%website%', website)
sample = sample.replace('%friend_name%', friend_name)
sample = sample.replace('%my_name%', sender_name)

from_address = 'inokentyshnipperson@yandex.ru'
to_address = 'yefim_korshever@mail.ru'
subject = 'Приглашение!'
content_type = 'text/plain; charset="UTF-8";'
letter = """\
From: {from_address}
To: {to_address}
Subject: {subject}
Content-Type: {content_type}

{sample}
"""

letter = letter.format(from_address = from_address, to_address = to_address, subject = subject, content_type = content_type, sample = sample)

letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
login = os.environ['YA_LOGIN']
password = os.environ['YA_PASS']
server.login(login, password)
server.sendmail(from_address, to_address, letter)
server.quit()
