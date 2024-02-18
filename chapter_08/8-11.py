# 8-11. Archived Messages

messages = [
    "On my way!",
    "Running a bit late.",
    "Do you believe in love after love?"
]

sent_messages = []

def show_messages(message_list):
    for message in message_list:
        print(message)

def send_messages(message_list):
    while message_list:
        popped_message = message_list.pop()
        print(popped_message)
        sent_messages.append(popped_message)

send_messages(messages[:])

print(messages)
print(sent_messages)