import logging

existing_loggers = {}


def init_logging(logger_name, level=logging.INFO):
    if logger_name in existing_loggers.keys():
        return existing_loggers[logger_name]
    else:
        logger = logging.getLogger("{name}".format(
            name=logger_name
        ))
        logger.setLevel(level)
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        existing_loggers[logger_name] = logger
        return logger
