import asyncio
import time
from datetime import datetime


class SyncExample:
    def fn1(self):
        time.sleep(6)
        print('start fn1 - ', datetime.now())
        time.sleep(5)
        print('mid fn1 - ', datetime.now())
        time.sleep(4)
        print('end fn1 - ', datetime.now())
        return True

    def fn2(self):
        time.sleep(2)
        print('start fn2 - ', datetime.now())
        time.sleep(2)
        print('end fn2 - ', datetime.now())
        return True

    def fn3(self):
        print('start fn3 - ', datetime.now())
        time.sleep(2)
        print('mid fn3 - ', datetime.now())
        time.sleep(10)
        print('end fn3 - ', datetime.now())
        return True

    def main(self):
        start = time.time()
        f1 = self.fn1()
        f2 = self.fn2()
        f3 = self.fn3()
        end = time.time()
        print('Sync Elapsed Time: ', end - start)


class AsyncExample:
    async def fn1(self):
        await asyncio.sleep(6)
        print('start fn1 - ', datetime.now())
        await asyncio.sleep(5)
        print('mid fn1 - ', datetime.now())
        await asyncio.sleep(4)
        print('end fn1 - ', datetime.now())

    async def fn2(self):
        await asyncio.sleep(2)
        print('start fn2 - ', datetime.now())
        await asyncio.sleep(2)
        print('end fn2 - ', datetime.now())

    async def fn3(self):
        print('start fn3 - ', datetime.now())
        await asyncio.sleep(2)
        print('mid fn3 - ', datetime.now())
        await asyncio.sleep(10)
        print('end fn3 - ', datetime.now())
        return True

    def fn4(self):
        print('start fn4', datetime.now())
        print('mid fn4', datetime.now())
        print('end fn4', datetime.now())

    # Ok
    async def main(self):
        start = time.time()
        self.fn4()

        f1 = asyncio.create_task(self.fn1())
        print('this is f1: ', f1)
        f2 = asyncio.create_task(self.fn2())
        print('this is f2: ', f2)
        f3 = asyncio.create_task(self.fn3())
        print('this is f3: ', f3)
        await f1
        await f2
        await f3
        print('value: ', f1.result(), f2.result(), f3.result())

        self.fn4()
        end = time.time()
        print('Async Elapsed Time: ', end-start)

    # Ok
    async def main2(self):
        start = time.time()
        batch = asyncio.gather(self.fn1(), self.fn2(), self.fn3())
        print(batch)
        f1, f2, f3 = await batch
        print('value: ', f1, f2, f3)
        end = time.time()
        print('Async Elapsed Time: ', end-start)

    # This is fail
    async def main3(self):
        start = time.time()
        f1 = await asyncio.gather(self.fn1())
        f2 = await asyncio.gather(self.fn2())
        f3 = await asyncio.gather(self.fn3())

        print('this is f1: ', f1)
        print('this is f2: ', f2)
        print('this is f3: ', f3)
        end = time.time()
        print('Async Elapsed Time: ', end-start)


if __name__ == '__main__':
    print('-'*20, 'Sync', '-'*20)
    sync_example = SyncExample()
    sync_example.main()

    print('|-'*50)

    print('-'*20, 'Async 1', '-'*20)
    async_example = AsyncExample()
    asyncio.run(async_example.main())

    print('-'*20, 'Async 2', '-'*20)
    asyncio.run(async_example.main2())

    print('-'*20, 'Async 3', '-'*20)
    asyncio.run(async_example.main3())
