
import requests
import httpx
import asyncio

TEST_URL = "https://httpbin.org/delay/5"

def demonstrate_sync_timeout():    
    print("Initiating synchronous request...")
    try:        
        requests.get(TEST_URL, timeout=3)
        print("Synchronous request succeeded.")
    except requests.exceptions.Timeout:
        print("Synchronous request timed out gracefully.")

async def demonstrate_async_timeout():    
    print("Initiating asynchronous request...")
    try:        
        async with httpx.AsyncClient(timeout=3) as client:
            await client.get(TEST_URL)
        print("Asynchronous request succeeded.")
    except httpx.TimeoutException:
        print("Asynchronous request timed out gracefully.")

async def main():    
    demonstrate_sync_timeout()    
    await demonstrate_async_timeout()

if __name__ == "__main__":
    asyncio.run(main())