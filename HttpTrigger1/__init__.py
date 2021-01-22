import logging

import azure.functions as func

import json 



def main(req: func.HttpRequest) -> str:
    logging.info('Python HTTP trigger function processed a request.')

    firstString = '{"a": 1, "b": 2, "c": 3, "d": 4}'
    jsonData = json.loads(firstString) 

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    return firstString

