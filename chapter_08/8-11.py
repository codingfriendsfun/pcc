#working from 8-10 code

#function that prints messages stored in a list
def show_messages(messages):
    """Prints messages stored in a list."""
    for message in messages:
        print(message)

#moves unsent messages to sent
def send_messages(unsent_messages, sent_messages):
    """Displays an unsent message and moves it to sent messages."""
    while unsent_messages:
        sending_message = unsent_messages.pop()
        print(sending_message)
        sent_messages.append(sending_message)

#list of sent and unsent messages
unsent_messages = [
    'I am a text message in this program', 
    'How are you today, text message?',
    'Hi text message, it is warm today.']
sent_messages = []

#verify messages are in unsent_messages and sent_messages is empty
print(unsent_messages)
print(sent_messages)

#pass copy of unsent_messages to keep values
send_messages(unsent_messages[:], sent_messages)

#verify unsent_messages hasn't had values removed
print(unsent_messages)
print(sent_messages)