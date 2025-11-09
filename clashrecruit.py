import requests

headers = {

    "Content-Type" : "application/json",
    "Authorization" :"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjQ2YjdiNzc2LTY4OGMtNDE1OS1iMjFmLTQzODFjNWYyYTIwNSIsImlhdCI6MTc2MjYzNjU2OSwic3ViIjoiZGV2ZWxvcGVyLzI4NjU3YTI4LTk5NWQtYmY3YS05NzRlLWEwNDViMWU2YzEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0Mi4xOTguMTAzLjE0NiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.8gLAKzH8pQ0-hDUA4aaRelqlOL48NXy5k29by0c-1PKkjgNCyfr_c8V-1Z_Huaa4jV2y2EgUhouNbZY-hmW1Bw" 
}
class Recruiter:
    def __init__(self, name, clan_name):
        self.name = name
        self.clan_name = name


    def print_info(self):
        print(self.name + self.clan_name)

def get_user():

    user_tag = input("Please enter your user tag: #")

    response = requests.get(
        'https://api.clashofclans.com/v1/players/%23'+user_tag, headers = headers)
    storage = response.json()
    # print(storage)

    for key in storage:
        if key == "leagueTier":
            league = storage[key]["name"]

            if "P.E.K.K.A" in league:
                print(storage[key]["name"])
                
            elif "Valkyrie" in league:
                print(storage[key]["name"])

            elif "Skeleton" in league:
                print(storage[key]["name"])

            else:
                print("other")




get_user()
#jon was here
#arkaaz was here
