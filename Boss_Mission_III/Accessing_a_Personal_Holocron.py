
from bs4 import BeautifulSoup

# The path to your local HTML file
file_path = "Chapter_9/The_HTML_of_a_Digital_Artifact_Gallery.html"

# Use the 'with' statement to safely open and read the file
try:
    with open(file_path, "r") as file:
        raw_html_content = file.read()

    # Feed the local HTML content into BeautifulSoup
    soup = BeautifulSoup(raw_html_content, 'html.parser')

    # Now, execute the perfect heist using your original logic
    # Use find_all() to locate every 'div' that has the class 'artifact-card'.
    all_artifacts = soup.find_all('div', class_='artifact-card')

    # Loop through each artifact card you found
    for artifact in all_artifacts:
        # Use find() to search INSIDE the current artifact card
        # for the element with the class 'artifact-name'.
        name_element = artifact.find('h3', class_='artifact-name')

        # Find the element with the class 'artifact-price'.
        price_element = artifact.find('span', class_='artifact-price')

        # Now you can get the clean text from those elements
        name = name_element.text.strip()
        price = price_element.text.strip()

        print(f"Found artifact: {name} for {price}")

except FileNotFoundError:
    print(f"ERROR: The file '{file_path}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")