import json
import os
import boto3
from decimal import Decimal


def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)


def lambda_handler(event, context):
    print("Received Event:", json.dumps(event, indent=2))

    http_method = event.get("httpMethod") or event.get(
        "requestContext", {}
    ).get("http", {}).get("method")

    # Only allow GET requests.
    # Reject invalid methods before connecting to DynamoDB.
    if http_method != "GET":
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid HTTP method"})
        }

    try:
        dynamodb = boto3.resource("dynamodb")

        table_name = os.environ["TABLE_NAME"]
        table = dynamodb.Table(table_name)

        response = table.update_item(
            Key={"id": "views"},
            UpdateExpression="SET #c = if_not_exists(#c, :start) + :inc",
            ExpressionAttributeNames={"#c": "count"},
            ExpressionAttributeValues={
                ":inc": 1,
                ":start": 0
            },
            ReturnValues="UPDATED_NEW"
        )

        views_count = response["Attributes"]["count"]

        return {
            "statusCode": 200,
            "body": json.dumps(
                {"views": views_count},
                default=decimal_default
            )
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }