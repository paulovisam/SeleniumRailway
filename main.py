from fastapi import FastAPI, BackgroundTasks, HTTPException
from pydantic import BaseModel
from extract import *
from telegram import TelegramBot
from datetime import datetime
import os
import time

SECRET = os.getenv("SECRET")

#
app = FastAPI()
tg = TelegramBot()
class Msg(BaseModel):
    msg: str
    secret: str

@app.get("/")

async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}


@app.get("/homepage")
async def demo_get():
    print('abrindo navegador')
    driver=createDriver()
    print('obtendo retorno')
    homepage = getGoogleHomepage(driver)
    driver.close()
    tg.send_message(f'{datetime.now()}')
    return homepage

@app.get('/run')
def get_run():
    while True:
        tg.send_message(f'{datetime.now()}')
        time.sleep(5)

@app.post("/backgroundDemo")
async def demo_post(inp: Msg, background_tasks: BackgroundTasks):
    
    background_tasks.add_task(doBackgroundTask, inp)
    return {"message": "Success, background task started"}
    


