
import requests

# Send the request to a real, stable web vault
vault_response = requests.get("https://www.rfc-editor.org/rfc/rfc1.html")
# The raw contents of the vault. It's a jumbled mess of text.
raw_html_content = vault_response.text
print(raw_html_content[:500]) # Prints the first 500 characters



from bs4 import BeautifulSoup
# (assuming you have the raw_html_content from the previous step)

# Feed the raw content into the BeautifulSoup decompiler
soup = BeautifulSoup(raw_html_content, 'html.parser')
# Now you have a perfectly organized object to work with!
print(soup.title) # This will neatly print the <title> tag from the RFC


