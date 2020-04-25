import requests
from bs4 import BeautifulSoup


def scrapp_main_div():
    url = "https://forum.pasja-informatyki.pl/questions/programowanie/c-plus-plus"
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    div = str(soup.find(class_='qa-q-list qa-q-list-vote-disabled'))
    div = div.split('qa-q-list qa-q-list-vote-disabled">')[1]
    div = div.split('<!-- END qa-q-list-item --> == $0')[0]
    return div


def list_of_last_posts():
    div = scrapp_main_div()
    list_of_last_posts_data= div.split('<!-- END qa-q-list-item -->')
    list_of_last_posts_data.pop()
    return list_of_last_posts_data

def title_of_post(post_data): ##WORKING VERSION!!!!
    post_data = post_data.split('qa-q-item-title">')[1]

    if ('qam-q-list-close-icon' in post_data):
        post_data = post_data.split('title=', 1)[1]
    post_data = post_data.split('title=')[1]
    post_data = post_data.split('</span>')[0]
    post_data = post_data.split('>')[1]
    return post_data

def describtion_of_post(post_data):
    post_data = post_data.split('qa-q-item-title">')[1]

    if ('qam-q-list-close-icon' in post_data):
        post_data = post_data.split('title=', 1)[1]

    post_data = post_data.split('title=')[1]
    post_data = post_data.split('</span>')[0]

    if("'>" in post_data):
        post_data = post_data.split("'>")[0]
        post_data = post_data.split("'",1)[1]
    else:
        post_data = post_data.split('">')[0]
        post_data = post_data.split('"',1)[1]

    return post_data

def time_of_post_exist(post_data):
    post_data = post_data.split('qa-q-item-when-data">')[1]
    post_data = post_data.split('</span>')[0]
    return post_data

def number_of_answears(post_data):
    post_data = post_data.split('class="qa-a-count-data">')[1]
    post_data = post_data.split('</span>')[0]
    return post_data

def number_of_views(post_data):
    post_data = post_data.split('qa-view-count-data">')[1]
    post_data = post_data.split('</span>')[0]
    return post_data

def author_of_post(post_data):
    post_data = post_data.split('qa-q-item-who-data"')[1]
    post_data = post_data.split('">')[1]
    post_data = post_data.split('</a>')[0]
    return post_data



