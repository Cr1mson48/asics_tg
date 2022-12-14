import requests
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from locale import atof

def main(alg, hashRate, power, power_cost, hashuint, rub=False):
    if rub == True:
        if power_cost != 0:
            data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            usd = data['Valute']['USD']['Value']
            power_cost = float(power_cost) / float(usd)

    driver = webdriver.Chrome()
    link = f'https://cryptocalc.online/ru/calculators/{alg}?hashRate={hashRate}&power={power}&powerCost={power_cost}&hashUnit={hashuint}&poolFee=0'
    print(link)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    #response = requests.get(link, headers=headers)
    #soup = BeautifulSoup(response.text, 'lxml')
    driver.implicitly_wait(30)
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    profit = []
    profit2 = []
    profit3 = []
    inf = soup.find_all('div', class_='tss-kk1978-calcTimeBlockPositive')
    neg = soup.find_all('div', class_='tss-dk2icf-calcTimeBlockNegative')
    inf2 = soup.find_all('div', class_='tss-aub44l-calcTimeBlock')
    bit = soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 tss-nd60qq-mainInfoPrice mui-1iv9rsj')
    print(inf)
    btc = 0
    #print(inf)
    for e in bit:
        print(e)
        btc = e.text.split(' ')[0]
    if not inf:
        for x in neg:
            profit.append(x.text.split('Прибыль')[1])
    else:
        for i in inf:
            profit.append(i.text.split('Прибыль')[1])
    for j in inf2:
        if 'Расходы' in j.text:
            z = j.text.split('.')
            z = '.'.join([z[1], z[2]])
            profit2.append(z)
    print(profit)
    print(profit2)

    if rub == True:
       if '-' in str(profit[0]):
           profit[0] = '-' + str(round(float(str(profit[0])[2:].replace(',', '')) * float(usd), 1))
       else:
           profit[0] = round(float(str(profit[0])[1:].replace(',', '')) * float(usd), 1)
       if '-' in str(profit[1]):
           profit[1] = '-' + str(round(float(str(profit[1])[2:].replace(',', '')) * float(usd), 1))
       else:
           profit[1] = round(float(str(profit[1])[1:].replace(',', '')) * float(usd), 1)
       if '-' in str(profit[2]):
           profit[2] = '-' + str(round(float(str(profit[2])[2:].replace(',', '')) * float(usd), 1))
       else:
           profit[2] = round(float(str(profit[2])[1:].replace(',', '')) * float(usd), 1)
       if '-' in str(profit[3]):
           profit[3] = '-' + str(round(float(str(profit[3])[2:].replace(',', '')) * float(usd), 1))
       else:
           profit[3] = round(float(str(profit[3])[1:].replace(',', '')) * float(usd), 1)
       profit2[0] = round(float(str(profit2[0])[1:].replace(',', '')) * float(usd), 1)
       profit2[1] = round(float(str(profit2[1])[1:].replace(',', '')) * float(usd), 1)
       profit2[2] = round(float(str(profit2[2])[1:].replace(',', '')) * float(usd), 1)
       profit2[3] = round(float(str(profit2[3])[1:].replace(',', '')) * float(usd), 1)
       output = f'''Профит за день: {profit[0]}₽
Профит за неделю: {profit[1]}₽
Профит за месяц: {profit[2]}₽
Профит за год: {profit[3]}₽
Расходы эл. за день: {profit2[0]}₽
Расходы эл. за неделю: {profit2[1]}₽
Расходы эл. за месяц: {profit2[2]}₽
Расходы эл. за год: {profit2[3]}₽
        '''

    else:
        output = f'''Профит за день: {profit[0]}
Профит за неделю: {profit[1]}
Профит за месяц: {profit[2]}
Профит за год: {profit[3]}
Расходы эл. за день: {profit2[0]}
Расходы эл. за неделю: {profit2[1]}
Расходы эл. за месяц: {profit2[2]}
Расходы эл. за год: {profit2[3]}
'''
    return output



