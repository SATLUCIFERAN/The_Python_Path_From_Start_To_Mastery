
import asyncio
import httpx

async def get_planet_data(planet_id: int):
    """
    This is a coroutine (async def). It's a task that can be paused.
    """
    async with httpx.AsyncClient() as client:
        url = f"https://api.starwars.com/planets/{planet_id}"
        print(f"Requesting data for planet ID {planet_id}...")
        
        # We hit 'await' here. The function pauses, and the control tower can
        # start another mission while we wait for the API response.
        response = await client.get(url)
        
        response.raise_for_status()
        planet = response.json()
        print(f"Received data for {planet['name']}!")
        return planet

async def main():
    """
    This is our main mission brief. It orchestrates all the tasks.
    """
    # Create a list of all the tasks we want to run concurrently.
    tasks = [
        get_planet_data(1),
        get_planet_data(2),
        get_planet_data(3)
    ]

    # The 'await asyncio.gather()' command tells the control tower to
    # run all these tasks simultaneously. The entire program will pause here
    # until ALL of them are finished.
    print("Launching probes to multiple planets...")
    results = await asyncio.gather(*tasks)

    print("\nMission complete. All data transmissions received.")
    for result in results:
        print(f" - Planet: {result['name']}")

# The single, final command that launches the entire async operation.
if __name__ == "__main__":
    asyncio.run(main())






{
  "author": "Master Yoda"
}