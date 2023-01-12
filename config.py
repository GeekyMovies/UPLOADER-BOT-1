import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5915563603:AAE1STI93wsA7MK9pma-MOKXU4Gww5KxwWk")
    
    API_ID = int(os.environ.get("API_ID", 23311160))
    
    API_HASH = os.environ.get("API_HASH", "2a1366013eca4256bce853346dbcda49")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "5691018873"))

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Geekymovies:Geekymovies@cluster0.7llffit.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "50"
