import logging
import subprocess
import configparser

logging.basicConfig(level=0)

try:
    config = configparser.RawConfigParser()
    config.read("./config/resource.cfg")
    oracle = dict(config.items("oracle"))
    connString = "{username}/{password}@{server}:{port}/{sid}".format(
        username=oracle["username"],
        password=oracle["password"],
        server=oracle["server"],
        port=oracle["port"],
        sid=oracle["sid"],
    )
    ctl = dict(config.items("ctl"))
    cmd = "sqlldr {conn} control={ctl} log='./log/address.log'".format(
        conn=connString, ctl=ctl["address"]
    )
    output = subprocess.call(cmd, shell=True, stderr=True)
    if output != 0:
        logging.error("Load Failed..Please check")
        exit(1)
    else:
        logging.info("### Oracle Loader completed successfully ###")
except Exception as err:
    logging.error(err)
    logging.error("Process exiting with status 1")
    exit(1)
