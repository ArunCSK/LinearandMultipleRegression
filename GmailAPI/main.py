from __future__ import print_function
import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

#from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
#SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
import auth
SCOPES = 'https://mail.google.com/'
CLIENT_SECRET_FILE = 'D:\Arundev\py\GmailAPI\credentials.json'
APPLICATION_NAME = 'Gmail API Python Quickstart'
authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
credentials = authInst.get_credentials()

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('D:\Arundev\py\GmailAPI\credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])

    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'])

    http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', http=http)

    import sendmail

    sendInst = sendmail.send_email(service)
    message = sendInst.create_message_with_attachment('arunsubburaj@gmail.com','arunsubburaj@gmail.com','Testing 123','Hi there, This is a test from Python!','D:\Arundev\py\GmailAPI\credentials.json')
    sendInst.send_message('me',message)

    

if __name__ == '__main__':
    main()    