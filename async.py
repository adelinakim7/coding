import asyncio

async def Hi(word, delay):
    await asyncio.sleep(delay)
    print(word)
    
async def main():
    await asyncio.gather(
        Hi("Charli", 5),
        Hi("Addison", 7),
        Hi("Payton", 5),
        Hi("Riley", 4),
        Hi("Nick", 1),
        Hi("Nessa", 9),
        Hi("Jayden", 3),
        Hi("Madison", 6),
        Hi("Josh", 8),
        Hi("Eva", 2),
        )
asyncio.run(main())
