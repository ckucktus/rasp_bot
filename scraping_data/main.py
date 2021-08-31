import aiohttp
from bs4 import BeautifulSoup



HEADERS = {
'Host': 'rasp.uatk.ru',
'Connection': 'keep-alive',
'Upgrade-Insecure-Requests': '1',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.60 YaBrowser/20.12.0.963 Yowser/2.5 Safari/537.36',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'ru,en;q=0.9'
}

_tokens = {
'group': 'С1-17',
#'date': '2021-01-04'
}


async def _token_parser(resp, data_time):
    html_get = await resp.content.read()
    soup_get = BeautifulSoup(html_get, 'html.parser')
    item = soup_get.find(name='meta', attrs={'name':'csrf-token'})
    csrf_token_get = item.get('content')
    _tokens['date'] = data_time
    _tokens['_token'] = csrf_token_get



async def POST(session):
    async with session.post('http://rasp.uatk.ru/students', allow_redirects=True, headers=HEADERS,
                            data=_tokens) as resp_post:
        return await resp_post.content.read()


async def main(data_time):
    async with aiohttp.ClientSession() as session:
        async with session.get('http://rasp.uatk.ru/students') as resp:
            await _token_parser(resp, data_time)
            post_obj = await POST(session)
            return await parser_schedule(post_obj)

async def parser_schedule(something_resp_after_post):
    soup_post = BeautifulSoup(something_resp_after_post, 'lxml')
    tbody = soup_post.find(name='tbody')
    rasp=''
    if not tbody:
        return "Расписания нет"
    else:
        for child in tbody.children:
            if child.name == 'tr':
                count=0
                for item in child.children:
                    if item != '\n':
                        if count==1:
                            rasp += item.string + '\n'
                        if count==2:
                            rasp += item.string + '\n'
                        if count==5: #доп условие ибо кабинета может не быть
                            rasp += f'Кабинет: {item.string}' + '\n'               #проставить экраны
                        count+=1
                else:
                    rasp+='\n'
    return rasp



