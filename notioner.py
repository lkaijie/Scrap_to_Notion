import requests
import json
from datetime import datetime, timezone, timedelta
from config import notion_token, database_id
import time


headers = {
    "Authorization": "Bearer " + notion_token,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

# Notion API endpoint
url = "https://api.notion.com/v1/databases/" + database_id + "/query"

def get_pages():
    ''' Get all pages from Notion database'''
    
    
    payload = {"page_size": 200}
    res = requests.post(url, headers=headers, json=payload)
    # print(res.json())
    
    data=res.json()['results']
    # print(data)
    
    with open('notiondb1.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    
    return res.json()['results']


def create_page(data: dict):
    create_url = "https://api.notion.com/v1/pages"
    
    payload = {"parent":{"database_id":database_id}, "properties":data}
    
    res = requests.post(create_url, headers=headers, json=payload)
    print("create page:",res.status_code)
    if res.status_code == 400:
        print(data)
    
    return res.json(), res.status_code

def update_page(page_id, data: dict):
    url = "https://api.notion.com/v1/pages/" + page_id
    
    payload = {"properties":data}
    
    res = requests.patch(url, headers=headers, json=payload)
    print("update page:",res.status_code)
    return res.json()

def get_primary_keys()-> list:
    pages = get_pages()
    title_company_location = []
    for x in pages:
        try:
            title_company_location.append([x['properties']['Title']["title"][0]["text"]["content"], 
                                        x['properties']['Company']["rich_text"][0]["text"]["content"], 
                                        x['properties']['Location']["rich_text"][0]["text"]["content"]
                                        ])
        except Exception as e:
            print(e)            
    return title_company_location
    
def main():
    # get all pages
    # get_pages()
    # title_company_location = get_primary_keys()
    # print("HERE IS THE LIST OF ENTRIES CHECK FOR DUPLICATES HERE:")
    # print(title_company_location)
    # # print(title_company_location)
    # print("------------------")
    # # create a sample page
    # url = "https://www.indeed.com/viewjob?jk=8b5b5b5b5b5b5b5b"
    # title = "Software Engineer"
    # company = "Indeed"
    # location = "Remote"
    # platform = "Indeed"
    # date_posted = datetime.now(timezone.utc).astimezone().isoformat()
    # date_scraped = datetime.now(timezone.utc).astimezone().isoformat() 
    # data = {
    #     "Date Posted":{ "date": {"start": date_posted}},
    #     "Date Scraped":{ "date": {"start": date_scraped}},
    #     # "URL": {"title": [{"text": {"content": url}}]},
    #     "URL": {"url": url},
    #     "Platform": {"rich_text": [{"text": {"content": platform}}]},
    #     "Company": {"rich_text": [{"text": {"content": company}}]},
    #     "Location": {"rich_text": [{"text": {"content": location}}]},
    #     "Title": {"title": [{"text": {"content": title}}]},
    # }

    # create_page(data)
    # time.sleep(5)

    # # update page
    # id = "87d8e120-60d4-4cba-8ba1-0eccc01c45a2"

    # title = "updated title"
    # company = "updated company"
    # updated_data = {"Title": {"rich_text": [{"text": {"content": title}}]},"Company": {"rich_text": [{"text": {"content": company}}]}}
    # update_page(id, updated_data)
    
    
    # print("creating page")
    # date_scraped = datetime.now(timezone.utc).astimezone().isoformat()
    # platform = "Indeed"
    # company = "Indeed"
    # location = "Remote"
    # title = "Software Engineerrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr"
    # data = {
    #         "Date Posted":{ "date": {"start": date_scraped}},
    #         "Date Scraped":{ "date": {"start": date_scraped}},
    #         "URL": {"url": url},
    #         "Platform": {"rich_text": [{"text": {"content": platform}}]},
    #         "Company": {"rich_text": [{"text": {"content": company}}]},
    #         "Location": {"rich_text": [{"text": {"content": location}}]},
    #         "Title": {"title": [{"text": {"content": title}}]},
    #     }
    # create_page(data)
    
    
    with open('notiondb1.json', 'r', encoding='utf8') as f:
        data = json.load(f)
        print(data[1])
    
if __name__ == "__main__":
    main()