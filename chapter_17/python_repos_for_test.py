import requests


def api_call():
    # Make API call; check response
    url = "https://api.github.com/search/repositories"
    url += "?q=language:python+sort:stars+stars:>10000"
    headers = {"Accept": "application/vnd.github.v3+json"}
    
    r = requests.get(url, headers=headers)
    print(f"Status code: {r.status_code}")
    return r


def dictionary_convert(response):
    """Convert response object to dictionary"""
    response_dict=response.json()
    return response_dict


def check_results(response_dict):
    """Print total repositories and check for complete results"""
    print(f"Total repositories: {response_dict['total_count']}")
    print(f"Complete results: {not response_dict['incomplete_results']}")


def get_repo_info(response_dict):
    """Count number of repos"""
    repo_dicts = response_dict['items']
    print(f"Repositories returned: {len(repo_dicts)}")
    
    return repo_dicts


def explore_single_repo(repo_dict):
    """Examine a single repository"""
    print(f"\nInformation on {repo_dict['name']}:")
    print(f"\tOwner: {repo_dict['owner']['login']}")
    print(f"\tStars: {repo_dict['stargazers_count']}")
    print(f"\tRepository: {repo_dict['html_url']}")
    print(f"\tCreated: {repo_dict['created_at']}")
    print(f"\tUpdated: {repo_dict['updated_at']}")
    print(f"\tDescription: {repo_dict['description']}")


response = api_call()
response_dict = dictionary_convert(response)
check_results(response_dict)
repo_dicts = get_repo_info(response_dict)
for repo_dict in repo_dicts:
    explore_single_repo(repo_dict)
