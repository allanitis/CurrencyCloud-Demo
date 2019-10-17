from botocore.vendored import requests
from botocore.vendored import requests

def handler(event, context):
    try:
        res = requests.post(
            "http://localhost/tokenise",
            params={},
            headers={"Accept":"","Content-Type":"applications/json"},
            data='plainText'
        )
        # your code goes here
    except BaseException as e:
        # error handling goes here
        raise(e)
        try:
            res = requests.post(
                "http://localhost/detokenise",
                params={},
                headers={"Accept":"","Content-Type":""},
                data=''
            )
            # your code goes here
        except BaseException as e:
            # error handling goes here
            raise(e)
    

    
    return {"message": "Successfully executed"}
