class Error:
    def __init__(self, code: str):
        self.code = code

    def get_code(self):
        return self.code

# ERROR_CODE
NO_FILE = "0"
FILE_TYPE_WRONG = "1"
AUDIO_USE_WRONG = "2"
CLIP_ERROR = "3"
ENVIRONMENT_WRONG = "4"
NEED_ADMIN = "5"
EDIT_REGISTER_WRONG = "6"
SET_ENVIRONMENT = "7"
TRANSFORM_ERROR = "8"
BAIDU_BUILD_TOKEN_WRONG = '9'
BAIDU_QUERY_TASK_FORMAT_CHANGE = "10"
USE_POST_ERROR = "11"
