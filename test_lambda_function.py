from unittest.mock import patch, MagicMock

from lambda_code.lambda_function import lambda_handler

import os

def test_get_request():
    os.environ["TABLE_NAME"] = "MyResumeViewCount"
    # Create a fake DynamoDB response.
    fake_response = {
        "Attributes": {
            "count": 101
        }
    }

    # Create a fake DynamoDB table.
    mock_table = MagicMock()

    # Tell the fake table what update_item() should return.
    mock_table.update_item.return_value = fake_response

    # Create a fake DynamoDB resource.
    mock_dynamodb = MagicMock()

    # Tell the fake resource which table to return.
    mock_dynamodb.Table.return_value = mock_table

    # Replace boto3.resource() with our fake DynamoDB resource.
    with patch("lambda_code.lambda_function.boto3.resource", return_value=mock_dynamodb):

        # Create a fake GET request.
        event = {
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            }
        }

        # Run our Lambda function.
        response = lambda_handler(event, None)

        # Check that Lambda returned HTTP 200.
        assert response["statusCode"] == 200

        # Check that DynamoDB's update_item() was called once.
        mock_table.update_item.assert_called_once()


def test_invalid_http_method():
    os.environ["TABLE_NAME"] = "MyResumeViewCount"
    # Create a fake POST request.
    event = {
        "requestContext": {
            "http": {
                "method": "POST"
            }
        }
    }

    # Run the Lambda function.
    response = lambda_handler(event, None)

    # Check that Lambda rejected the request.
    assert response["statusCode"] == 400


def test_dynamodb_error():
    os.environ["TABLE_NAME"] = "MyResumeViewCount"
    # Create a fake DynamoDB table.
    mock_table = MagicMock()

    # Make DynamoDB pretend that an error occurred.
    mock_table.update_item.side_effect = Exception("DynamoDB error")

    # Create a fake DynamoDB resource.
    mock_dynamodb = MagicMock()

    # Tell the fake resource to return our fake table.
    mock_dynamodb.Table.return_value = mock_table

    # Replace real boto3 with the fake DynamoDB resource.
    with patch("lambda_code.lambda_function.boto3.resource", return_value=mock_dynamodb):

        # Create a fake GET request.
        event = {
            "requestContext": {
                "http": {
                    "method": "GET"
                }
            }
        }

        # Run the Lambda function.
        response = lambda_handler(event, None)

        # Check that Lambda returned HTTP 500.
        assert response["statusCode"] == 500