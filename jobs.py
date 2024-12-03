import requests as re
from bs4 import BeautifulSoup

def getJobs(role : str):
    jobs = []

    response = re.get(f"https://wellfound.com/role/{role}")
    content = BeautifulSoup(response.content,
                            "html.parser")
    allcompanies = content.find_all("div", {"class": "mb-6"})

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
                "role": opening.find("a").text if opening.find("a") != None else "" ,
                "type": opening.find("span").text  if opening.find("span") is not None else "",
                "salary": opening.find("span", {"class": "pl-1"}).text if opening.find("span", {"class": "pl-1"}) is not None else "" ,
                "link": opening.find("a")["href"]  if opening.find("a") is not None else ""
            }
            obj["jobs"].append(openingdetail)
        jobs.append(obj)
    return  jobs