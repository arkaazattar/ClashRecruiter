import requests

headers = {

    "Content-Type" : "application/json",
    "Authorization" :"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjYzYTExOGFjLTYyMmQtNGJiNS05ZDI5LTQ4NjUwNGI1ZDgwZSIsImlhdCI6MTc1ODc3NzA3NSwic3ViIjoiZGV2ZWxvcGVyLzIyNDQwY2MxLWMyMDUtMDI0YS04NTFiLTY3ZjAxYjY4Y2E1OSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0Mi4xODkuOTkuMjM4IiwiMTQyLjExNS4zNi4xODAiXSwidHlwZSI6ImNsaWVudCJ9XX0.C0q7BiZpjORVy61KWHb_BQzNHSJc7M81QhxURxvLijCtSwNWboFzaWD-ekgmI2-F12Ng4mw_zYGJ12GXMl1d8A" 
}


def get_user():
    response = requests.get(
        'https://api.clashofclans.com/v1/players/%2382GVQYRRL', headers = headers)
    storage = response.json()
    # print(user_json)

    for key in storage:
        if key == "trophies":
            trophies = int(storage[key])

            if trophies > 3000:
                print("This user has over 3000 trophies")
            else:
                print("less than 3000")

get_user()
#jon was here
#arkaaz was here