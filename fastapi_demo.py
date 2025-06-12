from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
app = FastAPI()

from starlette.responses import JSONResponse
# 添加CORS中间件


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/index")
async def index():
    return {"code":"0000","data":"ping"}

@app.get("/get_libary")
async def home():
    return JSONResponse({"code":"0000",
                         "data": [{"name":"Audioxxx"},
                                  {"name": "Freexxx"},
                                  {"name": "Basexxx"}
                                  ]})

chat_list = []
def get_chat_history():
    return chat_list

def add_chat_history(chat_message:dict):
    chat_list.append(chat_message)
    return True

def chat_llm(history_messages):
    """
    与大语言模型交互
    :param history_messages:
    :return:
    """
    return "invoke_xxxx"


@app.post("/chat")
async def get_item(chat_str:str):
    if not chat_str:
        add_chat_history({"system":"What can I do for you?"})
        return {"code":"200","data":chat_list}
    else:
        add_chat_history({"human": chat_str})
        message_list = get_chat_history()
        robot_chat = chat_llm(message_list)
        add_chat_history({"system": robot_chat})
        return {"code":"200","data": chat_list}



if __name__=="__main__":
    uvicorn.run(app, host="127.0.0.1",  port=8000, reload=True)





