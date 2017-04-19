import requests
import json
from datetime import datetime, date, time, timedelta


def get_trending_repositories(days=7):
    date_today = datetime.date(datetime.now())
    date_before_week = date_today - timedelta(days=days)
    date_search = str(date_before_week) + '..' + str(date_today)
    count_repo = {'page': 1, 'per_page': 20}
    url = 'https://api.github.com/search/repositories?q=created:' + date_search + '&sort=stars'
    repositories = requests.get(url, count_repo)
    return repositories.json()

def print_resualt(repositories):
    for new_repo in repositories["items"]:
        print('--------------------------------------------------')
        print('Name: {}, count stars: {}, count open isues: {}'.format(new_repo['name'], new_repo['stargazers_count'], new_repo['open_issues']))
        if new_repo['open_issues'] > 0:
            print('Open issues:')
            issues = get_open_issues_amount(new_repo['owner'], new_repo['name'])
            for issue in issues:
                print('----',issue['html_url'])
        else:
            print('NO open issues')


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/' + repo_owner['login'] + '/' + repo_name +'/issues'
    list_issusies = requests.get(url)
    return list_issusies.json()
    


if __name__ == '__main__':
    repositories = get_trending_repositories()
    print_resualt(repositories)
