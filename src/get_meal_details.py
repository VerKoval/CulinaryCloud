import requests

# Define the API endpoint URL for listing all meal categories
api_url = 'https://www.themealdb.com/api/json/v1/1/categories.php'

# Make a GET request to the API
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON response
    categories_data = response.json()

    # Extract the list of categories
    categories = [category['strCategory'] for category in categories_data['categories']]

    # Print the list of categories
    print("Meal Categories:")
    for category in categories:
        print(category)
else:
    print(f'Error: Failed to retrieve meal categories (status code {response.status_code})')

