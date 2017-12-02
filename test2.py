def parse_code(parse_token):
    ind = parse_token.index("access_token")
    parsed = parse_token.split("&")[0][ind+13:]
    response =  requests.get("https://simulator-api.db.com/gw/dbapi/v1/ageCertificate?certificationMethod=LEGAL_AGE", headers = {"Authorization":"Bearer "+parsed})
    if(response.ok):
        bracket =  str(response.content).index("}")
    if(str(response.content)[15:bracket] == 'true'):
        return True
    elif(str(response.content)[15:bracket] == 'false'):
        return False
    else:
        print("connection broken")