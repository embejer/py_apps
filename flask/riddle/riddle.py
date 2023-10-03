'''
#pip install requests
this is an http request module like fetch
'''
import requests

'''
function get_riddles has one(1) parameter
and returns a list of riddles
`count` is the number of riddles to be return.
'''
def get_riddles(count):

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