def app(environ, start_response):
    data = ""
    for item in environ['QUERY_STRING'].split("&"):
        data += item + "\n"

    status = "200 OK"
    headers = [
        ("Content-Type", "text/plain")
    ]
    start_response(status, headers)
    return [data]
