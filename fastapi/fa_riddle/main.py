from fastapi import FastAPI

import requests

app = FastAPI()

'''
/healthcheck is always at the top.
this is use to verify if the API is online.
'''
@app.get("/healthcheck")
def read_item():
    return {"message": "API is Online"}


@app.get("/{count}")
async def read_root(count: int):

    '''
    initializing a list
    '''
    riddles = []
    
    '''
    checks if count is equal to zero(0)
    if count is zero(0) then count will be one(1)
    '''
    if not count:
        count = 1
    
    '''
    loops until it reaches the count
    '''
    for i in range(count):

        '''
        sends a request to get one(1) riddle from the other API
        '''
        response = requests.get('https://riddles-api.vercel.app/random')

        '''
        adds the riddle to the list
        '''
        riddles.append(response.json())

    '''
    returns the riddle list
    '''
    return riddles


