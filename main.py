from datetime import datetime, timezone, timedelta
from scraper import Scraper
import notioner as n


# Inconsistencies that needs to be fixed:
# Date posted
# Inconsistent spacing, strip() the blank spaces

def main():
    
    # Create a scraper object
    ss = Scraper()
    url = "https://www.glassdoor.com/Job/canada-software-intern-jobs-SRCH_IL.0,6_IN3_KO7,22.htm?fromAge=3"
    jobs_glassdoor = ss.get_glassdoor(url, None)
    # url_google = "https://www.google.com/search?q=computing+science+intern+canda&ei=RtDmY_jjAuS30PEP29efCA&uact=5&oq=computing+science+intern+canda&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIECCEQFTILCCEQFhAeEPEEEB06CggAEEcQ1gQQsAM6BQghEKABOggIIRAWEB4QHToJCAAQFhAeEPEEOgUIABCGA0oECEEYAEoECEYYAFCPIFioImCxI2gCcAF4AIABowGIAbwEkgEDMC40mAEAoAEByAEIwAEB&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwjjp-f-ioz9AhVhIn0KHQXzB38QudcGKAF6BAgYECk#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today&htischips=date_posted;today&htidocid=svzAopNcfaAAAAAAAAAAAA%3D%3D"
    url_google = "https://www.google.com/search?q=computing+science+intern+canada&ei=RtDmY_jjAuS30PEP29efCA&uact=5&oq=computing+science+intern+canda&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIECCEQFTILCCEQFhAeEPEEEB06CggAEEcQ1gQQsAM6BQghEKABOggIIRAWEB4QHToJCAAQFhAeEPEEOgUIABCGA0oECEEYAEoECEYYAFCPIFioImCxI2gCcAF4AIABowGIAbwEkgEDMC40mAEAoAEByAEIwAEB&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwjjp-f-ioz9AhVhIn0KHQXzB38QudcGKAF6BAgYECk#fpstate=tldetail&htivrt=jobs&htidocid=5zLISZiCuhEAAAAAAAAAAA%3D%3D"
    jobs_google = ss.get_google(url_google, None)
    # url_indeed = "https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=8280af2280ba31d1"
    url_indeed = "https://ca.indeed.com/jobs?q=software+intern&l=Canada&fromage=3&vjk=1ffe64efd5f7bc57"
    jobs_indeed = ss.get_indeed(url_indeed, None)
    
    data = jobs_glassdoor + jobs_google + jobs_indeed
    
    unique_data = {}
    for item in data:
        key = tuple(item[:2])  # Extract the first three indexes as a tuple
        if key not in unique_data:
            unique_data[key] = item
            
    # Convert the dictionary values back to a list
    unique_data = list(unique_data.values())
    pages = n.get_primary_keys()
    # print("Data(scraped):",data)
    # print("Unique data(scraped):",unique_data)
    filtered_data = []
    page_entries = [sublist[:2] for sublist in pages]
    for entry in unique_data:
        if entry[:2] not in page_entries:
            filtered_data.append(entry)
    # print("Pages:",pages)
    # print("Filtered data:",filtered_data)
    if len(filtered_data) == 0:
        print("No new entries")
        exit()
    created_pages = [0,0]
    for item in filtered_data:
        date_posted = item[4]
        date_scraped = datetime.now(timezone.utc).astimezone().isoformat() 
        url = item[3]
        platform = item[5]
        company = item[1]
        location = item[2]
        title = item[0]
        data = {
            "Date Posted":{ "date": {"start": date_scraped}},
            "Date Scraped":{ "date": {"start": date_scraped}},
            "URL": {"url": url},
            "Platform": {"rich_text": [{"text": {"content": platform}}]},
            "Company": {"rich_text": [{"text": {"content": company}}]},
            "Location": {"rich_text": [{"text": {"content": location}}]},
            "Title": {"title": [{"text": {"content": title}}]},
        }
        try:
            page = n.create_page(data)
        except Exception as e:
            print("Error creating page:",e)
            created_pages[1]+=1
            continue
        if page[1] == 200:
            created_pages[0]+=1
        else:
            print("Error creating page:",page[0])
            created_pages[1]+=1
    print("Created pages:",created_pages[0])
    print("Failed to create pages:",created_pages[1])
    print("link to notion:","https://www.notion.so/4d38e817b61e4729bd82ae6db962cc97?v=361064490e0c4492b49194bd7ff78783")

if __name__ == "__main__":
    main()