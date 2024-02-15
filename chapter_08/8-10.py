# Copy of 8-9: 
def send_messages(text_messages, sent_messages):
    """Print each message and move to sent messages"""
    while text_messages:
        current_message = text_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

def show_sent_messages(sent_messages):
    """Display sent messages and messages to be sent. """
    print("The following messages have been sent:")
    for sent_message in sent_messages:
        print(f"{sent_message}")
    
    print("The following messages need to be sent (should be blank):")
    for text_message in text_messages:
        print(f"{text_message}")

text_messages = ['lmao', 'kk', 'wtf should I write', "I don't feel creative"]
sent_messages = []

send_messages(text_messages, sent_messages)
show_sent_messages(sent_messages)