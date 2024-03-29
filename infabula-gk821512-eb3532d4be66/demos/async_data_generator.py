import asyncio
import httpx


async def random_name(count):
    url = "https://randomuser.me/api"
    print(f"#{count} start")
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        data = response.json()
        if data:
            first_name = data["results"][0]['name']['first']
            last_name = data["results"][0]['name']['last']
            print(f"#{count} {first_name} {last_name}")
            return first_name, last_name



async def main():
    tasks = []
    for task_count in range(5):
        tasks.append(asyncio.create_task(random_name(task_count)))

    names = await asyncio.gather(*tasks)

    for name in names:
        print(name)

asyncio.run(main())