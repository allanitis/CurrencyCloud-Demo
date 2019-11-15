from botocore.vendored import requests
from botocore.vendored import requests

def handler(event, context):
    
    try:
        res = requests.post(
            "https://devapi.currencycloud.com/v2/conversions/create",
            params={},
            headers={"X-Auth-Token":auth,"Accept":"application/json","Content-Type":"application/x-www-form-urlencoded"},
            data="buy_currency=USD&sell_currency=EUR&fixed_side=buy&amount=2300.00&term_agreement=true"
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        raise(e)
    return {"message": "Successfully executed"}
        try:
            res = requests.get(
                "http://api.yapily.com/jwks",
                params={},
                headers={"Accept":"application/json;charset=UTF-8"}
            )
            # your code goes here
        except BaseException as e:
            # error handling goes here
            raise(e)


