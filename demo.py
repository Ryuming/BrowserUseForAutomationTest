import asyncio
from dotenv import load_dotenv
load_dotenv()
import os

from langchain_mistralai import ChatMistralAI
from chat import ChatLangchain
from browser_use import Agent, Controller, BrowserSession, BrowserProfile, AgentHistoryList
from browser_use.llm import ChatOpenAI, ChatGoogle
import handler

from model.showcase_portal.interactive_button import interactive_button
from model.showcase_portal.input_field import input_field
from handler.CSV_handler import CSVHandler

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
    username = os.environ.get('FILUM_STAGING_USERNAME')
    password = os.environ.get('FILUM_STAGING_PASSWORD')
    sensitive_data = {
         'https://*.filum.asia': {
        'x_username': username,
        'x_password': password,
    },
    }
    variable_collection = {
        "anwser": input_field(
            name='answer',
            description='Answer for survey question 2: "How do you feel about the current state of the world?"',
            input_value='Test',
        ),
        "targetURL": input_field(
            name='targetURL',
            description='Target URL for showcase portal',
            input_value='https://demo.filum.asia/agents-showcase/auth?code=d7R8YrlyANxhYMKZ7Ejm70mphBvt968TnHwGYRy8AqE',
        ),
        "workspace" : input_field(
            name='workspace',
            description='Workspace to select in the left of avatar icon',
            input_value='thien+dance',
        ),
        "domain_url": input_field(
            name='domain_url',
            description='Domain URL for Filum company',
            input_value='https://cx.filum.ai',
        ),
        "username": input_field(
            name='username',
            description='Username for Filum company',
            input_value=os.environ.get('FILUM_PRODUCTION_USERNAME'),
        ),
        "password": input_field(
            name='password',
            description='Password for Filum company',
            input_value=os.environ.get('FILUM_PRODUCTION_PASSWORD'),
        ),
        "sensitive_data": input_field(
            name='sensitive_data',
            description='Sensitive data for Filum company',
            input_value={
                'https://*.filum.ai': {
                    'x_username': os.environ.get('FILUM_PRODUCTION_USERNAME'),
                    'x_password': os.environ.get('FILUM_PRODUCTION_PASSWORD'),
                },
            },
        ),
        "feature_name": input_field(
            name='feature_name',
            description='Feature name to perform testing',
            input_value='Showcase Portal',
        ),
        "feature_description": input_field(
            name='feature_description',
            description='Feature description to perform testing',
            input_value='The AI Agent Showcase is a strategic sales and marketing module designed to accelerate customer acquisition. It empowers administrators to create and share secure, time-limited invitation links for a specific, pre-configured AI agent. These links direct potential clients to an interactive, public-facing "Showcase Portal" or playground environment. Here, prospects can engage directly with the AI agent, experiencing its capabilities firsthand in a live demo. The showcase is explicitly designed for lead generation, featuring a prominent call-to-action that encourages interested users to make contact, effectively bridging the gap between product demonstration and sales conversion.',
        ),
    }

    button_collection = {
        "button_contact_us" : interactive_button(
            name='Contact us',
            use='click to navigate to contact page',
        ),
        "button_send" : interactive_button(
            name='Send',
            use='click to send message to AI Agent',
        ),
        "button_new_session" : interactive_button(
            name='New session',
            use ='click to create new session to chat with AI Agent',
        ),
        "button_icon" : interactive_button(
            name='Icon',   
            use='click to open icon list and select an icon to chat with AI Agent',
        ),
        "button_attach_file" : interactive_button(
            name='Attach file',
            use='click to attach file to chat with AI Agent',
        ),
    }
    
    """Read the CSV file and return its content as a DataFrame"""
    csv_handler = CSVHandler(file_path='./data/showcase_portal_prompt.csv')
    prompt = csv_handler.read_csv()


    for i in range(len(prompt)):
        agent = Agent(
            task=(
            'Variable list: \n'
            f'{variable_collection["anwser"].name}: "{variable_collection["anwser"]._input_value}"\n'
            f'{variable_collection["targetURL"].name}: "{variable_collection["targetURL"]._input_value}"\n'
            f'{variable_collection["workspace"].name}: "{variable_collection["workspace"]._input_value}"\n'
            f'{variable_collection["domain_url"].name}: "{variable_collection["domain_url"]._input_value}"\n'
            f'{variable_collection["username"].name}: "{variable_collection["username"]._input_value}"\n'
            f'{variable_collection["password"].name}: "{variable_collection["password"]._input_value}"\n'
            f'{variable_collection["sensitive_data"].name}: "{variable_collection["sensitive_data"]._input_value}"\n'
            f'{variable_collection["feature_name"].name}: "{variable_collection["feature_name"]._input_value}"\n'
            f'{variable_collection["feature_description"].name}: "{variable_collection["feature_description"]._input_value}"\n'
            'Button list: \n'
            f'{button_collection["button_contact_us"].name}: {button_collection["button_contact_us"].use}\n'
            f'{button_collection["button_send"].name}: {button_collection["button_send"].use}\n'
            f'{button_collection["button_new_session"].name}: {button_collection["button_new_session"].use}\n'
            f'{button_collection["button_icon"].name}: {button_collection["button_icon"].use}\n'
            f'{button_collection["button_attach_file"].name}: {button_collection["button_attach_file"].use}\n'
            # 'Important : I am a UI Automation Tester validating the survey feature of Filum company by using Playwright. \n'
            # 'Remember: if instruction require choose/pick/select randomly, they must be ramdom, read entire answers from survey before deciding. Please record your answer for each question in survey and show me when your task is done.\n'
            # '1. Open browser, from the curent tab, navigate to website https://survey.filum.ai/l/txbxef \n'
            # '2. In "Câu hỏi 1", click randomly into one of five icon in center of the page, then click into "Tiếp tục" button\n'
            # f'3. In "Câu hỏi 2", fill the text field with "{answer}", wait for 3 seconds and click into "Tiếp tục" button\n'
            # '4. In "Câu hỏi 3", Choose 2 random answers from the answer list, wait for 3 seconds and click into "Tiếp tục" button\n'
            # '5. In "Câu hỏi 4", Select one random value for each row, wait for 3 seconds and click into "Next" or "Tiếp tục" button\n'
            # '6. In "Câu hỏi 5", Fill any random string (about 20 characters) into "Giảng viên" and "Lịch học" text field, Click into "Next" or "Tiếp tục" button\n'
            # '7. If screen shows "Cảm ơn bạn đã phản hồi", then the task is completed successfully. Test case is passed, please tell me the test case is passed or not and the survey answers set you have recorded.\n'
            f'Important : I am a Manual Tester testing new feature named {variable_collection["feature_name"].input_value} of Filum company by using Playwright. Feature description: {variable_collection["feature_description"].input_value}\n'
            'Remember: Do the task carefully and follow the instruction. If cannot found expected element, maybe it is displaying in other language, try to translate from vietnamese into english to perform the task\n'
            'Please follow these instructions:\n'
            f'{prompt["prompt_text"][i]}\n'
            ),
            llm=ChatGoogle(
                model= 'gemini-2.0-flash-exp'
            ),
            sensitive_data=sensitive_data,
            controller=controlHandler,
            use_vision=True,
            browser_session=browser_session,
        )
        
        history = await agent.run()
        test_result = history.final_result()
        print("\n"+ test_result)
       
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
