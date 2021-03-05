import json
import requests

def read_bring_key():
    bing_api_key = None
    try:
        with open('bing.key', 'r') as f:
            bing_api_key = f.readline().strip()
    except:
        raise IOError('bing.key file not found')

    if not bing_api_key:
        raise KeyError('Bing key not found')

    return bing_api_key

def run_query(search_terms):
    bing_key = read_bring_key()
    search_url = "https://api.bing.microsoft.com/v7.0/search"
    headers = {"Ocp-Apim-Subscription-Key": bing_key}
    params = {"q": search_terms, "textDecorations": True, "textFormat": "HTML"}

    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()

    search_results = response.json()

    results = list()
    for result in search_results['webPages']['value']:
        results.append({
            'title': result['name'],
            'link': result['url'],
            'summary': result['snippet'],
        })
    return results


def main():
    search_terms = str(input('Введите поисковый запрос'))
    print(run_query(search_terms))

if __name__ == '__main__':
    main()


