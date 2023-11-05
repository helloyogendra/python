import os
import logging


# Configure logging once in your main module or script
output_log_file = "testCase.log"
log_file_path = os.path.join(r"c:\temp", output_log_file)

logging.basicConfig(
    filename=log_file_path,
    filemode="a",
    level=logging.INFO,  # Set the desired default log level here
    format="%(asctime)s : %(levelname)s : %(message)s : %(lineno)d",
    datefmt="%Y-%m-%d %I:%M:%S%p",
)

def custom_logger(fileName, logMsg, logLevel="err"):
   
    file = os.path.basename(fileName)
    log = f"File={file} : {logMsg}"

    # ANSI escape sequences for color coding in console.
    GREEN = "\033[32m"
    YELLOW = "\033[93m"
    RED = "\033[31m"
    RESET = "\033[0m"

    console = logging.StreamHandler()

    console.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s : %(lineno)d")

    console.setFormatter(formatter)

    logging.getLogger().addHandler(console)

    if logLevel == "debug":
        logging.debug(log)
    elif logLevel == "info":
        logging.info(log)
        print(f"{GREEN}{log}{RESET}")
    elif logLevel == "err":
        logging.error(log)
        print(f"{RED}{log}{RESET}")
    elif logLevel == "warn":
        logging.warning(log)
        print(f"{YELLOW}{log}{RESET}")
    elif logLevel == "crit":
        logging.critical(log)



#test
custom_logger(fileName=__file__, logMsg="Info", logLevel="info")
custom_logger(fileName=__file__, logMsg="Warn", logLevel="warn")
custom_logger(fileName=__file__, logMsg="Error", logLevel="err")



