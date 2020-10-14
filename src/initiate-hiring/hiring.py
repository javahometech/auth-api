import boto3
import json
import os
import uuid

def post(event, context):
    resp = {
        'statusCode':201,
        "message": "Panel added Successfully"
    }
    return json.dumps(resp)