from bot import Bot
from client import Client
from database import Database


class Server():
    def __init__(self):
        self.bot = Bot()
        self.database = Database('bank_db', 'clients')

        self.server_commands = {"/?": self.helpCommand,
                                "/help": self.helpCommand,
                                "/start": self.helpCommand,
                                }

        self.client_commands = [
            "/createclient",
            "/checkbalance",
            "/deposit",
            "/withdraw"
            ]

        self.special_characters = """!@#$%^&*()-+?_=,<>/\"\' """  # sanatization

    def helpCommand(self, chatid):
        """This function is the /help of the telegram bot"""

        text = "Welcome to CN bank, here is a list of valid commands:"
        text += "\n /help, /?, /start: For help"
        text += "\n /createclient <username> <name>: Create a new client"
        text += "\n /checkbalance <username>: Check the balance of a client"
        text += "\n /deposit <username> <amount>: Deposit money into a client's account"
        text += "\n /withdraw <username> <amount>: Withdraw money from a client's account"


        self.bot.sendMessages(chatid, text)

    def validadeCreateUser(self, command):
        """Validade the command and the format"""

        if " " in command:
            parts = command.split(" ")
            if len(parts) == 3 and parts[2] not in self.special_characters:
                return parts[0]

        return None

    def runServer(self):
        """Runs the server and gets the commands from the bot"""

        try:
            while True:
                command, chatid = self.bot.GetMessages()
                # If the command is invalid then:
                if not command or not chatid:
                    continue  # Restart the cycle until to get a new msg

                print(f"Received command: {command} from chat {chatid}")
                # If it's a help command then
                if command in self.server_commands.keys():
                    self.server_commands[command](chatid)  # Print the help
                    continue
                
                # If the command is in the client list's commands then:
                if command.startswith("/createuser"):
        
                    try:
                        _, username, name = command.split(" ")
                        result = self.database.createClient(username, name)
                        self.bot.sendMessages(chatid, self.database.getClient(username))
                        print(result)
                    except Exception as err:
                        print(f"An error occurred: {err}")

                if command.startswith("/createclient"):
                    try:
                        _, username, name = command.split(" ")
                        result = self.database.createClient(username, name)
                        if result:
                            self.bot.sendMessages(chatid, f"Client '{username}' created successfully!")
                        else:
                            self.bot.sendMessages(chatid, "Failed to create client.")
                    except Exception as err:
                        self.bot.sendMessages(chatid, f"Error creating client: {err}")

                elif command.startswith("/checkbalance"):
                    try:
                        _, username = command.split(" ")
                        client_data = self.database.getClient(username)
                        if client_data:
                            client = Client(
                                userid=client_data['userid'],
                                name=client_data['name'],
                                balance=client_data['balance'],
                                last_deposit=client_data['last_deposit'],
                                last_withdraw=client_data['last_withdraw']
                            )
                            client.check_balance()
                            self.bot.sendMessages(chatid, f"Balance for '{username}': ${client.balance}")
                        else:
                            self.bot.sendMessages(chatid, f"Client '{username}' not found.")
                    except Exception as err:
                        self.bot.sendMessages(chatid, f"Error checking balance: {err}")

                elif command.startswith("/deposit"):
                    try:
                        _, username, amount = command.split(" ")
                        amount = float(amount)
                        client_data = self.database.getClient(username)
                        if client_data:
                            client = Client(
                                userid=client_data['userid'],
                                name=client_data['name'],
                                balance=client_data['balance'],
                                last_deposit=client_data['last_deposit'],
                                last_withdraw=client_data['last_withdraw']
                            )
                            client.deposit(amount)
                            self.database.updateClient(username, {
                                'balance': client.balance,
                                'last_deposit': client.last_deposit,
                                'transaction_historic': client.transaction_history
                            })
                            self.bot.sendMessages(chatid, f"Deposited ${amount} to '{username}'. New balance: ${client.balance}")
                        else:
                            self.bot.sendMessages(chatid, f"Client '{username}' not found.")
                    except Exception as err:
                        self.bot.sendMessages(chatid, f"Error depositing money: {err}")

                elif command.startswith("/withdraw"):
                    try:
                        _, username, amount = command.split(" ")
                        amount = float(amount)
                        client_data = self.database.getClient(username)
                        if client_data:
                            client = Client(
                                userid=client_data['userid'],
                                name=client_data['name'],
                                balance=client_data['balance'],
                                last_deposit=client_data['last_deposit'],
                                last_withdraw=client_data['last_withdraw']
                            )
                            if client.withdraw(amount):
                                self.database.updateClient(username, {
                                    'balance': client.balance,
                                    'last_withdraw': client.last_withdraw,
                                    'transaction_historic': client.transaction_history
                                })
                                self.bot.sendMessages(chatid, f"Withdrew ${amount} from '{username}'. New balance: ${client.balance}")
                            else:
                                self.bot.sendMessages(chatid, "Insufficient balance or invalid amount.")
                        else:
                            self.bot.sendMessages(chatid, f"Client '{username}' not found.")
                    except Exception as err:
                        self.bot.sendMessages(chatid, f"Error withdrawing money: {err}")

                else:
                    self.bot.sendMessages(chatid, "Invalid command. Use /help for a list of commands.")

        except Exception as err:
            print(f"An error occurred: {err}")



server = Server()
server.runServer()
