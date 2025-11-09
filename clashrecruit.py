import requests

headers = {

    "Content-Type" : "application/json",
    "Authorization" :"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRlYTUzNWVhLTljYTAtNDFmMC04MDJlLWIzZjk4YzAyMmMxNCIsImlhdCI6MTc2MjY0NzgxMSwic3ViIjoiZGV2ZWxvcGVyLzI4NjU3YTI4LTk5NWQtYmY3YS05NzRlLWEwNDViMWU2YzEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0Mi4xOTguMTAzLjE0NiIsIjE0Mi4xMjYuMTgwLjE2NiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.3k8c1cIEQgKpyrdKhTBtuTidotVPGTKGg4G-fRbNEvef4TxqvFAQmvIpHBjm2gvko8Sb3iRBFbZCVVw2Y_cpeA" 
}
class Recruiter:
    def __init__(self, name, clan_name):
        self.name = name
        self.clan_name = name


    def print_info(self):
        print(self.name + self.clan_name)

def get_user():
    # list of all league names, lowest to highest - prob not needed
    league_list = ["Skeleton", "Barbarian", "Archer", "Wizard", "Valkyrie", "Witch", "Golem", "P.E.K.K.A", "Titan", "Dragon", "Electro", "Legend"]
    user_tag = input("Please enter your user tag: #")

    response = requests.get(
        'https://api.clashofclans.com/v1/players/%23'+user_tag, headers = headers)
    storage = response.json()
    #print(storage)

    for key in storage:
        if key == "leagueTier":
            league = storage[key]["name"]
            
            print(league)
    



get_user()
#jon was here
#arkaaz was here
