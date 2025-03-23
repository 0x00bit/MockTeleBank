import requests


class Bot():
    def __init__(self):
        self.TOKEN = ""
        URL_BASE = f"https://api.telegram.org/bot{self.TOKEN}"
        self.getUpdateURL = f"{URL_BASE}/getUpdates"
        self.sendMessageURL = f"{URL_BASE}/sendMessage"
        self.lastmsgid = None

    def GetMessages(self):
        """This function checks for updates in the chat"""
        try:
            responseApi = requests.get(self.getUpdateURL)  # Getting update
            if responseApi.status_code != 200:
                print("An error occurred during the request!")
                return None, None

            returnJson = responseApi.json()
            if not returnJson['result']:
                return None, None

            last_message = returnJson['result'][-1]
            idmsg = last_message['message']['message_id']

            if self.lastmsgid is not None and idmsg <= self.lastmsgid:
                return None, None

            self.lastmsgid = idmsg  # Updating the last message
            command = last_message['message']['text']  # The command given by the user
            idchat = last_message['message']['chat']['id']  # The id of the chat

            return command, idchat

        except Exception as err:
            print("An error occurred during the update: {err}")
            return None, None

    def sendMessages(self, idchat, text):
        """This function sends a message to the telegram chat"""
        dictData = {'chat_id': idchat, 'text': text}

        try:
            requestSend = requests.post(self.sendMessageURL, data=dictData)
            if requestSend != 200:
                print(f"An error occurred, message: {text} not sent")

        except Exception as err:
            print("Error in: {text}, error: {err}")
