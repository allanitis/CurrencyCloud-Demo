from cc_auth import Auth

def handler(event, context):
    a = Auth.get_auth_token()
    print(a)

    return {"message": "Successfully executed"}
