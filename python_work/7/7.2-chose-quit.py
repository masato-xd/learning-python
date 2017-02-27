prompt = '\nTell me something, and I will repeat it back to you:'
prompt += "\nEnter 'quit' when you are finished.\n"
message = ""

while message != 'quit':
    message = raw_input(prompt)
    if message != 'quit':
        print(message)
