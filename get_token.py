import requests
from requests.structures import CaseInsensitiveDict

url = "https://firebaseinstallations.googleapis.com/v1/projects/gamee-app/installations"

headers = CaseInsensitiveDict()
headers["accept"] = "application/json"
headers["accept-encoding"] = "gzip, deflate, br"
headers["accept-language"] = "en-GB,en;q=0.9,fa-IR;q=0.8,fa;q=0.7,ar-AE;q=0.6,ar;q=0.5,en-US;q=0.4"
headers["cache-control"] = "no-cache"
headers["content-length"] = "131"
headers["Content-Type"] = "application/json"
headers["origin"] = "https://prizes.gamee.com"
headers["pragma"] = "no-cache"
headers["referer"] = "https://prizes.gamee.com/"
# headers["sec-ch-ua"] = "" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96""
headers["sec-ch-ua-mobile"] = "?0"
headers["sec-ch-ua-platform"] = "Linux"
headers["sec-fetch-dest"] = "empty"
headers["sec-fetch-mode"] = "cors"
headers["sec-fetch-site"] = "cross-site"
headers["user-agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
headers["x-client-data"] = "CKW1yQEIlLbJAQiitskBCKmdygEInvnLAQjmhMwBCLaFzAEIy4nMAQiZj8wBCNKPzAEYjp7LAQ=="
headers["x-goog-api-key"] = "AIzaSyB4tdrYX6bsx4TKn4mDGRJ4rxoXfNI9txw"

# data = '{"fid":"f6wYksl6sfTwWHwaKdMMbz","authVersion":"FIS_v2","appId":"1:138287423652:web:8590c3fefe786faf554631","sdkVersion":"w:0.4.17"}'
# {"fid":"f8fxrZoqNx8KRmVPnDRCO8","authVersion":"FIS_v2","appId":"1:138287423652:web:8590c3fefe786faf554631","sdkVersion":"w:0.4.17"}
#{"fid":"dZ4JsJzioOlfLwSH6WGpC2","authVersion":"FIS_v2","appId":"1:138287423652:web:8590c3fefe786faf554631","sdkVersion":"w:0.4.17"}

data = '{"fid":"cmQXIfrralzwghxx453_1_","authVersion":"FIS_v2","appId":"1:138287423652:web:8590c3fefe786faf554631","sdkVersion":"w:0.4.17"}'
resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)
print(resp.content)