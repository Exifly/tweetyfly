#!/usr/bin/env python3
from termcolor import colored
import tweetyfly

start_text = '''                                                                                            
888888888888                                                            ad88 88              
     88                                            ,d                  d8"   88              
     88                                            88                  88    88              
     88 8b      db      d8  ,adPPYba,  ,adPPYba, MM88MMM 8b       d8 MM88MMM 88 8b       d8  
     88 `8b    d88b    d8' a8P_____88 a8P_____88   88    `8b     d8'   88    88 `8b     d8'  
     88  `8b  d8'`8b  d8'  8PP""""""" 8PP"""""""   88     `8b   d8'    88    88  `8b   d8'   
     88   `8bd8'  `8bd8'   "8b,   ,aa "8b,   ,aa   88,     `8b,d8'     88    88   `8b,d8'    
     88     YP      YP      `"Ybbd8"'  `"Ybbd8"'   "Y888     Y88'      88    88     Y88'     
                                                             d8'                    d8'      
                                                            d8'                    d8'       
'''

if __name__ == "__main__":
    print(colored(start_text, 'cyan', attrs=['bold']))
    min_delay = 2
    max_delay = 2
    tweetyfly.start(min_delay, max_delay)