import sys

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from config import Config

CONFIG_FILE_PATH = "/path/to/file"

if CONFIG_FILE_PATH is None:
    sys.exit("There is no config file-path!")

app = FastAPI()

@app.get("/")
async def root():
    if CONFIG.debug:
        print("Debug mode is enabled!")


    return {"message": CONFIG.message, "servers": CONFIG.servers}


@app.get("/dynamicconfig")
async def dynamicconfig():
    if CONFIG.debug:
        print("Debug mode is enabled!")

    return {"message": CONFIG.message, "servers": CONFIG.servers}

CONFIG = None

@app.on_event("startup")
@repeat_every(seconds=5)
def reload_config():
    global CONFIG
    print("Reloading the config from {}".format(CONFIG_FILE_PATH))

    try:
        CONFIG = Config.from_json(open(CONFIG_FILE_PATH, "r").read())
    except:
        print("Error loading configuration file.")

    if CONFIG is None: # CONFIG is declared as None before first successful assignment
        sys.exit('No configuration, exiting application.')