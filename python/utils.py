import datetime
import json
import logging
from time import mktime


# HTTP Status Codes considered as OK
HTTPS_OK_CODES = [200, 201, 202]


class DefaultEncoder(json.JSONEncoder):
    """Encode for the json
    """
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))

        return json.JSONEncoder.default(self, obj)


def print_json(json_data):
    """Print json data nicely
    """
    ret = json.dumps(json_data, cls=DefaultEncoder, sort_keys=True, indent=2)
    logging.info(ret)
    return ret


def check_response(resp):
    """Check response and log message if needed
    """
    ret = resp["ResponseMetadata"]["HTTPStatusCode"] in HTTPS_OK_CODES
    if ret is False:
        logging.error(f"Response:\n{json.dumps(resp, cls=DefaultEncoder, sort_keys=True, indent=2)}")
    return ret
