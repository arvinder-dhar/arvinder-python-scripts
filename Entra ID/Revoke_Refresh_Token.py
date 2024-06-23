'''
KB Articles

https://learn.microsoft.com/en-us/python/api/azure-identity/azure.identity.usernamepasswordcredential?view=azure-python
https://github.com/AzureAD/microsoft-authentication-library-for-python/blob/1.22.0/sample/username_password_sample.py
https://www.w3schools.com/python/ref_string_replace.asp
https://www.geeksforgeeks.org/how-to-convert-pythons-isoformat-string-back-into-datetime-object/
https://stackoverflow.com/questions/35351876/calculate-time-span-in-python
https://www.geeksforgeeks.org/how-to-send-beautiful-emails-in-python/
https://learn.microsoft.com/en-us/graph/api/user-revokesigninsessions?view=graph-rest-1.0&tabs=python

'''

##### Start #####

## Import Modules
import requests
from msal import PublicClientApplication
import json
#from datetime import datetime, timezone
#from email.message import EmailMessage
#import smtplib
import sys

## Variables

tenant = sys.argv[1]
authority = """https://login.microsoftonline.com/""" + str(tenant) + """ """
clientid = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
scope = ['https://graph.microsoft.com/.default']

app = PublicClientApplication(client_id=clientid, authority=authority)
result = app.acquire_token_by_username_password(username, password, scope)

if "access_token" in result:
    ## Get Users from the text File
    users=open('Entra ID/Users.txt','r')
    for user in users.readlines():
        print (user)
        #endpoint = "https://graph.microsoft.com/v1.0//users/"
        #endpoint += str(user)
        #endpoint += "/revokeSignInSessions"
        #endpoint = endpoint.rstrip()
        #print (endpoint)
        endpoint = "https://graph.microsoft.com/v1.0//users/chalawh@arvindruchi.onmicrosoft.com/revokeSignInSessions"
        graph_data = requests.post(
            endpoint,
            headers={'Authorization': 'Bearer ' + result['access_token']},).json()

'''
# Send Email if the Sync is more than 2 hours
    if int(time_span_minutes) > 120:
        print("AAD Sync Delayed, please check manually")
        msg = EmailMessage()
        msg["Subject"] = "PROD : AAD Sync Delay (Python)"
        msg["From"] = "something@something.com"
        msg["To"] = "something@something.com"

        msg.set_content("""<html>
        <font
            color=Red><font size='+2'><b>ALERT : Last AAD Export Sync Duration > 2 Hrs.</b><br>
            <font
            color=Black size='+1.5'><b>Please check the run cycles and confirm they are running correctly </b>
            <ul><li>
            <b>Primary Sync Server:</b> Graph Limitation</li>
            <li><b>LastDirsync Time(UTC):</b> """ + str(last_sync_unformatted) + """ </li>
            </ul>
            <p class=MsoNormal align=center style='text-align:left'><span
        style='font-family:'Arial',sans-serif'><img width=190 height=63 id='_x0000_i1025'
        src='https://imageURL.png'
        style='height:1in;width:4.5in' alt=Image><o:p></o:p></span></p>
            </html>""", subtype='html')

        server = smtplib.SMTP('smtpdata.com')
        server.send_message(msg)
'''
##### End #####
