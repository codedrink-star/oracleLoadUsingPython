import logging
import subprocess

logging.basicConfig(level=0)


def main():
    logging.info("Main function Started")
    logging.info("File: pincode.csv")
    logging.info("### Running Oracle Loader ###")
    output = subprocess.run(["python", "loader.py"])
    print(output)
    if output.returncode != 0:
        logging.error("Process Failed... Please check")
        return False
    else:
        return True


if __name__ == "__main__":
    if main():
        exit(0)
    else:
        exit(1)
