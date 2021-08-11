# # chatbot class
# class Chatbot:
#     def sayHello(self):
#         print("say hello")

#     def sayMyName(self):
#         print("My name is JeremyBot :D")

# # chatbot instance making
# chatbot = Chatbot()
# chatbot.sayHello()
# chatbot.sayMyName()

class SimpleObj:
    def __init__(self):
        print('call __init__()')

    def __del__(self):
        print('call __del__()')

obj = SimpleObj()
print('obj instance is alive...')
del obj