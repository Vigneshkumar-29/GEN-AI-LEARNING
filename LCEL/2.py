from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama

model = ChatOllama(
    model="qwen2.5:0.5b",
    temperature = 0,
    num_predict=50,
)

parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ('system','you are an helpful assistant'),
    ('human','{history}')
])
chain = prompt | model | parser

store = {}

def get_session_history(session_id):
    if session_id not in store:
        store[session_id] = []
    return store[session_id]

current_session_id = 1

while True:
    user_input = input("you: ")

    if user_input.lower() == 'exit':
        break
    try:
        history = get_session_history(current_session_id)
        history.append({'user_input':user_input})
        response = chain.invoke({'history':history})
        print(f'''
        user input => {user_input}
        response => {response}'''
        )
        history.append(response)
        store[current_session_id]=history
    except Exception as e:
        print(f'error => {e}')
        break

    new_session_id = input('''
                        if you want to continue with same session type anything except 'no' 
                        for new session type 'NO' ''').lower()

    if new_session_id == 'no':
        current_session_id+=1


'''
                 START
                   ↓
              while True
                   ↓
            Get user input
                   ↓
            Is it "exit"?
             /          \
           YES           NO
            ↓             ↓
          STOP          try
                          ↓
                 Get session history
                          ↓
                  Add user question
                          ↓
                    Invoke chain
                          ↓
                    Get LLM response
                          ↓
                     Print response
                          ↓
                 Add response to history
                          ↓
                 Save history to store
                          ↓
                    Any error?
                   /          \
                 YES           NO
                  ↓             ↓
                except      Ask session?
                  ↓             ↓
                STOP       Same session
                              OR
                          New session
                              ↓
                         while True
'''