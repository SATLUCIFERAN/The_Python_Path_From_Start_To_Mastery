
import asyncio
import httpx

async def get_ship_data(ship_id: int):
    """
    An async function to retrieve data for a single ship.
    The 'await' keyword tells the program to pause at this line,
    but it doesn't block the entire script. It can go and do other things
    until the response is ready.
    """
    async with httpx.AsyncClient() as client:
        url = f"https://api.starwars.com/ships/{ship_id}"
        response = await client.get(url)
        response.raise_for_status()
        return response.json()

async def main():
    """
    A 'main' async function that gathers all the requests and runs them concurrently.
    This is where the magic happens.
    """
    # A list of ships to retrieve
    ship_ids = [10, 11, 12, 13, 14, 15]

    # The 'asyncio.gather' function sends all the requests at once.
    # The program will not proceed until all responses have been received.
    print("Sending multiple requests simultaneously...")
    results = await asyncio.gather(*[
        get_ship_data(ship_id) for ship_id in ship_ids
    ])

    print("\nAll data received!")
    for result in results:
        print(f"✅ Retrieved info for: {result['name']}")

if __name__ == "__main__":
    # The 'asyncio.run' function starts the entire async process.
    asyncio.run(main())