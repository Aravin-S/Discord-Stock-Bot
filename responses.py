import random
import re
from getstock import getData

def handle_response(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey there!'

    if p_message == '!help':
        return "`Type $(Stock) to obtain the current Stock Price in CAD.`"
    
    if re.search('$',message):
        return getData(message[1:])
    
   

    
