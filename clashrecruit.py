import requests

headers = {

    "Content-Type" : "application/json",
    "Authorization" :"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRlYTUzNWVhLTljYTAtNDFmMC04MDJlLWIzZjk4YzAyMmMxNCIsImlhdCI6MTc2MjY0NzgxMSwic3ViIjoiZGV2ZWxvcGVyLzI4NjU3YTI4LTk5NWQtYmY3YS05NzRlLWEwNDViMWU2YzEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0Mi4xOTguMTAzLjE0NiIsIjE0Mi4xMjYuMTgwLjE2NiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.3k8c1cIEQgKpyrdKhTBtuTidotVPGTKGg4G-fRbNEvef4TxqvFAQmvIpHBjm2gvko8Sb3iRBFbZCVVw2Y_cpeA" 
}

class API:
    def __init__(self, user_tag, api):
        self.user_tag = ""
        self.token = False
        self.reason = 0
        self.json_data = {
            "token": str(api)
        }
        #api is one time use, no point of storing it 
    def check_player_api(self):
        #logic might be broken
        url = f"https://api.clashofclans.com/v1/players/%23{self.user_tag}/verifytoken"

        response = requests.post(url, headers=headers, json = self.json_data)
        self.storage = response.json() # Important!! this storage now holds whether the api key is valid or not

        if self.storage.get("reason") == "notFound":
            self.reason = "Player tag is incorrect" 

        elif self.storage.get("status") == "invalid":
            self.reason = "API Token is incorrect"

        elif self.storage.get("status") == "ok":
            self.token = True # set token value to 1 in boolean. this makes it easy to check if token info is correct

        else: self.reason = self.storage  

        return self.token #dont really need to store token in class, as its being returned anyways. keeping for now in the case that we need it for error checking.

class Advertisement:

    def __init__(self, requirements, Recruiter):
        self.requirements = requirements

    
class Recruiter:
    
    requirements = []

    def __init__(self, user_tag, clan_tag):
        self.user_tag = user_tag
        self.clan_tag = clan_tag

    def print_info(self): # idk why we would need this 
        print(self.user_tag + " " + self.clan_tag)

    def check_if_leader(self):
        roles = ["coLeader", "Elder"]
        is_leader =  False
        #GET API INFO
        response = requests.get(
            f"https://api.clashofclans.com/v1/clans/%23{self.clan_tag}")
        #Store api info
        self.storage = response.json()
        #print(self.storage)
        large_list = self.storage.get("items")
        print(large_list)
        for i in large_list:
            if large_list[i].get("tag") == self.user_tag:
                if large_list[i].get("role") in roles:
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

        def apply(self, Recruiter):
            stats = self.get_stats()
            eligibility = True
            for i in range(2):

                # this is for sure broken    
                if stats[i-1] >= Recruiter.get_requirements()[i-1]:
                    continue
                else:
                    eligibility = False

            if eligibility == True:
                print("Applied")    

            else:
                print("not eligible")

                
def get_user():
    # list of all league names, lowest to highest - prob not needed
    league_list = ["Skeleton", "Barbarian", "Archer", "Wizard", "Valkyrie", "Witch", "Golem", "P.E.K.K.A", "Titan", "Dragon", "Electro", "Legend"]
    
    invalid_input = True
    while invalid_input:
        recruiting = input("Are you recuiting? Yes or no: ").lower()
        if recruiting == "yes" or  recruiting == "no" or recruiting == 'test':
            invalid_input = False
            
            # get user api regardless of whether they are looking for clan or not
            valid_api = False
            while  valid_api == False:
                user_tag = input("Please enter your player tag: ")
                api = input("Please enter your API token: ")
                user = API(user_tag, api)
                user.check_player_api()
                if user.token == True:
                    valid_api = True
                else: print(f"{user.reason}, try again") 
        else: print("Invalid input")
    
    # will not reach here unelss the api key is valid

    if recruiting == 'yes': #need to implement calling of other functtions
        invalid_clan = True
        while invalid_clan:
            clan_tag = input("Enter Clan Tag: ")
            if clan_tag[0] == '#':
                clan_tag = clan_tag[1:]
            clan = Recruiter(user_tag, clan_tag)
            clan.check_if_leader()
            print(clan.storage)

            if clan.storage.get('reason') == 'notFound':
                print("Clan not found, try again.")
            else:
                invalid_clan = False
        print("Exited loop, clan is real")

    
    elif recruiting == 'no' : # case that they are looking for a clan
        invalid_input = True
        while invalid_input:
            looking_for_clan = input("Are you looking for a clan? Yes or no: ").lower()
            if looking_for_clan == "yes" or  looking_for_clan == "no":
                invalid_input = False
            else: print("Invalid input")

        # this is now broken
        if looking_for_clan == 'yes':
            lfc = Recruitee(name, user_tag)
            lfc.name = input("Enter your ")

        if looking_for_clan == "no":
            return(print("Thank you for trying our app."))
        


#TESTING OBJECTS HERE !! !! !!
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

       # re.apply(rr)

    elif recruiting == "Yes":
        name = input("Name: ")
        
        get_inputs = True
        while get_inputs:
            
            clan_tag = input("Clan tag: ")


        user_test = Recruiter(name, clan_tag)
        user_test.print_info()
        # user_test.get_clan_info()


    #elif recruiting == "No":
    #    name = input("Please enter your name: ")
    #    user_tag = input("Please enter your user tag: #")
#
 #       rt = Recruitee(name, user_tag)
#
 #       rt.get_stats()
    else:
        acpt_input = True
        while acpt_input:
            user_tag = input("Please enter your user tag: #")
            response = requests.get(
                'https://api.clashofclans.com/v1/players/%23'+user_tag, headers = headers)
            storage = response.json()
        
            print(storage)
        
            try: 
                storage['reason'] == 'notFound'
                print("User doesn't exist!")
            except:
                for key in storage:
                    if key == "leagueTier":
                        league = storage[key]["name"]
                        print(league)
                        acpt_input = False
            
        
get_user()
#jon was here
#arkaaz was here
#testing for jon


