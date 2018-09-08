"""
This file record the common usage of logging.
Level: DEBUG, INFO, WARMING, ERROR, CRITIAL
Logging method: info(), debug(), warn(), warning, error, exception, critical
"""

import logging

# simple logging with error level
logging.error("This is the error message!!!")

# logging to a file
logging.basicConfig(filename='logs.log', level=logging.DEBUG)
logging.info("This is the info message!!!")

# logging to a file with overwrite mode
logging.basicConfig(filename='logs.log', filemode='w', level=logging.DEBUG)
logging.info("This is the info messgae!!!")

# logging from multiple modules
# main.py
import logging
import mymodule

def main():
    logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.info('Started')
    mylib.do_something()
    logging.info('Finished')

if __name__ == '__main__':
    main()

# mymoduler.py
import logging

def do_something():
    logging.info('Doing something')
    
# logging variable data
logging.warning('%s before you %s', 'Look', 'leap!')

# Chaging the format of displayed messages
logging.basicConfig(format='%(levelname)s-%(asctime)s:%(message)s', level=logging.DEBUG, datafmt='%m/%d/%Y %I:%M:%S %p')
