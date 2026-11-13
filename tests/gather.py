import asyncio



async def sleep_await(delay,id):
    print("Started Sample Wait")
    await asyncio.sleep(delay)
    print("Done Fake Wait")
    return {"id": id}
async def main():
    results = await asyncio.gather(sleep_await(2,1), sleep_await(2,2))
    print("It's done bro")
    for result in results:
        print(result)

    # print(result1,result2)
# 


# main()
asyncio.run(main())