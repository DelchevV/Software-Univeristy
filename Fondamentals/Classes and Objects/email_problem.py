class Email:
    def __init__(self, sender, receiver, contents):
        self.sender=sender
        self.receiver=receiver
        self.contents=contents
        self.is_sent=False

    def send(self):
        self.is_sent=True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.contents}. " \
               f"Sent: {self.is_sent}"


emails=[]
while True:
    data=input().split()
    if data[0]=="Stop":
        break
    send=data[0]
    receive=data[1]
    content=data[2]
    email=Email(send,receive,content)
    emails.append(email)

send_emails=list(map(int, input().split(", ")))
for x in send_emails:
    emails[x].send()
for email in emails:
    print(email.get_info())