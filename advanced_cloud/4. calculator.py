import json
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logger.info("Starting lambda")

def calculate(number1, number2, operator):
    if operator == '+':
        return f"{number1} + {number2} = {number1 + number2}"
    elif operator == '-':
        return f"{number1} - {number2} = {number1 - number2}"    
    elif operator == '*':
        return f"{number1} * {number2} = {number1 * number2}"
    elif operator == '/':
        try:
            return f"{number1} / {number2} = {number1 / number2}"
        except ZeroDivisionError:
            return "Error: Division by zero"
    else:
        return f"Error: Invalid operator {operator}"

def lambda_handler(event, context):
    logger.info(f"Received event: {event}")
    method = event.get('httpMethod', '')
    path = event.get('path', '')

    if path == '/calc':
        if method == 'GET':
            logger.info("GET request received")
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'number1': "float(2)",
                    'number2': "float(2)",
                    'operator': "str within ['+', '-', '*', '/']"
                })
            }

        elif method == 'POST':
            logger.info("POST request received")
            try:
                data = event.get('body', '{}')
                if isinstance(data, str):
                    data = json.loads(data)
                number1 = float(data['number1'])
                number2 = float(data['number2'])
                operator = data['operator']
                result = calculate(number1, number2, operator)

                return {
                    'statusCode': 200,
                    'body': json.dumps({'result': result})
                }
            except Exception as e:
                logger.error(f"Error in POST: {str(e)}")
                return {
                    'statusCode': 500,
                    'body': json.dumps({'error': str(e)})
                }

        else:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'INVALID METHOD'})
            }

    return {
        'statusCode': 404,
        'body': json.dumps({'error': 'INVALID PATH'})
    }
