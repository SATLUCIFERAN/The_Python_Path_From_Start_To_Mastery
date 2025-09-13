
import asyncio
import httpx
import os
from dotenv import load_dotenv

# Your first task: Load your long-term Kyber crystal key from the Holocron.
load_dotenv()

# The TokenManager is your personal droid, handling all the dirty work of
# managing tokens and keeping your lightsaber charged.
class TokenManager:
    def __init__(self, refresh_token: str):
        self.refresh_token = refresh_token
        self.access_token = None
        
    async def get_access_token(self):
        """Returns the current access token, or refreshes it if it's not set."""
        if not self.access_token:
            print("No active lightsaber found. Using the Kyber crystal to forge a new one...")
            await self.refresh_the_token()
        return self.access_token

    async def refresh_the_token(self):
        """
        The sacred ritual: uses the long-term refresh token to get a new,
        short-lived access token.
        
        Note: The actual endpoint for a refresh token is a POST request with
        your refresh token in the body. We'll use httpbin.org to simulate this.
        """
        refresh_url = "https://httpbin.org/post"
        
        print("Forging a new lightsaber... Stand by.")
        
        try:
            async with httpx.AsyncClient() as client:
                # We send the refresh token to the server to get a new access token.
                response = await client.post(
                    refresh_url,
                    json={"refresh_token": self.refresh_token}
                )
                response.raise_for_status()
                
                # In a real-world scenario, the API would return a new access token.
                # We'll just grab a dummy one from the response for this demo.
                new_token_data = response.json().get('json')
                if new_token_data and new_token_data.get('refresh_token'):
                    self.access_token = "dummy_access_token_from_refresh" # Replace with real token from response
                    print("Lightsaber forged! You now have a fresh access token.")
                else:
                    print("Forging failed. The Kyber crystal might be invalid.")
                    self.access_token = None
                    
        except httpx.HTTPStatusError as e:
            print(f"Forging failed with an HTTP error: {e}")
            self.access_token = None
        except Exception as e:
            print(f"An unexpected error occurred during forging: {e}")
            self.access_token = None


async def secure_mission(token_manager: TokenManager):
    """
    Attempts to access a secure Jedi archive with an access token.
    If it fails due to a 401 Unauthorized error, it attempts to refresh the token
    and retry the mission once.
    """
    
    # We will start with a known-bad token to trigger the refresh flow immediately.
    # In a real app, this would be a token from a previous run.
    token_manager.access_token = "expired_or_invalid_access_token"
    
    # The URL of the protected archive (simulated).
    protected_url = "https://httpbin.org/bearer"
    
    for attempt in range(2): # We'll try a maximum of 2 times
        try:
            access_token = await token_manager.get_access_token()
            
            headers = {
                "Authorization": f"Bearer {access_token}"
            }
            
            print(f"\nAttempting mission to {protected_url} with attempt #{attempt + 1}...")
            
            async with httpx.AsyncClient() as client:
                response = await client.get(protected_url, headers=headers)
                response.raise_for_status()
                
                print("Mission successful! Data received:")
                print(response.json())
                return # Mission is complete, so we exit the function
        
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                print(f"A disturbance in the Force detected! Server returned a 401 Unauthorized.")
                print("Lightsaber appears to be out of power. Initiating refresh protocol...")
                await token_manager.refresh_the_token()
                
                # Check if refresh was successful. If not, don't retry.
                if not token_manager.access_token:
                    print("Failed to refresh token. Mission failed.")
                    return
            else:
                print(f"Mission failed with an unexpected HTTP error: {e}")
                return
        except Exception as e:
            print(f"An unexpected error occurred during the mission: {e}")
            return
    
    print("Mission failed after multiple attempts. All hope is lost.")

async def main():
    # Load the refresh token securely from the environment.
    refresh_token = os.getenv("REFRESH_TOKEN")
    
    if not refresh_token:
        print("Error: REFRESH_TOKEN not found. Mission cannot start.")
        return
        
    # The Jedi Commando droid is ready!
    commando = TokenManager(refresh_token)
    
    # Begin the mission.
    await secure_mission(commando)

if __name__ == "__main__":
    asyncio.run(main())