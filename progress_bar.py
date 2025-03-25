# цикл, в котором отслеживается статус процент выполненных интераций и оценка по длительности по времени
# Пример вывода информации статус бара
'''
Оценочное время выполнения: 12 мин и 7 сек.
Оставшееся время: 630 сек. Выполнено: 13%. Успешно: https://zakupki.gov.ru/epz/customer223/organization/customerRegistry/view.html?id=537250            
Элемент 162 из 1211: проблема list index out of range в https://zakupki.gov.ru/epz/customer223/search/results.html?morphology=on&search
Оставшееся время: 0 сек. Выполнено: 100%. Успешно: https://zakupki.gov.ru/epz/customer223/organization/customerRegistry/view.html?id=376071             
Длительность парсинга: 26 мин 0 сек.
Успешно проанализированных ссылок: 1204; неудачных: 8.
'''

# импорт библиотек
import time
import random

# служебные строки кода
total_count = 100 # Заменить на свой. Счетчик для статуса парсинга (сделано из ...)
start_time = time.time() # время старта процесса
newline = False # первое состояние переключателя новой строки
sleep_time = 0,.5 # установка времени сна парсинга
approximate_duration = sleep_time[1] * total_count * 1.2 # приблизительное время выполнения с учетом кэффициента погрешности
print(f'Оценочное время выполнения: {round(approximate_duration // 60)} мин и {round(approximate_duration % 60)} сек.')

# Списки для сохранения результата
failed_parsed_url_list = [] # список с неудачной попыткой парсинга

for index in range(total_count):
    time.sleep(random.uniform(sleep_time[0], sleep_time[1])) # отложенное время операций парсинга 0-0,5 сек. (более естественное по времени запросы, чтобы не блокировали)
    try:
        # Основное тело цикла
        
        # статус процесса парсинга успешных попыток
        processing_status = (index + 1) / total_count # сколько выполнено
        approximate_left_time = approximate_duration * (1 - processing_status) # приблизительное время выполнения
        print(f'Оставшееся время: {approximate_left_time:.0f} сек. Выполнено: {processing_status:.0%}. Успешно: {customer_url:<100}', end='\r')
        newline = True
    
    except Exception as err: # в случаи ошибки: логирование
        failed_parsed_url_list.append(customer_url) # добавление url в лист с неудачные попытками парсинга (для повторной попытки парсинга)

        # статус процесса парсинга неудачных попыток
        if newline: print()
        print(f'\033[31mЭлемент {index} из {total_count - 1}: проблема {err} в {url}\033[0m', end='\r\n')
        newline = False


# длительность парсинга по времени
duration_time = round(time.time() - start_time) # время в сек
print()
print(f'Длительность парсинга: {duration_time // 60} мин {duration_time % 60} сек.')
print(f'Успешно проанализированных ссылок: {inn_okved_df['customer_okved'].count()}; неудачных: {len(failed_parsed_url_list)}.')
