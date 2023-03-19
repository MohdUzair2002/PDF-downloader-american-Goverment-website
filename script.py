import requests
from bs4 import BeautifulSoup
import time
try:
    name_of_school=[]
    codes=[]
    year=[2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020,2021]
    cookies = {
        '__cf_bm': 'iGFbSwFsIMUp8rgJIe8W.bLKRQNEfRjhDysFQX8NvIw-1667565640-0-Ad2vCRTl/Hr+0zDlwNNlT9jELm8H07vx3euQVx7kZO9k5E3qf/lXczBCrv/6j1amQkLp9Q8nv+wDFIxkzHhSEWQ=',
    }

    headers = {
        'authority': 'www.ade.az.gov',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': '__cf_bm=iGFbSwFsIMUp8rgJIe8W.bLKRQNEfRjhDysFQX8NvIw-1667565640-0-Ad2vCRTl/Hr+0zDlwNNlT9jELm8H07vx3euQVx7kZO9k5E3qf/lXczBCrv/6j1amQkLp9Q8nv+wDFIxkzHhSEWQ=',
        'referer': 'https://www.ade.az.gov/sder/PublicReports.asp',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    }

    params = {
        'FiscalYear': '2006',
    }
    page = requests.get('https://www.ade.az.gov/sder/PublicReports.asp', params=params,  headers=headers)
    print(page.status_code)
    soup=BeautifulSoup(page.content,'html.parser')
    id=soup.find(id='comEntityID')
    id_text=str(id.text).split('\n')
    del id_text[0]
    del id_text[-1]
    options=id.find_all('option')
    for option in options:
        value=option['value']
        codes.append(value)
        # print(option.text,value)

        # print(value)
    i=0
    while(i < 16):
        cookies = {
        '__cf_bm': 'IbeSBaWcEkGneRongQWihUCNlxNBTLK66Q3pCAEzXwg-1667574510-0-AdTW7n60UV7ZoSzExnNJ9Jrg7mpFrrruOJc5fiuJQ2Apt6RuHCJP3Y/l8WDZtQCkkrzINxeVsjWG3OnQcA3mCmc=',
        }

        headers = {
        'authority': 'www.ade.az.gov',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        # 'cookie': '__cf_bm=IbeSBaWcEkGneRongQWihUCNlxNBTLK66Q3pCAEzXwg-1667574510-0-AdTW7n60UV7ZoSzExnNJ9Jrg7mpFrrruOJc5fiuJQ2Apt6RuHCJP3Y/l8WDZtQCkkrzINxeVsjWG3OnQcA3mCmc=',
        'origin': 'https://www.ade.az.gov',
        'referer': 'https://www.ade.az.gov/sder/PublicReports.asp?FiscalYear=2006',
        'sec-ch-ua': '"Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        }

        j=0
        while( j< 269):
            data = {
                'comFiscalYear': f'{year[i]}',
                'comEntityID': f'{codes[j]}',
                'comGrouping': '1',
                'comListType': '4',
                'butCreateReport': 'Create Report',
            }
            

            response = requests.post('https://www.ade.az.gov/sder/ReportGenerationPublic.asp',  headers=headers, data=data)
            print(i)
            print(j)
            name=(f'{id_text[j]} {year[i]}').replace('/','')
        
            with open(f'{name}.pdf', 'wb') as f:
                f.write(response.content)
            time.sleep(1)
            j+=1
        i+=1
except:
    print(f"The error came when the program was on year={year[i]} and school={id_text[j]} ,so kindly run again" )
