from bs4 import BeautifulSoup
import requests

data = requests.get("https://monierate.com/").text

soup = BeautifulSoup(data, "lxml")
table = soup.find("tbody", class_="changers")

desired_providers = ["Grey", "CBN", "Klasha", "Chipper Cash", "Payday"]

data_list = []

for tr in table.find_all("tr"):
    columns = tr.find_all("td")

    if columns != []:
        providers = columns[0].text.strip()
        rate = (
            columns[1]
            .text.strip()
            .replace("â¦", "₦")
            .replace("per $1", "")
            .replace("\n", "")
        )
        last_updated = columns[3].text.replace("2023", "")
        modified = last_updated[5:]

        if providers in desired_providers:
            data_list.append([providers, rate, modified])
            # print("provider      rate      last update")
            datas = f"{providers}      {rate}     {last_updated}"
            print(datas)