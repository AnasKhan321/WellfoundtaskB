import requests as re
from bs4 import BeautifulSoup
import random


USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
]

proxies = {
    "http": "http://103.191.218.153:8090",
    "https": "http://103.191.218.153:8090"
}
def getJobs(role: str):
    jobs = []
    headers = {
        'User-Agent': random.choice(USER_AGENTS),
        'Referer': 'https://wellfound.com/'
    }

    try:

        response = re.get(f"https://wellfound.com/role/{role}", headers=headers  ,  proxies=proxies, timeout=10)
        content = BeautifulSoup(response.content,
                                "html.parser")
    except Exception as e :
        return []

    print(response.content)
    if response.status_code != 200:
        print("Failed to retrieve content")
        return []

    print(content)
    allcompanies = content.find_all("div", {"class": "mb-6"})

    if len(allcompanies) > 0:
        allcompanies.pop()

    for item in allcompanies:
        companyname = item.find("h2", {"class": "font-semibold"})
        jobopenings = item.find_all("div", {"class": "min-h-[50px]"})
        obj = {
            "Company": companyname.text if companyname is not None else "",
            "jobs": []
        }
        for opening in jobopenings:
            openingdetail = {
                "role": opening.find("a").text if opening.find("a") != None else "",
                "type": opening.find("span").text if opening.find("span") is not None else "",
                "salary": opening.find("span", {"class": "pl-1"}).text if opening.find("span", {
                    "class": "pl-1"}) is not None else "",
                "link": opening.find("a")["href"] if opening.find("a") is not None else ""
            }
            obj["jobs"].append(openingdetail)
        jobs.append(obj)
    return jobs
