import logging


class LogGen:

    @staticmethod
    def loggen():
        # logfile = "C:\\Users\\subha\\PycharmProjects\\iBridge360Aroha\\Logs\\automation.log"
        # logging.basicConfig("C:\\Users\\subha\\PycharmProjects\\iBridge360Aroha\\Logs\\automation.log", format='%(asctime)s: %(levelname)s:%(message)s', datefmt='%m-%d-%Y %I:%M:%S %p')

        logging.basicConfig()
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger

