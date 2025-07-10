import asyncio
from dotenv import load_dotenv
load_dotenv()

from langchain_mistralai import ChatMistralAI
from chat import ChatLangchain
from browser_use import Agent, Controller
from browser_use.llm import ChatOpenAI, ChatGoogle
import handler

controlHandler = Controller()

async def main():



    print(f'Give me answer for surver question 2: "How do you feel about the current state of the world?"')
    answer = input('Your answer: ')
    if not answer:
        answer = ""

    agent = Agent(
        task=(
        'Important : I am UI Automation Tester validating the task using Playwright.\n'
        '1. Open browser, from the curent tab, navigate to website https://survey.filum.asia/l/dwlqrz\n'
        '2. Click randomly into one of five icon in center of the page, then click into "Next" or "Tiếp tục" button\n'
        f'3. Fill the text field with "{answer}", wait for 5 seconds and click into "Next" or "Tiếp tục" button\n'
        '4. Click into "Next" or "Tiếp tục" button\n'
        '5. Click into "Next" or "Tiếp tục" button\n'
        '6. Click into "Next" or "Tiếp tục" button\n'
        '7. Click into "Next" or "Tiếp tục" button\n'
        '8. Click into "Next" or "Tiếp tục" button\n'
        '9. Click into "Next" or "Tiếp tục" button\n'
        '10. Click into "Next" or "Tiếp tục" button\n'
        '11. Click into "Next" or "Tiếp tục" button\n'
        '12. Click into "Send" or "Gửi phản hồi" button\n'
        ),
        llm=ChatGoogle(
            model= 'gemini-2.0-flash-exp'
        ),
        controller=controlHandler,
    )
    history = await agent.run()
    test_result = history.final_result()
    print("\n"+ test_result)

asyncio.run(main())