import asyncio
from dotenv import load_dotenv
load_dotenv()
from browser_use import Agent
from browser_use.llm import ChatGoogle

async def main():
    agent = Agent(
        task=(
        'Important : I am UI Automation Tester validating the task using Playwright.\n'
        '1. Open browser, navigate to website https://survey.filum.asia/l/dwlqrz\n'
        '2. Click randomly into one of five icon in center of the page\n'
        '3. Click into "Next" or "Tiếp tục" button\n'
        '4. Click into "Next" or "Tiếp tục" button\n'
        '5. Click into "Next" or "Tiếp tục" button\n'
        '6. Click into "Next" or "Tiếp tục" button\n'
        '7. Click into "Next" or "Tiếp tục" button\n'
        '8. Click into "Next" or "Tiếp tục" button\n'
        '9. Click into "Next" or "Tiếp tục" button\n'
        '10. Click into "Next" or "Tiếp tục" button\n'
        '11. Click into "Next" or "Tiếp tục" button\n'
        '12. Click into "Send" or "Gửi phản hồi" button\n'
        '13. Close current browser\n'
        ),
        llm=ChatGoogle(model="gemini-2.0-flash-exp"),
    )
    history = await agent.run()
    test_result = history.final_result()
    print("\n"+ test_result)

asyncio.run(main())