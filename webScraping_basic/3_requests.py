import requests
res = requests.get("http://gogle.com")
#res = requests.get("http://nadocoding.tistory.com")
res.raise_for_status()  # 오류가 생기면 오류 출력, 프로그램 종료
# print("응답코드 :", res.status_code)  # 200이면 정상

# if res.status_code == requests.codes.ok: #requests.codes.ok = 200
#     print("정상입니디")
# else:
#     print("문제가 생겼습니다. [에러코드 ", res.status_code, "]")

print(len(res.text))
print(res.text)

with open("webScraping_basic/mygoogle.html", "w", encoding="utf8") as f:
    f.write(res.text)
