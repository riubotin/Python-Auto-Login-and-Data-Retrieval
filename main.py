import requests
from bs4 import BeautifulSoup

# Function to login to the website
def login_to_website(username, password):
    login_url = 'https://example.com/login'  # Replace with the actual login URL of the website
    login_data = {
        'username': username,
        'password': password
    }
    session = requests.Session()
    response = session.post(login_url, data=login_data)
    
    # Check if login was successful
    if response.status_code == 200:
        print("Login successful!")
        return session
    else:
        print("Failed to login.")
        return None

# Function to fetch data after successful login
def get_data(session):
    data_url = 'https://example.com/data'  # Replace with the actual URL of the data page
    response = session.get(data_url)
    
    if response.status_code == 200:
        # Using BeautifulSoup to parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Retrieving data from a specific element on the page
        data = soup.find('div', class_='data-container').text
        
        return data
    else:
        print("Failed to fetch data.")
        return None

# Function to save data to a text file
def save_data_to_file(data):
    file_path = 'data.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(data)
    print(f"Data saved to {file_path}.")

# Example usage of the script
if __name__ == "__main__":
    # Replace with your actual username and password
    username = 'your_username'
    password = 'your_password'
    
    # Login to the website
    session = login_to_website(username, password)
    
    if session:
        # If login successful, fetch data
        data = get_data(session)
        
        if data:
            # If data fetched successfully, save to text file
            save_data_to_file(data)
        
        # Logout or close session if necessary
        session.close()
