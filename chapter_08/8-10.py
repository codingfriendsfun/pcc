# Define a list of short text messages
messages = ["Hello, how are you?", "Good morning!", "Have a great day!", "See you soon!"]
sent_messages = []

# Function to send messages and move them to sent_messages list
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

# Call the function to send messages
send_messages(messages, sent_messages)

# Print both lists to confirm messages were moved
print("\nMessages list:", messages)
print("Sent messages list:", sent_messages)
