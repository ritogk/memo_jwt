from app import create_app
from Config import Config
from dotenv import load_dotenv

# 環境変数読み込み
load_dotenv(override=True)
config = Config.getInstance()

create_app()
