def handler(request, context):
    headers = {'content-type': 'text/html; charset=utf-8;'}
    return {'statusCode': 200, 'headers': headers, 'body': '<h1>Hello World! 🎉</h1>'}
