import time
import asyncio

async def brewCoffee():
    print("Start brewing coffee...")
    await asyncio.sleep(3)
    print("End brewCoffee")
    return "Coffee ready"

async def toastBegele():
    print("Start toasting begele...")
    await asyncio.sleep(2)
    print("End toastBegele")
    return "Begele toasted"

async def main():
    start_time = time.time()

#Work using batch
    # batch = asyncio.gather(brewCoffee(), toastBegele())
    # result_coffee, result_begele = await batch

#Work using Individual task
    coffee_task = asyncio.create_task(brewCoffee())
    begele_task = asyncio.create_task(toastBegele())

    result_coffee = await coffee_task
    result_begele = await begele_task


    end_time = time.time()
    elased_time = end_time - start_time

    print(f"Result of brewCoffee: {result_coffee}")
    print(f"Result of toastBegele: {result_begele}")
    print(f"Total time: {elased_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(main())