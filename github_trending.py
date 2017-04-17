import requests, json
from datetime import datetime, date, time, timedelta

def get_trending_repositories(top_size=20):
    #get dates for search
    date_today = datetime.date(datetime.now())
    date_before_week = date_today - timedelta(days=7)
    #get request for github
    date_search = str(date_before_week) + '..' + str(date_today)
    url = 'https://api.github.com/search/repositories?q=created:' + date_search + '&sort=stars'
    params = {'page': 1, 'per_page': top_size}
    repositories = requests.get(url, params)
    my_dict = repositories.json()
    for i in my_dict["items"]:
        print(i['id'], i['stargazers_count'], i['open_issues'], i['name'])
        if i['open_issues'] > 0:
            get_open_issues_amount(i['owner'], i['name'])




def get_open_issues_amount(repo_owner, repo_name):
    url = 'https://api.github.com/repos/' + repo_owner['login'] + '/' + repo_name +'/issues'
    params = {'page': 1, 'per_page': 20}
    list_issusies = requests.get(url, params)
    my_dict = list_issusies.json()
    for i in my_dict:
        print(i['html_url'])


if __name__ == '__main__':
    get_trending_repositories()
    #repo_owner, repo_name = get_trending_repositories()
    #get_open_issues_amount(repo_owner, repo_name)
