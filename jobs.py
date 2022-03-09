import requests
from bs4 import BeautifulSoup
import warnings
import json
from decouple import config
import pandas as pd
import asyncio



warnings.filterwarnings('ignore')

#
job_locations=['Nairobi','Nakuru','Thika','Mombasa','Remote','Mombasa']
job_categories=['software-data','marketing-communications','engineering-technology','legal-services']


async def get_jobs():
    job_count=[]

    for loc in job_locations:
        for category in job_categories:
            headers=json.loads(config("HEADERS"))
            uri=f'https://www.brightermonday.co.ke/jobs/{category}/{loc.lower()}'
            proxy=json.loads(config("PROXY"))
            try:
                # req = requests.get(url=uri, headers=headers, verify=False, proxies=proxy)
                req=requests.get(url=uri,headers=headers)
                bs_content=BeautifulSoup(req.content,'html.parser')
                job_content=bs_content.find_all('div',class_='pt-2')
                job_count.append(job_content)
            except Exception as e:
                print(str(e))


    return job_count


async def clean():
    jobs_count = await get_jobs()
    job_list = []
    for items in jobs_count:
        for item in items:
            job_link=item.find('a')
            if job_link is not None and 'title' in job_link.attrs:
                job_title=job_link.attrs.get('title').strip()
                job_url=job_link.attrs.get('href')
                job={"title":job_title,"link":job_url}
                job_list.append(job)
                # print(f'{job_title}\t\t{job_url}')
    # print(pd.DataFrame(job_list))
    return pd.DataFrame(job_list)


if __name__ == '__main__':
    asyncio.run(clean())

