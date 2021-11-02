import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')  # 從環境變數拿取API KEY 要在project根目錄下新增.env檔存入要設定的環境變數
