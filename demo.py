import asyncio
from dotenv import load_dotenv
load_dotenv()
import os

from langchain_mistralai import ChatMistralAI
from chat import ChatLangchain
from browser_use import Agent, Controller, BrowserSession, BrowserProfile, AgentHistoryList
from browser_use.llm import ChatOpenAI, ChatGoogle
import handler

controlHandler = Controller()

async def main():

    browser_profile = BrowserProfile(
        user_data_dir = None,
        #viewport={'width': 1920, 'height': 1080},  
        headless = False,
        no_viewport = True,
      )  # or 'firefox', 'webkit'

    browser_session = BrowserSession(
        browser_profile=browser_profile,
    )
    # task=(
    #     'Important : I am a UI Automation Tester validating the survey feature of Filum company by using Playwright. \n'
    #     'Remember: if instruction require choose/pick/select randomly, they must be ramdom, read entire answers from survey before deciding. Please record your answer for each question in survey and show me when your task is done.\n'
    #     '1. Open browser, from the curent tab, navigate to website https://survey.filum.ai/l/txbxef \n'
    #     '2. In "Câu hỏi 1", click randomly into one of five icon in center of the page, then click into "Tiếp tục" button\n'
    #     f'3. In "Câu hỏi 2", fill the text field with "{answer}", wait for 3 seconds and click into "Tiếp tục" button\n'
    #     '4. In "Câu hỏi 3", Choose 2 random answers from the answer list, wait for 3 seconds and click into "Tiếp tục" button\n'
    #     '5. In "Câu hỏi 4", Select one random value for each row, wait for 3 seconds and click into "Next" or "Tiếp tục" button\n'
    #     '6. In "Câu hỏi 5", Fill any random string (about 20 characters) into "Giảng viên" and "Lịch học" text field, Click into "Next" or "Tiếp tục" button\n'
    #     '7. If screen shows "Cảm ơn bạn đã phản hồi", then the task is completed successfully. Test case is passed, please tell me the test case is passed or not and the survey answers set you have recorded.\n'

    #     )


    # print(f'Give me answer for surver question 2: "How do you feel about the current state of the world?"')
    # answer = input('Your answer: ')
    # if not answer:
    answer = "Test"

    targetURL = 'https://app.filum.asia/ai-automation?tab=ai-settings'
    workspace = 'Test AI Agent'
    domain_url = 'https://app.filum.asia'
    username = os.environ.get('FILUM_STAGING_USERNAME')
    password = os.environ.get('FILUM_STAGING_PASSWORD')
    sensitive_data = {
         'https://*.filum.asia': {
        'x_username': username,
        'x_password': password,
    },
    }

    for i in range(1):
        agent = Agent(
            task=(
            # 'Important : I am a UI Automation Tester validating the survey feature of Filum company by using Playwright. \n'
            # 'Remember: if instruction require choose/pick/select randomly, they must be ramdom, read entire answers from survey before deciding. Please record your answer for each question in survey and show me when your task is done.\n'
            # '1. Open browser, from the curent tab, navigate to website https://survey.filum.ai/l/txbxef \n'
            # '2. In "Câu hỏi 1", click randomly into one of five icon in center of the page, then click into "Tiếp tục" button\n'
            # f'3. In "Câu hỏi 2", fill the text field with "{answer}", wait for 3 seconds and click into "Tiếp tục" button\n'
            # '4. In "Câu hỏi 3", Choose 2 random answers from the answer list, wait for 3 seconds and click into "Tiếp tục" button\n'
            # '5. In "Câu hỏi 4", Select one random value for each row, wait for 3 seconds and click into "Next" or "Tiếp tục" button\n'
            # '6. In "Câu hỏi 5", Fill any random string (about 20 characters) into "Giảng viên" and "Lịch học" text field, Click into "Next" or "Tiếp tục" button\n'
            # '7. If screen shows "Cảm ơn bạn đã phản hồi", then the task is completed successfully. Test case is passed, please tell me the test case is passed or not and the survey answers set you have recorded.\n'

                'Important : I am a UI Automation Tester configuring AI&Automation setting of Filum company by using Playwright.  \n'
                'Remember: If element are not visible, then scroll to the element. Please record your steps show me when your task is done.\n'
                f'1. Open browser, check if login is required, if yes, then login to {domain_url} with x_username and x_password, if not, then continue to step 2\n'
                f'2. Select workspace in the left of avatar icon, then select {workspace} workspace\n'
                f'3. Navigate to website {targetURL} \n'
                '4. Click into first Agent from the list \n'
                '5. Open Overview tab, then open Instruction modal \n'
                '6. Add Instruction with name from "Instruction1" to "Instruction20" and Save changes after each step \n'
                '7. Click on avatar icon in the top right corner, then click on "Đăng xuất" or "Log out" button to logout\n'
                '8. Show me the your steps and instruction list you created when your task is done.\n'
            ),
            llm=ChatGoogle(
                model= 'gemini-2.0-flash-exp'
            ),
            sensitive_data=sensitive_data,
            controller=controlHandler,
            use_vision=True,
            browser_session=browser_session,
        )
        #code = AgentHistoryList().save_as_playwright_script(output_path= "generated_scripts\github_search.py")
        history = await agent.run()
        test_result = history.final_result()
        print("\n"+ test_result)
        print(f'Generated script saved to: {code}')

asyncio.run(main())

        # This code is a template for a UI Automation Tester using Playwright to interact with Filum's webchat. 
        # 'Important : I am a UI Automation Tester sending message to webchat of Filum company by using Playwright. to verify response \n'
        # 'Remember: wait for response message before sending the next message\n'
        # '1. Open browser, Open 5 tabs, for each tab, navigate to website https://app.filum.asia/conversation-channels/webchat/4177 \n'
        # '2. In each tab, send a message to Filum webchat, the message is "Hello, this is a test message from Playwright" \n'
        # '3. Wait for response message from Filum webchat, then record the sent message and response message \n'
        # '4. In each tab, send message "cho tui xin giá mấy chiếc xe bên mình đi" to Filum webchat" \n'
        # '5. Wait for response message from Filum webchat, then record the sent message andresponse message \n'
        # '6. In each tab, send message "xe cùi bắp mà cũng không có, cáu thật" to Filum webchat\n'
        # '7. Wait for response message from Filum webchat, then record the sent message andresponse message \n'
        # '8. Show me the sent messages and response messages from all tabs when your task is done.\n'
