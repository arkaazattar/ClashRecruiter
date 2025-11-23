import requests

headers = {

    "Content-Type" : "application/json",
    "Authorization" :"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRlYTUzNWVhLTljYTAtNDFmMC04MDJlLWIzZjk4YzAyMmMxNCIsImlhdCI6MTc2MjY0NzgxMSwic3ViIjoiZGV2ZWxvcGVyLzI4NjU3YTI4LTk5NWQtYmY3YS05NzRlLWEwNDViMWU2YzEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0Mi4xOTguMTAzLjE0NiIsIjE0Mi4xMjYuMTgwLjE2NiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.3k8c1cIEQgKpyrdKhTBtuTidotVPGTKGg4G-fRbNEvef4TxqvFAQmvIpHBjm2gvko8Sb3iRBFbZCVVw2Y_cpeA" 
}

class API:
    def __init__(self, user_tag, api):
        self.token = False
        self.user_tag = user_tag
        self.reason = 0 # should be string but wtv
        self.json_data = {
            "token": str(api)
        }
        #api is one time use, no point of storing it 
    def check_player(self):
        url = f"https://api.clashofclans.com/v1/players/%23{self.user_tag}"
        response = requests.get(url, headers=headers)
        self.storage = response.json() 

        if self.storage.get("reason") == "notFound":
            self.reason = "Player tag is incorrect" 
            return False
        return True
    
    def check_player_api(self):
        #logic might be broken
        url = f"https://api.clashofclans.com/v1/players/%23{self.user_tag}/verifytoken"

        response = requests.post(url, headers=headers, json = self.json_data)
        self.storage = response.json() # Important!! this storage now holds whether the api key is valid or not

        if self.storage.get("status") == "invalid":
            self.reason = "API Token is incorrect"

        elif self.storage.get("status") == "ok":
            self.token = True # set token value to 1 in boolean. this makes it easy to check if token info is correct

        else: self.reason = self.storage  

        print(self.storage)
        return self.token #dont really need to store token in class, as its being returned anyways. keeping for now in the case that we need it for error checking.

class Advertisement:

    def __init__(self, requirements, Recruiter):
        self.requirements = requirements

    
class Recruiter: # error checking needs to be done out of class
    
    requirements = []

    def __init__(self, user_tag, clan_tag):
        self.user_tag = user_tag
        self.clan_tag = clan_tag

    def print_info(self): # idk why we would need this 
        print(self.user_tag + " " + self.clan_tag)

    def check_if_leader(self):
        roles = ["leader", "coleader", "admin"]
        is_leader =  False
        #GET API INFO
        response = requests.get(
            f"https://api.clashofclans.com/v1/clans/%23{self.clan_tag}/members", headers = headers)
        #Store api info
        self.storage = response.json()
        #print(self.storage)
        if self.storage.get("reason") == "notFound":
            return
        large_list = self.storage.get("items")
        #print(large_list)
        for player_info in large_list:    
            if (player_info.get("tag"))[1:] == self.user_tag: #user_tag needs to never have a #
                if player_info.get("role").lower() in roles:
                  is_leader = True
        return is_leader     

    def post_ad(self):
        print(self.requirements)

    def set_requirements(self, th_level, League):

        self.requirements = [th_level, League]

    def get_requirements(self):
        return self.requirements


class Recruitee:
    # everything here now needs to call back to api request

    def __init__(self, user_tag):
        self.user_tag = user_tag

def ask_if_recruiting():
    invalid_input = True
    while invalid_input:
        recruiting = input("Are you recuiting? Yes or no: ").lower()
        if recruiting == "yes" or  recruiting == "no" or recruiting == 'test':
            invalid_input = False
        else: print("Invalid input")
    return recruiting # returns yes, no, or test

def check_api():
    valid_api = False
    while valid_api == False:
        user_tag = input("Please enter your player tag: #")
        tag_check = API(user_tag, "")
        if tag_check.check_player() == False:
            print(f"{tag_check.reason}, try again.")
            continue
        api = input("Please enter your API token: ")
        user = API(user_tag, api)
        user.check_player_api()
        if user.token == True:
            valid_api = True
        else: print(f"{user.reason}, try again") 
    return(user_tag)

def recruiting(user_tag): 
    invalid_clan = True
    while invalid_clan:
        clan_tag = input("Enter Clan Tag: #")
        try:   
            if clan_tag[0] == '#':
                clan_tag = clan_tag[1:]
        except:
            continue
        clan = Recruiter(user_tag, clan_tag)
        if clan.check_if_leader() == True:
            invalid_clan = False
        else: print("Clan not found, try again?")
    return
        #print(clan.storage)

def recruitee():
    invalid_input = True
    while invalid_input:
        looking_for_clan = input("Are you looking for a clan? Yes or no: ").lower()
        if looking_for_clan == "yes" or  looking_for_clan == "no":
            if looking_for_clan == "no":
                exit() # kill program ? prob wont be needed when made into website
            else: invalid_input = False
        else: print("Invalid input")
    return

def get_user():
    response = ask_if_recruiting()
    user_tag = check_api()
    if response == "yes":
        recruiting(user_tag)
    if response == "no":
        recruitee()

    

#TESTING OBJECTS HERE !! !! !! ts dont work anymore </3
    if recruiting == "test":
        #INITIALIZE RECRUITER TEST
        name = input("Recruiter Name: ")
        clan_tag = input("Clan tag: ")
        rr = Recruiter(name, clan_tag)
        #SET REQUIREMENTS FOR CLAN FOR RECRUITER
        th_req = input("Enter Townhall requirement: ")
        league_req = input("Enter League requirement number: ")
        rr.set_requirements(int(th_req), int(league_req))
        #INITIALIZE RECRUITEE
        name = input("Recruitee, Please enter your name: ")
        user_tag = input("Recruitee, Please enter your user tag: #")
        api = input("Recruitee, Please enter your API token: ")
        re = API(user_tag, api)
        re.check_player_api()
        #print(re.storage)


            
        
get_user()
#jon was here
#arkaaz was here
#testing for jon


