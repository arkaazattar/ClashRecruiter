import requests

headers = {

    "Content-Type" : "application/json",
    "Authorization" :"Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImRlYTUzNWVhLTljYTAtNDFmMC04MDJlLWIzZjk4YzAyMmMxNCIsImlhdCI6MTc2MjY0NzgxMSwic3ViIjoiZGV2ZWxvcGVyLzI4NjU3YTI4LTk5NWQtYmY3YS05NzRlLWEwNDViMWU2YzEzNyIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjE0Mi4xOTguMTAzLjE0NiIsIjE0Mi4xMjYuMTgwLjE2NiJdLCJ0eXBlIjoiY2xpZW50In1dfQ.3k8c1cIEQgKpyrdKhTBtuTidotVPGTKGg4G-fRbNEvef4TxqvFAQmvIpHBjm2gvko8Sb3iRBFbZCVVw2Y_cpeA" 
}

class Advertisement:

    def __init__(self, requirements, Recruiter):
        self.requirements = requirements

    
class Recruiter:
    requirements = []

    def __init__(self, name, clan_tag):
        self.name = name
        self.clan_tag = clan_tag

    def print_info(self):
        print(self.name + " " + self.clan_tag)

    def get_clan_info(self):

        #GET API INFO
        response = requests.get(
            'https://api.clashofclans.com/v1/clans/%23'+self.clan_tag, headers = headers)
        #Store api info
        self.storage = response.json()
        #print(self.storage)

    def post_ad(self):
        print(self.requirements)

    def set_requirements(self, th_level, League):

        self.requirements = [th_level, League]

    def get_requirements(self):
        return self.requirements


class Recruitee:

        def __init__(self, name, user_tag, api):
            self.name = name
            self.user_tag = user_tag
            self.json_data = {
                "token": str(api)
            }
            #api is one time use, no point of storing it 
        def get_stats(self):
            #logic might be broken
            url = f"https://api.clashofclans.com/v1/players/%23{self.user_tag}/verifytoken"

            response = requests.post(url, headers=headers, json = self.json_data)
            self.storage = response.json()
            #try: 
            #    self.storage['reason'] == 'notFound'
            #    print("User doesn't exist!")
            #except:
            #    for key in self.storage:
            #        if key == "leagueTier":
            #            league = self.storage[key]["name"]
                        #Get the int of the league that recruitee is in
            #            y=""
            #            for ch in league:
            #                if ch.isdigit():
            #                    y += ch 
            #        elif key == "townHallLevel":
            #            th_level = self.storage[key]
                    
                        
            # print(th_level, league)
            #stats = [th_level, int(y)]    
            return
        
        def apply(self, Recruiter):
            stats = self.get_stats()
            eligibility = True
            for i in range(2):

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
        else: print("Invalid input")
    
    if recruiting == 'yes': #need to implement calling of other functtions
        invalid_clan = True
        while invalid_clan:
            name = input("Enter Name: ")
            clan_tag = input("Enter Clan Tag: ")
            if clan_tag[0] == '#':
                clan_tag = clan_tag[1:]
            clan = Recruiter(name, clan_tag)
            clan.get_clan_info()
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
        api = input("Recruitee, Please enter your API token")
        re = Recruitee(name, user_tag, api)
        re.get_stats()
        print(re.storage)

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
