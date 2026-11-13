import asyncio



async def sleep_await(delay,id):
    print("Started Sample Wait")
    await asyncio.sleep(delay)
    print("Done Fake Wait")
    return {"id": id}
async def main():
    task1 = sleep_await(2,1)
    task2 = sleep_await(2,2)
    result1 = await task1
    result2 = await task2
    print("It's done bro")
    print(result1)
    print(result2) 


# main()
asyncio.run(main())