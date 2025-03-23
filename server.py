from bot import Bot


class Server():
    def __init__(self):
        self.bot = Bot()

        self.server_commands = {"/?": self.helpCommand,
                                "/help": self.helpCommand,
                                "/start": self.helpCommand,
                                }

        self.client_commands = {"/checkbalance": print("not implemented yet"),
            "/deposit": print("not implemented yet"),
            "/withdraw": print("not implemented yet")
            }

        self.special_characters = """!@#$%^&*()-+?_=,<>/\"\'"""  # sanatization

    def helpCommand(self, chatid):
        """This function is the /help of the telegram bot"""

        text = "Welcome to my bot, here is a list of valid commands:"
        text += "\n /help, /?, /start: For help"
        text += "\n /withdraw"

        self.bot.sendMessages(chatid, text)

    def validadeCommand(self, command):
        """Validade the command and the format"""

        if ":" in command:
            parts = command.split(":", 1)
            if len(parts) == 2 and parts[1] not in self.special_characters:
                return parts[1]

        return None

    def runServer(self):
        """Runs the server and gets the commands from the bot"""

        try:
            while True:
                command, chatid = self.bot.GetMessages()
                if not command or not chatid:
                    continue  # Restart the cycle until to get a new msg

                print(f"Received command: {command} from chat {chatid}")

                if command in self.server_commands.keys():
                    self.server_commands[command](chatid)
                    continue
        except Exception as err:
            print(f"An error occurred: {err}")


server = Server()
server.runServer()
