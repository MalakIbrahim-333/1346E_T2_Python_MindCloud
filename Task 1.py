# Chat Bot

# Base knowledge stored in a dictionary
knowledge_base = {
    "hello": "Hi there! Glad you’re here. What’s your name?",
    "how are you?": "I’m doing fine, thanks for asking. How’s your day going?",
    "thank you": "You’re most welcome!",
    "bye": "Alright, take care and stay safe."
}

# List to keep track of conversation history
conversation_history = []

# Variable to store the user's name
user_name = None

print("Hello! I’m here to chat, help, and keep you company. Type 'bye' whenever you’d like to leave.")
conversation_history.append("Bot: Hello! I’m here to chat, help, and keep you company. Type 'bye' whenever you’d like to leave.")

while True:
    user_input = input("You: ").strip().lower()
    conversation_history.append(f"You: {user_input}")

    # Exit condition
    if user_input == "bye":
        bot_reply = f"Goodbye {user_name if user_name else ''}. take care and stay safe.."
        print(bot_reply)
        conversation_history.append(f"Bot: {bot_reply}")
        break

    # If the chatbot doesn't know the user's name yet
    if user_name is None and user_input not in knowledge_base:
        user_name = user_input.title()
        bot_reply = f"It’s really nice to meet you, {user_name}. How can I help you today?"
        print(bot_reply)
        conversation_history.append(f"Bot: {bot_reply}")
        continue

    # Math operations
    try:
        if "+" in user_input:
            nums = user_input.split("+")
            total = int(nums[0]) + int(nums[1])
            bot_reply = f"That comes to {total}."
            print(bot_reply)
            conversation_history.append(f"Bot: {bot_reply}")
            continue

        elif "-" in user_input:
            nums = user_input.split("-")
            result = int(nums[0]) - int(nums[1])
            bot_reply = f"That works out to {result}."
            print(bot_reply)
            conversation_history.append(f"Bot: {bot_reply}")
            continue

        elif "*" in user_input:
            nums = user_input.split("*")
            product = int(nums[0]) * int(nums[1])
            bot_reply = f"The answer is {product}."
            print(bot_reply)
            conversation_history.append(f"Bot: {bot_reply}")
            continue

        elif "/" in user_input:
            nums = user_input.split("/")
            if int(nums[1]) == 0:
                bot_reply = "Division by zero isn’t possible, but we can work through another calculation if you’d like."
            else:
                quotient = int(nums[0]) / int(nums[1])
                bot_reply = f"That gives {quotient}."
            print(bot_reply)
            conversation_history.append(f"Bot: {bot_reply}")
            continue
    except ValueError:
        bot_reply = "I think there was a little mix-up with the numbers. Could you try again?"
        print(bot_reply)
        conversation_history.append(f"Bot: {bot_reply}")
        continue

    # If the message is in the knowledge base
    if user_input in knowledge_base:
        bot_reply = knowledge_base[user_input]
        print(bot_reply)
        conversation_history.append(f"Bot: {bot_reply}")
    else:
        # Handles any questions that are not stored in its base data.
        bot_reply = "I may not have an exact answer for that, but I’m here to listen and help however I can."
        print(bot_reply)
        conversation_history.append(f"Bot: {bot_reply}")

# Show conversation history at the end
print("\nOur chat history:")
for line in conversation_history:
    print(line)