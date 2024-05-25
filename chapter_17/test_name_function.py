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
    response_dict = dictionary_convert(website)
    repo_dicts = get_repo_info(response_dict)
    
    num_dicts =  len(repo_dicts)
    assert num_dicts >= 30
    

def test_total_repositories(website):
    """Test total number repositories > 100"""
    response_dict = dictionary_convert(website)
    total_repos = response_dict['total_count']
    assert total_repos >= 100


def test_complete_results(website):
    """Test for complete results"""
    response_dict = dictionary_convert(website)
    complete = not response_dict['incomplete_results']
    assert complete == True