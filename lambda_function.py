import json
import boto3

sns = boto3.client("sns")
TOPIC_ARN = "arn:aws:sns:ap-south-1:716145636894:myfifotopic.fifo"

def lambda_handler(event, context):
    try:
        method = event.get("requestContext", {}).get("http", {}).get("method", "GET")

        if method == "GET":
            # Return the HTML page
            with open("index.html", "r") as f:
                html_page = f.read()
            return {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "text/html",
                    "Access-Control-Allow-Origin": "*"
                },
                "body": html_page
            }

        elif method == "POST":
            body_raw = event.get("body", "{}")
            try:
                body = json.loads(body_raw)
            except Exception:
                body = {}

            message = body.get("message", "")

            if message:
                sns.publish(
                    TopicArn=TOPIC_ARN,
                    Message=message,
                    Subject="Message from Lambda Webpage",
                    MessageGroupId="web-message-group",  # FIFO required
                    MessageDeduplicationId=str(hash(message))  # unique deduplication
                )
                return {
                    "statusCode": 200,
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"
                    },
                    "body": json.dumps({"status": "Message sent", "message": message})
                }
            else:
                return {
                    "statusCode": 400,
                    "headers": {
                        "Access-Control-Allow-Origin": "*",
                        "Content-Type": "application/json"
                    },
                    "body": json.dumps({"status": "Error", "reason": "No message provided"})
                }

        else:
            return {
                "statusCode": 405,
                "headers": {"Access-Control-Allow-Origin": "*"},
                "body": "Method Not Allowed"
            }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps({"status": "Internal Server Error", "error": str(e)})
        }
