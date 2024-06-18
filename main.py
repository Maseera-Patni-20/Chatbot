import google.generativeai as ai

#API KEY
API_KEY='AIzaSyBfEub76JhiytoLGhEAd5EP8z9Df7hMtuI'

#Configure the API
ai.configure(api_key=API_KEY)

#Create a new model
model=ai.GenerativeModel("gemini-pro")
chat=model.start_chat()

#Start a conversion
while True:
    message=input('You: ')
    if message.lower()=='bye':
        print('Chatbot:Goodbye!')
        break
    response=chat.send_message(message)
    print('Chatbot',response.text)