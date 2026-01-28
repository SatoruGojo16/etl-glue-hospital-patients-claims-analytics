import logging
import boto3
import json

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    sns = boto3.resource("sns")
    topic = sns.Topic("arn:aws:sns:us-east-1:023495890465:notify-s3-mail")
    response = topic.publish(
        Message=json.dumps({"Status": "PASSED"}),
    )
    print(response)
    logger.info("###  SNS \r" + "ERR")

    return response
