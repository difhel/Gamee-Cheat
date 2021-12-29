import hashlib
import json
import requests
from requests.structures import CaseInsensitiveDict
def get_checksum(score,playTime,url):
	gameStateData = ""
	str2hash = f"{score}:{playTime}:{url}:{gameStateData}:crmjbjm3lczhlgnek9uaxz2l9svlfjw14npauhen"
	result = hashlib.md5(str2hash.encode())
	checksum = result.hexdigest()
	return checksum

def get_token(Gameurl):
	url = "http://api.service.gameeapp.com"
	headers = CaseInsensitiveDict()
	headers["Host"] = "api.service.gameeapp.com"
	headers["Connection"] = "keep-alive"
	headers["Content-Length"] = "224"
	headers["client-language"] = "en"
	headers["x-install-uuid"] = "0c1cd354-302a-4e76-9745-6d2d3dcf2c56"
	headers["sec-ch-ua-mobile"] = "?0"
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"
	# headers["sec-ch-ua"] = "" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96""
	headers["sec-ch-ua-platform"] = "Windows"
	headers["Content-Type"] = "application/json"
	headers["Accept"] = "*/*"
	headers["Origin"] = "https://prizes.gamee.com"
	headers["Sec-Fetch-Site"] = "cross-site"
	headers["Sec-Fetch-Mode"] = "cors"
	headers["Sec-Fetch-Dest"] = "empty"
	headers["Referer"] = "https://prizes.gamee.com/"
	headers["Accept-Encoding"] = "gzip, deflate, br"
	headers["Accept-Language"] = "en-US,en;q=0.9"
	data = '{"jsonrpc":"2.0","id":"user.authentication.botLogin","method":"user.authentication.botLogin","params":{"botName":"telegram","botGameUrl":"'+Gameurl+'","botUserIdentifier":null}}'
	resp = requests.post(url, headers=headers, data=data)
	# print(resp.status_code)
	result_data = resp.json()
	# print(result_data)
	token = result_data['result']['tokens']['authenticate']
	# print(token)
	return token

def game_id(game_url):

	url = "https://api.service.gameeapp.com/"

	headers = CaseInsensitiveDict()
	headers["accept"] = "*/*"
	headers["accept-encoding"] = "gzip, deflate, br"
	headers["accept-language"] = "en-US,en;q=0.9"
	headers["cache-control"] = "no-cache"
	headers["client-language"] = "en"
	headers["content-length"] = "173"
	headers["Content-Type"] = "application/json"
	headers["origin"] = "https://prizes.gamee.com"
	headers["pragma"] = "no-cache"
	headers["referer"] = "https://prizes.gamee.com/"
	# headers["sec-ch-ua"] = "" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96""
	headers["sec-ch-ua-mobile"] = "?0"
	headers["sec-ch-ua-platform"] = "Windows"
	headers["sec-fetch-dest"] = "empty"
	headers["sec-fetch-mode"] = "cors"
	headers["sec-fetch-site"] = "cross-site"
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"

	data = '{"jsonrpc":"2.0","id":"game.getWebGameplayDetails","method":"game.getWebGameplayDetails","params":{"gameUrl":"'+game_url+'"}}'


	resp = requests.post(url, headers=headers, data=data)

	result_data = resp.json()
	# print(result_data)
	return result_data['result']['game']['id']

def send_score(score,timePlay,checksum,token,game_url,game_id):
	url = "http://api.service.gameeapp.com"

	headers = CaseInsensitiveDict()
	headers["Host"] = "api.service.gameeapp.com"
	headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/89.0.4389.90 Safari/537.36"
	headers["Accept"] = "*/*"
	headers["Accept-Language"] = "en-US,en;q=0.5"
	headers["Accept-Encoding"] = "gzip, deflate"
	headers["X-Install-Uuid"] = "91516df9-f651-40ef-9c11-ccd357429228"
	headers["Client-Language"] = "en"
	headers["Content-Type"] = "application/json"
	headers["Origin"] = "https://prizes.gamee.com"
	headers["Referer"] = "https://prizes.gamee.com/"
	headers["Sec-Fetch-Dest"] = "empty"
	headers["Sec-Fetch-Mode"] = "cors"
	headers["Sec-Fetch-Site"] = "cross-site"
	headers["Te"] = "trailers"
	headers["Authorization"] = "Bearer {my_token}".format(my_token=token)
	#  eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOiIxNjQwNjUyNTE4IiwidXNlcklkIjoxNTQzMDIzOSwiaW5zdGFsbFV1aWQiOiJlNjgyZjhkYS02ZjY3LTRjODQtYTI5My1mMDk0YjBkYzc0ZGYiLCJ0eXBlIjoiYXV0aGVudGljYXRpb25Ub2tlbiIsImF1dGhvcml6YXRpb25MZXZlbCI6ImJvdCIsInBsYXRmb3JtIjoiYm90LXRlbGVncmFtIn0.VkWEgipqHWjpT01tebhn-oOj0sPD8c_W7UBnE9KTgfo
	data = '{"jsonrpc":"2.0","id":"game.saveWebGameplay","method":"game.saveWebGameplay","params":{"gameplayData":{"gameId":'+str(game_id)+',"score":'+str(score)+',"playTime":'+str(timePlay)+',"gameUrl":"'+game_url+'","metadata":{"gameplayId":30},"releaseNumber":8,"gameStateData":null,"createdTime":"2021-12-28T03:20:24+03:30","checksum":"'+checksum+'","replayVariant":null,"replayData":null,"replayDataChecksum":null,"isSaveState":false,"gameplayOrigin":"game"}}}'


	resp = requests.post(url, headers=headers, data=data)

	print(resp.status_code)
	print(resp.content)
# https://prizes.gamee.com#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DgdiggXrZVTXZWAYSoPAe
# https://prizes.gamee.com/game-bot/rollerdisco-34106e5c0f111a182e5afe0ddede5c39f2be4fa3#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DhHJUbMEoNfxVRmVmJorD
game_url = '/game-bot/rollerdisco-34106e5c0f111a182e5afe0ddede5c39f2be4fa3'
score = 12104
time = 1309
token = get_token(game_url)
checksum = get_checksum(score, time, game_url)
game_id = game_id(game_url)
send_score(score, time, checksum, token, game_url, game_id)
# https://prizes.gamee.com/game-bot/rollerdisco-34106e5c0f111a182e5afe0ddede5c39f2be4fa3#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DhHJUbMEoNfxVRmVmJorD
# print("{'jsonrpc':'2.0",'id':'user.authentication.botLogin','method':'user.authentication.botLogin','params':{'botName':'telegram','botGameUrl':'u','botUserIdentifier':''}}")
# https://prizes.gamee.com/game-bot/Qru0ALuCQ-453060498ed6e44985181e8627af827634c14461#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DsbCtzuMYGxRLbkVNWMnk
# https://prizes.gamee.com/game-bot/u0yXP5o-9356840cdc7752799b666b4aea9358ab5140d03a#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DnoprfTfzIebnuyxXecEv
# https://prizes.gamee.com/game-bot/Qru0ALuCQ-453060498ed6e44985181e8627af827634c14461#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DsbCtzuMYGxRLbkVNWMnk
# https://prizes.gamee.com/game-bot/rollerdisco-34106e5c0f111a182e5afe0ddede5c39f2be4fa3#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DhHJUbMEoNfxVRmVmJorD
# https://prizes.gamee.com/game-bot/u0yXP5o-9356840cdc7752799b666b4aea9358ab5140d03a#tgShareScoreUrl=tgb%3A%2F%2Fshare_game_score%3Fhash%3DnoprfTfzIebnuyxXecEv