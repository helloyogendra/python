import asyncio

async def fetch_data(n):
    print(f"Start fetching data {n}...")
    await asyncio.sleep(2)
    print(f"Data {n} fetched!")
    return f"Data {n}"

async def main():
    tasks = [fetch_data(i) for i in range(3)]
    results = await asyncio.gather(*tasks)
    print(f"Results: {results}")

asyncio.run(main())



#### asyncio.wait 



async def task(id, delay):
    print(f"Task {id} started")
    await asyncio.sleep(delay)
    print(f"Task {id} finished")
    return f"Result from task {id}"

async def main():
    # Create a set of tasks
    tasks = {
        asyncio.create_task(task(1, 2)),
        asyncio.create_task(task(2, 3)),
        asyncio.create_task(task(3, 1)),
    }

    # Wait for all tasks to complete
    done, pending = await asyncio.wait(tasks)

    for t in done:
        print(f"Task result: {t.result()}")

# Run the main function
asyncio.run(main())



#### asyncio.queue


import asyncio

async def producer(queue):
    for i in range(5, 25, 5):
        print(f"Producing {i}")
        await asyncio.sleep(1)  # Simulate some I/O operation
        await queue.put(i)
    await queue.put(None)  # Sentinel to signal the consumer to stop

async def consumer(queue):
    while True:
        item = await queue.get()
        if item is None:  # Check for sentinel to exit
            break
        print(f"Consuming {item}")
        await asyncio.sleep(2)  # Simulate consuming time

async def main():
    queue = asyncio.Queue()

    # Start the producer and consumer tasks
    producer_task = asyncio.create_task(producer(queue))
    consumer_task = asyncio.create_task(consumer(queue))

    # Wait for both tasks to finish
    await asyncio.gather(producer_task, consumer_task)

# Run the main function
asyncio.run(main())

