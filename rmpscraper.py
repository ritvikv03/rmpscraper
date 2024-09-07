import requests
from bs4 import BeautifulSoup
import pandas as pd
import argparse
import json
import time

# Constants for the Rate My Professor URL
BASE_URL = "https://www.ratemyprofessors.com/search/teachers"

# Function to get professor data from a specific page
def get_professors_data(university, department, page=1):
    params = {
        "query": university,
        "sid": department,
        "page": page
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data from Rate My Professors (status code {response.status_code})")

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # This is a placeholder selector. You need to inspect the RMP site for actual structure.
    professor_elements = soup.find_all('div', class_='professor')

    professors = []
    
    for prof in professor_elements:
        try:
            name = prof.find('h2').get_text(strip=True)
            rating = prof.find('span', class_='rating').get_text(strip=True)
            difficulty = prof.find('span', class_='difficulty').get_text(strip=True)
            comments = prof.find('div', class_='comments').get_text(strip=True)
            professors.append({
                'name': name,
                'rating': rating,
                'difficulty': difficulty,
                'comments': comments
            })
        except AttributeError:
            # Skip any entries that don't have all required fields
            continue

    return professors

# Function to handle pagination
def scrape_all_professors(university, department):
    all_professors = []
    page = 1

    while True:
        print(f"Scraping page {page}...")
        try:
            professors = get_professors_data(university, department, page)
            if not professors:
                break
            all_professors.extend(professors)
            page += 1
            time.sleep(1)  # Sleep to avoid overwhelming the server
        except Exception as e:
            print(f"Error: {e}")
            break

    return all_professors

# Function to save data as CSV
def save_as_csv(professors, output_file):
    df = pd.DataFrame(professors)
    df.to_csv(output_file, index=False)
    print(f"Data saved to {output_file}")

# Function to save data as JSON
def save_as_json(professors, output_file):
    with open(output_file, 'w') as f:
        json.dump(professors, f, indent=4)
    print(f"Data saved to {output_file}")

# Main function to handle command-line arguments and program flow
def main():
    # Removed argparse and added variables to allow function to run in Jupyter
    university = "Your University" # Replace with your university
    department = "Your Department" # Replace with your department
    output = "csv" # Choose either csv or json

    print(f"Scraping professors from {university} in the {department} department...")
    professors = scrape_all_professors(university, department)

    if output == 'csv':
        save_as_csv(professors, f'{university}_professors.csv')
    elif output == 'json':
        save_as_json(professors, f'{university}_professors.json')

if __name__ == '__main__':
    main()