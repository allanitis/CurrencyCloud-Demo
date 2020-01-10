import requests
import json

class Auth:
    def get_auth_token():
        id = "matt@fintechsandpit.com"
        user = ""
        try:
            print("trying to request")
            res = requests.post(
                "https://devapi.currencycloud.com/v2/authenticate/api",
                params={},
                headers={"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
                data="login_id={}&api_key={}".format(id, user)
            )
            auth_token = json.loads(res.text)["auth_token"]
        except BaseException as e:
            print(e)
            print('exception found')
            raise(e)
        
        return {"message": "Successfully executed", "auth_token": auth_token}

