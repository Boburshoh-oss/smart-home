import asyncio

async def run_forever():
    await asyncio.sleep(5)
    await asyncio.create_subprocess_shell("daphne config.asgi:application -b 0.0.0.0 --port 8000")
    while True:
        await asyncio.sleep(0.1)


async def main():
    await asyncio.create_subprocess_shell("python manage.py makemigrations")
    await asyncio.sleep(1)
    await asyncio.create_subprocess_shell("python manage.py migrate")
    await asyncio.sleep(1)
    await asyncio.create_subprocess_shell("python manage.py runworker mqtt")    

if __name__ == "__main__":
    asyncio.run(main())
    asyncio.run(run_forever())
