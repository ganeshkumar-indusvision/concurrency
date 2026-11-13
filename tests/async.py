import asyncio



async def sleep_await(delay,id):
    print("Started Sample Wait")
    await asyncio.sleep(delay)
    print("Done Fake Wait")
    return {"id": id}
async def main():
    task = sleep_await(2,1)
    result = await task
    print("It's done bro")
    print(result) 


# main()
asyncio.run(main())