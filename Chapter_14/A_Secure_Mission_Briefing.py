
import asyncio
import httpx
import os
from dotenv import load_dotenv

# Load environment variables from a .env file.
# This is the first step of your mission.
load_dotenv()

async def access_jedi_archives():
    
    api_key = os.getenv("API_KEY")   
    if not api_key:
        print("Error: API_KEY not found in your .env file. Mission aborted.")
        print("Please create a .env file in the same directory "
              "and add: API_KEY=your_secret_key")
        return

    # 3. Create the authorization header with your secret.
    # The header name ('X-API-Key') depends on the API you're using.
    # For a Bearer token, the header would be "Authorization": "Bearer YOUR_TOKEN"
    headers = {
        "X-API-Key": api_key,
        "Accept": "application/json"
    }

    # This is a test endpoint that returns the headers it received.
    # It lets us verify that our secret was sent correctly.
    url = "https://httpbin.org/headers"

    print("Attempting secure access to the Jedi Archives...")

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers=headers)
            response.raise_for_status() # This command will raise an exception for 4xx/5xx status codes
            
            print("Access granted! Here are the headers the server received:")
            # We are printing a JSON object, not the secret directly.
            print(response.json()['headers'])

    except httpx.HTTPStatusError as e:
        # A 401 error is a direct signal that authentication failed.
        if e.response.status_code == 401:
            print("Authentication failed. Your API key may be invalid or expired. Received 401 Unauthorized.")
        else:
            print(f"An unexpected HTTP error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


async def main():
    await access_jedi_archives()

if __name__ == "__main__":
    asyncio.run(main())