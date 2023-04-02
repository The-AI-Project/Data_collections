import requests
from filter import Filter
head={
"Host": "www.selfstudys.com",
"Accept-Encoding": "gzip, deflate, br",
"DNT": "1",
"Connection": "keep-alive",
"Referer": "https://www.selfstudys.com/mcq/neet/online/mock-test/biology?page=2",
#"Cookie": 'XSRF-TOKEN=eyJpdiI6Ilwva0daQ200VnpRZnNaMVU2VUJNNkt3PT0iLCJ2YWx1ZSI6IlVseFwvSTBHY0ZIcnNWSkFcL3A5M3pNc0dONzJ1ZlJSTWxGWWRKWjFwVDNCT1V1R2pSOGRzblB1Zzc0VDNCbE03MVBzVDUzWjg0Z2pZQVYxVHQ5Q2h1Qnc9PSIsIm1hYyI6ImUyNjgxNmIwMTA4ZmU3ZjU5N2YyZDUxODE0YmYwNjAzYmMzOWQzOGE4Mjc1NmIyNDJjODQ1MzhmYTE4MmY0NzIifQ%3D%3D; laravel_session=eyJpdiI6IkVtVzBKeG9jTHQyZGFaQ3VvV0VxUEE9PSIsInZhbHVlIjoiXC9Rc1BuYUlFNllDN2VCV1gxN05YUVc0bE9iY29DYXRZRzlzZ2N4NnBNWnA0a3EzZkJ4UG53VVgzMHZIVENGaEczSEZkemNVeEozRVNUQWJJQ3psMkV3PT0iLCJtYWMiOiJkMDY3MWU3Njk4YWJlZGE4NWI3NDdmMTJlOTA4NmZlZTBmNGI4ZWMzMzRiZDc2M2YwMGZjMjlhZjMxOTEzYzhmIn0%3D; _ga_37JFJQ7LER=GS1.1.1679659037.1.1.1679661696.0.0.0; _ga=GA1.1.1434393468.1679659037; g_state={"i_p":1679666247960,"i_l":1}',
"Upgrade-Insecure-Requests": "1",
"Sec-Fetch-Dest": "document",
"Sec-Fetch-Mode": "navigate",
"Sec-Fetch-Site": "same-origin",
"Sec-Fetch-User": "?1"
}
url=f"https://www.selfstudys.com/mcq/neet/online/mock-test/biology/biology-test-"#then use next link to hover between questions
#https://www.selfstudys.com/mcq/neet/online/mock-test/biology/biology-test-189
re=requests.Session()
for moc in range(1,190):
    with open("dataa.html","w+",encoding='utf-8')as file:
       file.write(re.get(url+str(moc),headers=head).text)
       file.close()
    Filter(moc)

