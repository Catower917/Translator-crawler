import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseurl = "https://papago.naver.com/?sk=ko&tk=en&st="
plusurl = input("번역할 내용을 입력하시오 : ")
url = baseurl + urllib.parse.quote_plus(plusurl)

html = urllib.request.urlopen(url).read()


soup = BeautifulSoup(html, "html.parser")
text = soup.select('div')

print(text)
