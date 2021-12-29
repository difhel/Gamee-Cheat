import requests
from requests.structures import CaseInsensitiveDict

url = "http://api.service.gameeapp.com"

headers = CaseInsensitiveDict()
headers["Host"] = "api.service.gameeapp.com"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/89.0.4389.90 Safari/537.36"
headers["Accept"] = "*/*"
headers["Accept-Language"] = "en-US,en;q=0.5"
headers["Accept-Encoding"] = "gzip, deflate"
# headers["X-Install-Uuid"] = "91516df9-f651-40ef-9c11-ccd357429228"
headers["Client-Language"] = "en"
headers["Content-Type"] = "application/json"
headers["Origin"] = "https://prizes.gamee.com"
headers["Referer"] = "https://prizes.gamee.com/"
headers["Sec-Fetch-Dest"] = "empty"
headers["Sec-Fetch-Mode"] = "cors"
headers["Sec-Fetch-Site"] = "cross-site"
headers["Te"] = "trailers"
headers["Authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOiIxNjQwNjkyNjYxIiwidXNlcklkIjoxNTQzMDIzOSwiaW5zdGFsbFV1aWQiOiIwYzFjZDM1NC0zMDJhLTRlNzYtOTc0NS02ZDJkM2RjZjJjNTYiLCJ0eXBlIjoiYXV0aGVudGljYXRpb25Ub2tlbiIsImF1dGhvcml6YXRpb25MZXZlbCI6ImJvdCIsInBsYXRmb3JtIjoiYm90LXRlbGVncmFtIn0.7R5DivzKXPtoqWZ35kL5YOsTCKLA1Lx-OJ2ptSPF2uU"
#  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOiIxNjQwNjUyNTE4IiwidXNlcklkIjoxNTQzMDIzOSwiaW5zdGFsbFV1aWQiOiJlNjgyZjhkYS02ZjY3LTRjODQtYTI5My1mMDk0YjBkYzc0ZGYiLCJ0eXBlIjoiYXV0aGVudGljYXRpb25Ub2tlbiIsImF1dGhvcml6YXRpb25MZXZlbCI6ImJvdCIsInBsYXRmb3JtIjoiYm90LXRlbGVncmFtIn0.VkWEgipqHWjpT01tebhn-oOj0sPD8c_W7UBnE9KTgfo
data = '{"jsonrpc":"2.0","id":"game.saveWebGameplay","method":"game.saveWebGameplay","params":{"gameplayData":{"gameId":268,"score":45,"playTime":245,"gameUrl":"/game-bot/bj6dEMMXfq-6e52c18c9c37c98764c3186d90c1aab98c08910d","metadata":{"gameplayId":30},"releaseNumber":8,"gameStateData":null,"createdTime":"2021-12-28T03:20:24+03:30","checksum":"921103e4b4befc6257a4d91882100e3c","replayVariant":null,"replayData":null,"replayDataChecksum":null,"isSaveState":false,"gameplayOrigin":"game"}}}'


resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
print(resp.content)