import os
import pickle
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import base64

class GoogleServices:
    SCOPES = [
        "https://www.googleapis.com/auth/gmail.modify",
        "https://www.googleapis.com/auth/gmail.send",
    ]

    def __init__(self) -> None:
        self.creds = self.authenticate()
        
        self.service = self.get_gmail_service()

    def authenticate(self):
        creds = None
        
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                print("credentials loaded")
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                print("verification initiated")
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', 
                    self.SCOPES
                )
                creds = flow.run_local_server(port=0)

            with open('token.pickle', 'wb') as token:
                print("credentials saved")
                pickle.dump(creds, token)

        return creds

    def get_gmail_service(self):
        try:
            service = build('gmail', 'v1', credentials=self.creds)
            return service
        except HttpError as error:
            print(f'An error occurred: {error}')
            return None

    def send_email(self, to, subject, body):
        print(f"to: {to}   subject: {subject}   body: {body}")
        try:
            message = MIMEMultipart()
            message['to'] = to
            message['subject'] = subject
            message.attach(MIMEText(body, 'plain'))

            raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

            message = self.service.users().messages().send(userId='me', body={'raw': raw_message}).execute()
            print(f'Sent message to {to} Message Id: {message["id"]}')
            
            return True, None

        except HttpError as error:
            print(f'An error occurred: {error}')
            
            return False, error