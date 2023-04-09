import requests
from bs4 import BeautifulSoup


def main(url):
    with requests.Session() as req:
        r = req.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        target = [
            f"https://www.valeofglamorgan.gov.uk{item['href']}"
            for item in soup.select("a[href$='.csv']")
        ]
        for x in target:
            print(f"Downloading {x}")
            r = req.get(x)
            name = x.rsplit("/", 1)[-1]
            with open(name, "wb") as f:
                f.write(r.content)


main("https://www.valeofglamorgan.gov.uk/en/our_council/Council-Finance.aspx")


# https://www.valeofglamorgan.gov.uk/Documents/Our%20Council/Council/Finance/2022/Payables-greater-than-500-Apr-Excel-2022.xlsx
# https://www.valeofglamorgan.gov.uk/en/our_council/Council-Finance.aspx/Documents/Our%20Council/Council/Finance/2022/Payables-greater-than-500-Apr-2022.csv
