def ya300(url):
  '''
  Краткий перезсказ статей и видео от Яндекса.
  Отправка ссылки и получение ответа в виде списка из пунктов с кратким пересказом
  с помощью сервиса Яндекс 300.
  '''
    # блок кода передачи ссылки
    endpoint = 'https://300.ya.ru/api/sharing-url'
    response = requests.post(
        endpoint,
        json = {
          'article_url': url
        },
        headers = {'Authorization': 'OAuth <замените на собственный токен от Яндекса>'} # подробнее https://oauth.yandex.ru/
    )
   
    # блок кода ответа в структурированном виде и ссылки на результат
    final_response = requests.get(response.json()['sharing_url']) # GET-запрос
    soup = BeautifulSoup(final_response.content.decode('utf-8'), 'lxml')

    # краткий пересказ в виде списка из пунктов
    text = []
    for item in soup.find('div', attrs={'class':'summary-scroll'}).find_all('li'):
        try:
            text.append(item.find('h2').text.strip())
        except:
            pass
        for subitem in item.find_all('li'):
            text.append(subitem.text.strip('\xa0\u2009 '))
    
    return (
            text, # результат в виде списка
            response.json()['sharing_url'] # ссылка на краткий пересказ в яндекс сервисе
           )
