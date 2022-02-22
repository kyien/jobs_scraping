import requests
from bs4 import BeautifulSoup
import warnings
import asyncio
warnings.filterwarnings('ignore')

#
job_locations=['Nairobi','Nakuru','Thika','Mombasa','Remote','Mombasa']
job_categories=['software-data','marketing-communications','engineering-technology','legal-services']

async def get_jobs():
    job_count=[]

    for loc in job_locations:
        for category in job_categories:
            headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
            uri=f'https://www.brightermonday.co.ke/jobs/{category}/{loc.lower()}'
            # proxy={"http": "http://proxy2.safaricom.net:8080" , "https":"http://proxy2.safaricom.net:8080"}
            # req=await requests.get(url=uri,headers=headers,verify=False,proxies=proxy)
            try:
                req=requests.get(url=uri,headers=headers)
                bs_content=BeautifulSoup(req.content,'html.parser')
                job_content=bs_content.find_all('div',class_='mb-5')
                job_count.append(job_content)
            except Exception as e:
                print(str(e))


    return job_count


async def clean():
    jobs_count=await get_jobs()
    for jobs in jobs_count:
        for job in jobs:
            job_title=job.find('a').attrs.get('title')
            print(job_title)

    return


# p=get_jobs()
# print(p)
# print(get_jobs())
if __name__ == '__main__':
    asyncio.run(clean())
