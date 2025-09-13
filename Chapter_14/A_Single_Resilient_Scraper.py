
import asyncio, random, httpx

async def fetch_all(base="https://swapi.dev/api/starships/"):
    items, url = [], base
    async with httpx.AsyncClient(timeout=10, verify=False) as client:  # set verify=True in prod
        while url:
            for tries in range(5):  # retry this page up to 5 times
                try:
                    r = await client.get(url); r.raise_for_status()
                    data = r.json()
                    items += data.get("results", [])
                    url = data.get("next")
                    await asyncio.sleep(0.3)  # be polite
                    break
                except httpx.HTTPStatusError as e:
                    if e.response.status_code != 429:  # other HTTP errors → stop
                        url = None; break
                    delay = float(e.response.headers.get(
                        "Retry-After", (1 * (2 ** tries)) + random.uniform(0, 0.5)
                    ))
                    await asyncio.sleep(delay)
                except httpx.TimeoutException:
                    await asyncio.sleep(1 * (2 ** tries))
            else:
                break  # gave up retries for this page
    return items

async def main():
    ships = await fetch_all()
    print(f"Total starships: {len(ships)}")
    for s in ships: print("-", s.get("name", "unknown"))

if __name__ == "__main__":
    asyncio.run(main())









