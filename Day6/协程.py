import asyncio
import aiohttp


urls=[

]

async def aiodownload(url):
    name=url.rsplit()
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open("img/"+name,mode="wb") as f:
                f.write(await resp.content.read())


async def main():
    tasks=[]
    for url in urls:
        tasks.append(aiodownload(url))

    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())