def main2(alg, hashRate, power, power_cost, hashuint, rub=False):

    if rub == True:
        if power_cost != 0:
            data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            usd = data['Valute']['USD']['Value']
            power_cost = float(power_cost) / float(usd)
    driver = webdriver.Chrome()
    link = f'https://cryptocalc.online/ru/calculators/{alg}?hashRate={hashRate}&power={power}&powerCost={power_cost}&hashUnit={hashuint}&poolFee=0'
    print(link)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    #response = requests.get(link, headers=headers)
    #soup = BeautifulSoup(response.text, 'lxml')
    driver.implicitly_wait(30)
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    profit = []
    profit2 = []
    profit3 = []
    inf = soup.find_all('div', class_='tss-kk1978-calcTimeBlockPositive')
    neg = soup.find_all('div', class_='tss-dk2icf-calcTimeBlockNegative')
    inf2 = soup.find_all('div', class_='tss-aub44l-calcTimeBlock')
    bit = soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 tss-nd60qq-mainInfoPrice mui-1iv9rsj')
    print(inf)
    btc = 0
    #print(inf)
    for e in bit:
        print(e)
        btc = e.text.split(' ')[0]
    if not inf:
        for x in neg:
            profit.append(x.text.split('Прибыль')[1])
    else:
        for i in inf:
            profit.append(i.text.split('Прибыль')[1])
    for j in inf2:
        if 'Расходы' in j.text:
            z = j.text.split('.')
            z = '.'.join([z[1], z[2]])
            profit2.append(z)
    print(profit)
    print(profit2)

    if rub == True:
        if '-' in str(profit[0]):
            profit[0] = '-' + str(round(float(str(profit[0])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[0] = round(float(str(profit[0])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[1]):
            profit[1] = '-' + str(round(float(str(profit[1])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[1] = round(float(str(profit[1])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[2]):
            profit[2] = '-' + str(round(float(str(profit[2])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[2] = round(float(str(profit[2])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[3]):
            profit[3] = '-' + str(round(float(str(profit[3])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[3] = round(float(str(profit[3])[1:].replace(',', '')) * float(usd), 1)

        profit2[0] = round(float(str(profit2[0])[1:].replace(',', '')) * float(usd), 1)
        profit2[1] = round(float(str(profit2[1])[1:].replace(',', '')) * float(usd), 1)
        profit2[2] = round(float(str(profit2[2])[1:].replace(',', '')) * float(usd), 1)
        profit2[3] = round(float(str(profit2[3])[1:].replace(',', '')) * float(usd), 1)

        output = f'''Profit per day: {profit[0]}₽
Profit for the week: {profit[1]}₽
Profit for the month: {profit[2]}₽
Profit for the year: {profit[3]}₽
Electricity costs per day: {profit2[0]}₽
Electricity costs per week: {profit2[1]}₽
Electricity costs per month: {profit2[2]}₽
Electricity costs per year: {profit2[3]}₽
        '''
    else:
        output = f'''Profit per day: {profit[0]}
Profit for the week: {profit[1]}
Profit for the month: {profit[2]}
Profit for the year: {profit[3]}
Electricity costs per day: {profit2[0]}
Electricity costs per week: {profit2[1]}
Electricity costs per month: {profit2[2]}
Electricity costs per year: {profit2[3]}
    '''
    return output



def litecoin(alg, hashRate, power, power_cost, hashuint, rub=False):
    if rub == True:
        if power_cost != 0:
            data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            usd = data['Valute']['USD']['Value']
            power_cost = float(power_cost) / float(usd)
    driver = webdriver.Chrome()
    link = f'https://cryptocalc.online/ru/calculators/{alg}?hashRate={hashRate}&power={power}&powerCost={power_cost}&hashUnit={hashuint}&poolFee=0'
    link2 = f'https://cryptocalc.online/ru/calculators/dogecoin?hashRate={hashRate}&power={power}&powerCost={power_cost}&hashUnit={hashuint}&poolFee=0'

    print(link)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    # response = requests.get(link, headers=headers)
    # soup = BeautifulSoup(response.text, 'lxml')
    driver.implicitly_wait(30)
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    profit = []
    profit2 = []
    profit3 = []
    inf = soup.find_all('div', class_='tss-kk1978-calcTimeBlockPositive')
    neg = soup.find_all('div', class_='tss-dk2icf-calcTimeBlockNegative')
    inf2 = soup.find_all('div', class_='tss-aub44l-calcTimeBlock')
    bit = soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 tss-nd60qq-mainInfoPrice mui-1iv9rsj')
    print(inf)
    btc = 0
    # print(inf)
    for e in bit:
        print(e)
        btc = e.text.split(' ')[0]
    if not inf:
        for x in neg:
            profit.append(x.text.split('Прибыль')[1])
    else:
        for i in inf:
            profit.append(i.text.split('Прибыль')[1])
    for j in inf2:
        if 'Расходы' in j.text:
            z = j.text.split('.')
            z = '.'.join([z[1], z[2]])
            profit2.append(z)
    print(profit)
    print(profit2)

    if rub == True:
        if '-' in str(profit[0]):
            profit[0] = '-' + str(round(float(str(profit[0])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[0] = round(float(str(profit[0])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[1]):
            profit[1] = '-' + str(round(float(str(profit[1])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[1] = round(float(str(profit[1])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[2]):
            profit[2] = '-' + str(round(float(str(profit[2])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[2] = round(float(str(profit[2])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[3]):
            profit[3] = '-' + str(round(float(str(profit[3])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[3] = round(float(str(profit[3])[1:].replace(',', '')) * float(usd), 1)

        profit2[0] = round(float(str(profit2[0])[1:].replace(',', '')) * float(usd), 1)
        profit2[1] = round(float(str(profit2[1])[1:].replace(',', '')) * float(usd), 1)
        profit2[2] = round(float(str(profit2[2])[1:].replace(',', '')) * float(usd), 1)
        profit2[3] = round(float(str(profit2[3])[1:].replace(',', '')) * float(usd), 1)

        output = f'''Profit per day: {profit[0]}₽
    Profit for the week: {profit[1]}₽
    Profit for the month: {profit[2]}₽
    Profit for the year: {profit[3]}₽
    Electricity costs per day: {profit2[0]}₽
    Electricity costs per week: {profit2[1]}₽
    Electricity costs per month: {profit2[2]}₽
    Electricity costs per year: {profit2[3]}₽
            '''
    else:
        output = f'''Profit per day: {profit[0]}
    Profit for the week: {profit[1]}
    Profit for the month: {profit[2]}
    Profit for the year: {profit[3]}
    Electricity costs per day: {profit2[0]}
    Electricity costs per week: {profit2[1]}
    Electricity costs per month: {profit2[2]}
    Electricity costs per year: {profit2[3]}
        '''


    a1 = profit[0]
    a2 = profit[1]
    a3 = profit[2]
    a4 = profit[3]
    a5 = profit2[0]
    a6 = profit2[1]
    a7 = profit2[2]
    a8 = profit2[3]



    driver.implicitly_wait(30)
    driver.get(link2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    profit = []
    profit2 = []
    profit3 = []
    inf = soup.find_all('div', class_='tss-kk1978-calcTimeBlockPositive')
    neg = soup.find_all('div', class_='tss-dk2icf-calcTimeBlockNegative')
    inf2 = soup.find_all('div', class_='tss-aub44l-calcTimeBlock')
    bit = soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 tss-nd60qq-mainInfoPrice mui-1iv9rsj')
    print(inf)
    btc = 0
    # print(inf)
    for e in bit:
        print(e)
        btc = e.text.split(' ')[0]
    if not inf:
        for x in neg:
            profit.append(x.text.split('Прибыль')[1])
    else:
        for i in inf:
            profit.append(i.text.split('Прибыль')[1])
    for j in inf2:
        if 'Расходы' in j.text:
            z = j.text.split('.')
            z = '.'.join([z[1], z[2]])
            profit2.append(z)
    print(profit)
    print(profit2)

    if rub == True:
        if '-' in str(profit[0]):
            profit[0] = '-' + str(round(float(str(profit[0])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[0] = round(float(str(profit[0])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[1]):
            profit[1] = '-' + str(round(float(str(profit[1])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[1] = round(float(str(profit[1])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[2]):
            profit[2] = '-' + str(round(float(str(profit[2])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[2] = round(float(str(profit[2])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[3]):
            profit[3] = '-' + str(round(float(str(profit[3])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[3] = round(float(str(profit[3])[1:].replace(',', '')) * float(usd), 1)

        profit2[0] = round(float(str(profit2[0])[1:].replace(',', '')) * float(usd), 1)
        profit2[1] = round(float(str(profit2[1])[1:].replace(',', '')) * float(usd), 1)
        profit2[2] = round(float(str(profit2[2])[1:].replace(',', '')) * float(usd), 1)
        profit2[3] = round(float(str(profit2[3])[1:].replace(',', '')) * float(usd), 1)

        profit[0] = profit[0] + a1
        profit[1] = profit[1] + a2
        profit[2] = profit[2] + a3
        profit[3] = profit[3] + a4


        output = f'''Profit per day: {profit[0]}₽
Profit for the week: {profit[1]}₽
Profit for the month: {profit[2]}₽
Profit for the year: {profit[3]}₽
Electricity costs per day: {profit2[0]}₽
Electricity costs per week: {profit2[1]}₽
Electricity costs per month: {profit2[2]}₽
Electricity costs per year: {profit2[3]}₽
            '''
    else:

        profit[0] = profit[0] + ' + ' + a1
        profit[1] = profit[1] + ' + ' + a2
        profit[2] = profit[2] + ' + ' + a3
        profit[3] = profit[3] + ' + ' + a4


        output = f'''Profit per day: {profit[0]}
Profit for the week: {profit[1]}
Profit for the month: {profit[2]}
Profit for the year: {profit[3]}
Electricity costs per day: {profit2[0]}
Electricity costs per week: {profit2[1]}
Electricity costs per month: {profit2[2]}
Electricity costs per year: {profit2[3]}
        '''


    return output





def litecoin2(alg, hashRate, power, power_cost, hashuint, rub=False):
    if rub == True:
        if power_cost != 0:
            data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            usd = data['Valute']['USD']['Value']
            power_cost = float(power_cost) / float(usd)
    driver = webdriver.Chrome()
    link = f'https://cryptocalc.online/ru/calculators/{alg}?hashRate={hashRate}&power={power}&powerCost={power_cost}&hashUnit={hashuint}&poolFee=0'
    link2 = f'https://cryptocalc.online/ru/calculators/dogecoin?hashRate={hashRate}&power={power}&powerCost={power_cost}&hashUnit={hashuint}&poolFee=0'

    print(link)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
    # response = requests.get(link, headers=headers)
    # soup = BeautifulSoup(response.text, 'lxml')
    driver.implicitly_wait(30)
    driver.get(link)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    profit = []
    profit2 = []
    profit3 = []
    inf = soup.find_all('div', class_='tss-kk1978-calcTimeBlockPositive')
    neg = soup.find_all('div', class_='tss-dk2icf-calcTimeBlockNegative')
    inf2 = soup.find_all('div', class_='tss-aub44l-calcTimeBlock')
    bit = soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 tss-nd60qq-mainInfoPrice mui-1iv9rsj')
    print(inf)
    btc = 0
    # print(inf)
    for e in bit:
        print(e)
        btc = e.text.split(' ')[0]
    if not inf:
        for x in neg:
            profit.append(x.text.split('Прибыль')[1])
    else:
        for i in inf:
            profit.append(i.text.split('Прибыль')[1])
    for j in inf2:
        if 'Расходы' in j.text:
            z = j.text.split('.')
            z = '.'.join([z[1], z[2]])
            profit2.append(z)
    print(profit)
    print(profit2)

    if rub == True:
        if '-' in str(profit[0]):
            profit[0] = '-' + str(round(float(str(profit[0])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[0] = round(float(str(profit[0])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[1]):
            profit[1] = '-' + str(round(float(str(profit[1])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[1] = round(float(str(profit[1])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[2]):
            profit[2] = '-' + str(round(float(str(profit[2])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[2] = round(float(str(profit[2])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[3]):
            profit[3] = '-' + str(round(float(str(profit[3])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[3] = round(float(str(profit[3])[1:].replace(',', '')) * float(usd), 1)

        profit2[0] = round(float(str(profit2[0])[1:].replace(',', '')) * float(usd), 1)
        profit2[1] = round(float(str(profit2[1])[1:].replace(',', '')) * float(usd), 1)
        profit2[2] = round(float(str(profit2[2])[1:].replace(',', '')) * float(usd), 1)
        profit2[3] = round(float(str(profit2[3])[1:].replace(',', '')) * float(usd), 1)

        output = f'''Profit per day: {profit[0]}₽
    Profit for the week: {profit[1]}₽
    Profit for the month: {profit[2]}₽
    Profit for the year: {profit[3]}₽
    Electricity costs per day: {profit2[0]}₽
    Electricity costs per week: {profit2[1]}₽
    Electricity costs per month: {profit2[2]}₽
    Electricity costs per year: {profit2[3]}₽
            '''
    else:
        output = f'''Profit per day: {profit[0]}
    Profit for the week: {profit[1]}
    Profit for the month: {profit[2]}
    Profit for the year: {profit[3]}
    Electricity costs per day: {profit2[0]}
    Electricity costs per week: {profit2[1]}
    Electricity costs per month: {profit2[2]}
    Electricity costs per year: {profit2[3]}
        '''


    a1 = profit[0]
    a2 = profit[1]
    a3 = profit[2]
    a4 = profit[3]
    a5 = profit2[0]
    a6 = profit2[1]
    a7 = profit2[2]
    a8 = profit2[3]



    driver.implicitly_wait(30)
    driver.get(link2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')

    profit = []
    profit2 = []
    profit3 = []
    inf = soup.find_all('div', class_='tss-kk1978-calcTimeBlockPositive')
    neg = soup.find_all('div', class_='tss-dk2icf-calcTimeBlockNegative')
    inf2 = soup.find_all('div', class_='tss-aub44l-calcTimeBlock')
    bit = soup.find_all('p', class_='MuiTypography-root MuiTypography-body1 tss-nd60qq-mainInfoPrice mui-1iv9rsj')
    print(inf)
    btc = 0
    # print(inf)
    for e in bit:
        print(e)
        btc = e.text.split(' ')[0]
    if not inf:
        for x in neg:
            profit.append(x.text.split('Прибыль')[1])
    else:
        for i in inf:
            profit.append(i.text.split('Прибыль')[1])
    for j in inf2:
        if 'Расходы' in j.text:
            z = j.text.split('.')
            z = '.'.join([z[1], z[2]])
            profit2.append(z)
    print(profit)
    print(profit2)

    if rub == True:
        if '-' in str(profit[0]):
            profit[0] = '-' + str(round(float(str(profit[0])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[0] = round(float(str(profit[0])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[1]):
            profit[1] = '-' + str(round(float(str(profit[1])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[1] = round(float(str(profit[1])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[2]):
            profit[2] = '-' + str(round(float(str(profit[2])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[2] = round(float(str(profit[2])[1:].replace(',', '')) * float(usd), 1)

        if '-' in str(profit[3]):
            profit[3] = '-' + str(round(float(str(profit[3])[2:].replace(',', '')) * float(usd), 1))
        else:
            profit[3] = round(float(str(profit[3])[1:].replace(',', '')) * float(usd), 1)

        profit2[0] = round(float(str(profit2[0])[1:].replace(',', '')) * float(usd), 1)
        profit2[1] = round(float(str(profit2[1])[1:].replace(',', '')) * float(usd), 1)
        profit2[2] = round(float(str(profit2[2])[1:].replace(',', '')) * float(usd), 1)
        profit2[3] = round(float(str(profit2[3])[1:].replace(',', '')) * float(usd), 1)

        profit[0] = profit[0] + a1
        profit[1] = profit[1] + a2
        profit[2] = profit[2] + a3
        profit[3] = profit[3] + a4

        output = f'''Профит за день: {profit[0]}₽
Профит за неделю: {profit[1]}₽
Профит за месяц: {profit[2]}₽
Профит за год: {profit[3]}₽
Расходы эл. за день: {profit2[0]}₽
Расходы эл. за неделю: {profit2[1]}₽
Расходы эл. за месяц: {profit2[2]}₽
Расходы эл. за год: {profit2[3]}₽
            '''
    else:

        profit[0] = profit[0] + ' + ' + a1
        profit[1] = profit[1] + ' + ' + a2
        profit[2] = profit[2] + ' + ' + a3
        profit[3] = profit[3] + ' + ' + a4

        output = f'''Профит за день: {profit[0]}
Профит за неделю: {profit[1]}
Профит за месяц: {profit[2]}
Профит за год: {profit[3]}
Расходы эл. за день: {profit2[0]}
Расходы эл. за неделю: {profit2[1]}
Расходы эл. за месяц: {profit2[2]}
Расходы эл. за год: {profit2[3]}'''


    return output

#main(24000, 1, 0.03, 'MH')
