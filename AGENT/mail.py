from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent


@tool
def save_notes( title:str, what:str, where:str, when:str, action:str, sender:str, priority:str ) -> str:
    ''' Save the important information form the given E-mail '''

    print("\n========== NOTES ==========")
    print("Title: ",title)
    print("What: ",what)
    print("When: ",when)
    print("Where: ",where)
    print("Action: ",action)
    print("Sender: ",sender)
    print("Priority: ",priority)
    print("===========================\n")


    return "Note save successfully"


@tool
def write_email( to:str, subject:str, body:str) ->str:
    '''Act as an professional and write an email '''

    print("\n========== EMAIL ==========")
    print("To: ",to)
    print("Subject",subject)
    print("Body: ",body)
    print("===========================\n")

    return "Email created successfully"


tools = [save_notes,write_email]


model = ChatOllama(
    model = 'llama3.1',
    temperature = 0
)


agent = create_agent(model,
                    tools,
                    )


while True:

    print("You can write an mail or covert the mail into key notes")

    user_input = input("you: ")

    if user_input.lower() == 'break':
        break

    response1 = agent.invoke({
        "messages":[

            ("user",{user_input})

        ]
    })
    print(f"\nBot:\n{response1['messages'][-1].content}\n") 