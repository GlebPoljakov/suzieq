from typing import Optional
from fastapi import FastAPI, HTTPException
import logging
import uuid


from suzieq.sqobjects import *

# TODO: logging to this file isn't working
logging.FileHandler('/tmp/rest-server.log')
logger = logging.getLogger(__name__)
app = FastAPI()



@app.get("/api/v1/table/{verb}")
async def read_table(verb: str):
    if verb == 'show':
        verb = 'get'
    return getattr(tables.TablesObj(), verb)().to_json(orient="records")

@app.get("/api/v1/device/{verb}")
async def read_device(verb: str, hostname: str = "",
                      start_time: str = "", end_time: str = "",
                      view: str = "latest", namespace: str = ""):
    if verb == 'show':
        verb = 'get'
    try:
        return getattr(device.DeviceObj(hostname=hostname,
                                    start_time=start_time,
                                    end_time=end_time,
                                    view=view,
                                    namespace=namespace), verb)\
                                    (hostname=hostname, 
                                    namespace=namespace)\
                                    .to_json(orient="records")
        
    except AttributeError as err:
        u = uuid.uuid1()
        logger.warning(f"invalid verb {verb}: {err} id={u}")
        raise HTTPException(status_code=404, detail=f"{verb} not supported id={u}")