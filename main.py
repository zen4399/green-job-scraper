import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

url = "https://www.green-japan.com/job/engineer"

res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, "html.parser")

jobs = soup.select(".cassetteRecruit")

job_list = []

for job in jobs:
    title = job.select_one(".cassetteRecruit__copy").get_text(strip=True)
    company = job.select_one(".cassetteRecruit__name").get_text(strip=True)
    link = "https://www.green-japan.com" + job.select_one("a.cassetteRecruit__copyLink")["href"]

    job_list.append({
        "求人タイトル": title,
        "企業名": company,
        "詳細ページURL": link
    })
    time.sleep(0.5)  # 負荷対策

df = pd.DataFrame(job_list)
df.to_csv("green_jobs.csv", index=False, encoding="utf-8-sig")
