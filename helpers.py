global json_file
json_file = "/etc/pandora/accounts.json" # this is supposrd to be users jason adress

def new_account():
    # if we are talking about a json file 
    # for now it does not take a parameter 
    from datetime import datetime
    import json
    with open(json_file, "r+") as jf:
        data = json.load(jf) # loading json file

        accounts = data['accounts'] 
        for account in accounts:
            if not account["start_time"]:
                today = datetime.now().isoformat()
                account["start_time"] = today
                jf.seek(0) # moving the pointer to frist 
                json.dump(data, jf, indent=4) # setting the whole file to the cahnged data
                jf.truncate()
                return account["uuid"], account
    raise Exception("no free accounts left")


if __name__ == "__main__":
    print(new_account())
    """note that line 24 also changes the json file so the second time you run it there is no
    starting time so there will be NONE"""