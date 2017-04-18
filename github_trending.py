import requests
import json
from datetime import datetime, date, time, timedelta

params = {'page': 1, 'per_page': 20}


def get_trending_repositories():
    date_today = datetime.date(datetime.now())
    date_before_week = date_today - timedelta(days=7)
    date_search = str(date_before_week) + '..' + str(date_today)

    url = 'https://api.github.com/search/repositories?q=created:' + date_search + '&sort=stars'
    repositories = requests.get(url, params)

    repos = repositories.json()
    for new_repo in repos["items"]:
        print('--------------------------------------------------')
        print('Name: {}, count stars: {}, count open isues: {}'.format(new_repo['name'], new_repo['stargazers_count'], new_repo['open_issues']))
        if new_repo['open_issues'] > 0:
            print('Open issues:')
            get_open_issues_amount(new_repo['owner'], new_repo['name'])
        else:
            print('NO open issues')


def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/' + repo_owner['login'] + '/' + repo_name +'/issues'
    list_issusies = requests.get(url, params)

    issues = list_issusies.json()
    for issue in issues:
        print('----',issue['html_url'])


if __name__ == '__main__':
    get_trending_repositories()
