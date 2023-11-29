#!/usr/bin/env python3
import requests

def get_all_english_terms():
    base_url = "https://en.wiktionary.org/w/api.php"
    
    # Specify the category or other criteria to filter English terms
    category = "English_lemmas"
    
    # Set parameters for the API request
    params = {
        'action': 'query',
        'format': 'json',
        'list': 'categorymembers',
        'cmtitle': f'Category:{category}',
        'cmlimit': 500,  # Adjust the limit based on your needs
    }

    terms = []

    while True:
        # Make the API request
        response = requests.get(base_url, params=params)
        data = response.json()

        # Extract terms from the response
        members = data['query']['categorymembers']
        terms.extend([member['title'] for member in members])

        # Check if there are more results to fetch
        if 'continue' in data:
            params['cmcontinue'] = data['continue']['cmcontinue']
        else:
            break

    return terms

def save_terms_to_file(terms, filename='wiktionary_terms.txt'):
    with open(filename, 'w', encoding='utf-8') as file:
        for term in terms:
            file.write(term + '\n')

if __name__ == "__main__":
    english_terms = get_all_english_terms()
    print(f"Number of English terms: {len(english_terms)}")
    print(english_terms[:10])  # Print the first 10 terms as an example
    save_terms_to_file(english_terms)
