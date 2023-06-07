from datetime import datetime, timezone, timedelta
from scraper import Scraper
import notioner as n


# Inconsistencies that needs to be fixed:
# Date posted
# Inconsistent spacing, strip() the blank spaces


ss = Scraper()

url = "https://www.glassdoor.com/Job/canada-software-intern-jobs-SRCH_IL.0,6_IN3_KO7,22.htm?fromAge=3"
# test = n.get_pages()
jobs_glassdoor = ss.get_glassdoor(url, None)
# https://www.glassdoor.ca/partner/jobListing.htm?pos=105&ao=1136043&s=58&guid=0000018896c945e895afc89a069ccff0&src=GD_JOB_AD&t=SR&vt=w&uido=AF88B208036661754A76D7BCDAB6CDD6&cs=1_4b4f1aa2&cb=1686156953278&jobListingId=1008624007095&jrtk=3-0-1h2bcihgdm6qe801-1h2bcihhci9ii800-fb7ab2c6af859dbf-
# print(jobs)
url_google = "https://www.google.com/search?q=computing+science+intern+canda&ei=RtDmY_jjAuS30PEP29efCA&uact=5&oq=computing+science+intern+canda&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIHCCEQoAEQCjIECCEQFTILCCEQFhAeEPEEEB06CggAEEcQ1gQQsAM6BQghEKABOggIIRAWEB4QHToJCAAQFhAeEPEEOgUIABCGA0oECEEYAEoECEYYAFCPIFioImCxI2gCcAF4AIABowGIAbwEkgEDMC40mAEAoAEByAEIwAEB&sclient=gws-wiz-serp&ibp=htl;jobs&sa=X&ved=2ahUKEwjjp-f-ioz9AhVhIn0KHQXzB38QudcGKAF6BAgYECk#htivrt=jobs&fpstate=tldetail&htichips=date_posted:today&htischips=date_posted;today&htidocid=svzAopNcfaAAAAAAAAAAAA%3D%3D"
jobs_google = ss.get_google(url_google, None)
# print(jobs_google)

url_indeed = "https://ca.indeed.com/jobs?q=software+intern&fromage=1&vjk=8280af2280ba31d1"
jobs_indeed = ss.get_indeed(url_indeed, None)
# print(jobs_indeed)
# in format             
# job_list.append([title, company, location, url, listing_age, "glassdoor"])    


data = jobs_glassdoor + jobs_google + jobs_indeed

unique_data = {}

for item in data:
    key = tuple(item[:3])  # Extract the first three indexes as a tuple
    if key not in unique_data:
        unique_data[key] = item
        
# Convert the dictionary values back to a list
unique_data = list(unique_data.values())

pages = n.get_primary_keys()
filter_keys = set(tuple(item[:3]) for item in pages)

filtered_data = [item for item in unique_data if tuple(item[:3]) not in filter_keys]

if len(filtered_data) == 0:
    print("No new entries")
    exit()
for item in filtered_data:
    # print(item)
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
    # job_list.append([title, company, location, url, listing_age, "glassdoor"])
    n.create_page(data)

