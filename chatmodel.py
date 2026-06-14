from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)
    
    #temperature=0.9,
    #temperature is a parameter that controls the randomness of the generated text. Higher values (e.g., 1.5) will produce more random and creative responses, while lower values (e.g., 0.2) will produce more focused and deterministic responses.
    #max_new_tokens=30
    #max_new_tokens is a parameter that limits the maximum number of tokens in the generated response. Setting it to 30 means that the model will generate a response with at most 30 tokens, which can help control the length of the output and prevent excessively long responses.  


chat = ChatGoogleGenerativeAI(llm=llm)
#a=input("ask me anything: ")
#response = chat.invoke(a)

chat_history = [SystemMessage(content="You are a helpful assistant.")]
while True:
    user = input("you:")
    chat_history.append(HumanMessage(content=user))
    if user == "exit":
        print("exiting...")
        break
    response = chat.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("ai:", response.content)
  
