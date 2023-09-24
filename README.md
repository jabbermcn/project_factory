Описание
С помощью Django и Django REST Framework написать API для приёма сообщений и отправки их в Telegram бот.
Функционал готового задания должен выглядеть следующим образом: через API получаем сообщение, его потом отправляем в
Telegram бот.

Схема работы:
1. Пользователь регистрируется в нашей системе. При регистрации указывает логин, пароль и имя
2. Пользователь находит бота в Telegram и подписывается на него. На этом этапе требуется создать Telegram бота.
3. В личном кабинете генерирует токен и привязывает этот токен к своему чату. Простой способ реализации: любое входящее
   сообщение от пользователя бот запоминает как токен пользователя
4. Пользователь отправляет на API своё сообщение. В этот момент бот сразу дублирует его в Telegram. Пользователь должен
   получать только свои сообщения.
   Формат сообщения:
   {Имя пользователя}, я получил от тебя сообщение: {Сообщение}
   Сообщение должно идти с новой строки.
   Функционал:
1. Авторизация
2. Регистрация
3. Генерация токена для телеграм бота. (Только после авторизации)
4. Отправка сообщений своему боту. На сервере фиксировать: дату и тело
   сообщения. (Только после авторизации)
5. Получение списка всех сообщений: дата отправки, сообщение (Только после
   авторизации)
   Функционал выше должен работать через REST API.
_____________________________________
http://127.0.0.1:8000/api/register/  POST - регистрация пользователя
_____________________________________
http://127.0.0.1:8000/api/auth/login/ POST - получение токена авторизации
_____________________________________
http://127.0.0.1:8000/api/send_message/ POST - отправка сообщений
_____________________________________
http://127.0.0.1:8000/api/get_messages/ GET - получение списка всех сообщений
_____________________________________