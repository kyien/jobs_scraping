from jobs import clean
from send_mail import compose_mail
import asyncio


async def run_app():

    try:
        jobs_df = await clean()
        compose_mail(jobs_df)

    except Exception as err:
        print(str(err))

if __name__ == '__main__':
    asyncio.run(run_app())