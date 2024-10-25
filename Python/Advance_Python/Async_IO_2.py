import asyncio

print("execution started ")

async def fetch_data():
    print("Start fetching data...")
    await asyncio.sleep(2)  # Simulating I/O operation with sleep
    print("Data fetched!")
    return "Data"

async def process_data():
    print("Start processing data...")
    await asyncio.sleep(1)  # Simulating I/O operation with sleep
    print("Data processed!")
    return "Processed Data"

async def main():
    # Schedule both coroutines to run concurrently
    fetch_task = asyncio.create_task(fetch_data())
    process_task = asyncio.create_task(process_data())

    # Wait for both tasks to complete
    fetched_data = await fetch_task
    processed_data = await process_task

    print(f"Fetched: {fetched_data}, Processed: {processed_data}")

# Run the main coroutine
asyncio.run(main())

print("execution completed ")
