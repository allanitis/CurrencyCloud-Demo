import requests
from cc_auth_1 import Auth

def handler(event, context):
    auth_token = Auth.get_auth_token()["auth_token"]
    print(auth_token)
    try:
        res = requests.post(
            "https://devapi.currencycloud.com/v2/conversions/create",
            params={},
            headers={"X-Auth-Token":auth_token,"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
            data="buy_currency=USD&sell_currency=EUR&fixed_side=buy&amount=1000&term_agreement=true"
        )
        print(res.text)
    except BaseException as e:
        # error handling goes here
        raise(e)

    return {"message": "Successfully executed"}

