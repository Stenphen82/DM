import requests
import string
from lxml import html

def user_info(user_id):

    content = requests.get(url="https://www.shiyanlou.com/user/" + user_id)
    
    if not bool(content):
        user_name, user_level, join_date = None, None, None
    
    else:
        tree = html.fromstring(content.text)
        tree.xpath('//span[@class="username"]/text()')
        
        user_name=str(tree.xpath('//span[@class="username"]/text()')).strip(string.punctuation)
        
        user_level=int(str(tree.xpath('//span[@class="user-level"]/text()')).strip(string.punctuation).strip('L'))

        join_date_orig=tree.xpath('//span[@class="join-date"]/text()')
        a,b=str(join_date_orig).split()
        join_date=a.strip(string.punctuation)

    return user_name, user_level, join_date

user_info("214893")
