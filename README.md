# SNS-Lambda-SQS ⚙️

This project shows how to connect a simple **web page** to an **AWS SNS FIFO Topic** using **Lambda** and **API Gateway**. 
A fast, minimal setup to push browser messages straight to SNS.

## 📂 Project Structure
sns-lambda-sqs/
│── lambda_function.py # Backend — Lambda handler
│── index.html # Frontend — HTML page
│── README.md # Documentation

## Files
1) **[SNS-LAMBDA-SQS](lambda_function.py)** → Lambda backend
  - Serves the HTML page on **GET**  
  - Publishes messages to SNS FIFO on **POST**
    
2) **[SNS-LAMBDA-SQS](index.html)** → Frontend  
  - Input field and button to send messages  
  -JavaScript `fetch()` to POST messages to Lambda

## How It Works
1. User opens the API Gateway URL → sees `index.html`.  
2. Enters a message and clicks **Send**.  
3. The frontend calls Lambda (POST).  
4. Lambda publishes the message to **SNS FIFO Topic** with `MessageGroupId` and `MessageDeduplicationId`.  
5. Response is shown on the web page and message is available in SNS subscribers.  

## Setup
1. Create an **SNS FIFO Topic** in AWS.  
2. Deploy **[SNS-LAMBDA-SQS](lambda_function.py)** to a Lambda function.  
3. Give Lambda `sns:Publish` permission for your topic.  
4. Connect Lambda to **API Gateway** (enable CORS).  
5. Open the endpoint in a browser and start sending messages!  

## Example
- Input: `Hello SNS!`  
- Frontend Response: `Message sent: Hello SNS!`  
- SNS Topic Message: stored in order with FIFO guarantees.  

## Stack
- AWS Lambda  
- Amazon SNS (FIFO)
- API Gateway  
- HTML + JavaScript  

Simple, serverless, and ready to try.
