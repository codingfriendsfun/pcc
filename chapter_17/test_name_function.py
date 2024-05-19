import pytest

from python_repos_for_test import api_call, dictionary_convert, check_results
from python_repos_for_test import get_repo_info, explore_single_repo


@pytest.fixture
def website():
    """Get a response object"""
    r = api_call()
    return r

def test_api_call(website):
    "Test that API call worked"
    assert website.status_code == 200

def test_get_repo_info(website):
    """Test expected number of repositories returned"""
    response_dict = get_repo_info(website)
    
    num_dicts =  len(response_dict)
    assert num_dicts >= 200
    

# Test total number repositories > 100

# if bored, test completed results = True