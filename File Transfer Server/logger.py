import logging

logging.basicConfig(filename='server.log', level=logging.INFO)

def log_event(message):
    logging.info(message)