users=open('Entra ID/Users.txt','r')
for user in users.readlines():
    print(user)
    endpoint = "https://graph.microsoft.com/v1.0//users/"
    endpoint += str(user)
    endpoint += "/revokeSignInSessions"
    print (endpoint)