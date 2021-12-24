import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')  # 從環境變數拿取API KEY 要在project根目錄下新增.env檔存入要設定的環境變數

DOWNLOADS_DIR = 'downloads'
CAPTIONS_DIR = os.path.join(DOWNLOADS_DIR, 'captions')  # 將下載的資料分別存在不同的資料夾中->captions及videos在downloads李
VIDEOS_DIR = os.path.join(DOWNLOADS_DIR, 'videos')
OUTPUTS_DIR = 'outputs'