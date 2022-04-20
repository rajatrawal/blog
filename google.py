from google_auth_oauthlib.flow import  InstalledAppFlow
from googleapiclient.discovery import build
import pickle


scopes = ['https://www.googleapis.com/auth/calendar']
flow = InstalledAppFlow.from_client_secrets_file('client.json',scopes=scopes)
# credentials = flow.run_console()
credentials = flow.run_local_server()

print(credentials)
# credentials = flow.fetch_token('')
# # credentials = '4/1AX4XfWg9EPp8rVRypHTxkhQij54Qh8jBLTAiQk6a7leslJzbTHT3bEHCAjQ'
# # pickle.dump(credentials,open('tocken.pkl','wb'))
# credentials = pickle.load(open('tocken.pkl','rb'))
# service = build('calendar','v3',credentials=credentials)
# result = service.calendarList().list().execute()
# calendar_id =result['items'][0]['id']
# result = service.events().list(calendarId = calendar_id).execute()
# print(result['items'][0])