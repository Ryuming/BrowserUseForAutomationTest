

Step 1: Open virtual environment 
    python -m venv your_venv_name
  - For Windows: 
      cd your_venv_name\Scripts
      activate.bat
  - For MacOS:
      source your_venv_name/Scripts/activate

Step 2: Install required package
    pip install browser-use asyncio dotenv

Step 3: Install Playwright 
    playwright install

Step 4: Rename environment.file into .env, get your own GOOGLE_API_KEY and GOOGLE_APPLICATION_CREDENTIALS then save your .env 

Step 5: Back to your project root folder and run demo.py
  - For Windows:
      cd ..\..\
      python demo.py
  - For MacOS:
      Rich people please fill this field, i'm not using any MacOS device
