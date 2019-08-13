import random
import asyncio

#def sleep(seconds):
#    start = time.time()
#    while time.time() - start < seconds:
#        yield


async def produce():
    #while True:
    #yield from asyncio.sleep(0.5)
    await asyncio.sleep(0.5)
    data = random.randint(0,10)
    return data

#@asyncio.coroutine
async def consume():
    sum_ = 0 
    count = 0

    while True:
       #data = yield from produce()
        data = await produce()
        print('Got data:',data)

        sum_ += data
        count += 1
        
        print('Sum: ',sum_)
        print('Averange: ',sum_ / count)
        print()

#@asyncio.coroutine
async def another_task():
    while True:
        print()
        print('Hello from another task')
        print()
        #yield from asyncio.sleep(1)
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [consume(),another_task()]
    loop.run_until_complete(asyncio.wait(tasks))
