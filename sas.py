import random
import string

def generate_conversation_name(length=8):
    characters = string.ascii_letters + string.digits
    name = ''.join(random.choice(characters) for _ in range(length))
    return name

# Generate a random conversation name
conversation_name = generate_conversation_name()
print("Generated Conversation Name:", conversation_name)
