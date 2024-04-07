def rawDataToJson(raw_headers):
    raw_headers = raw_headers.strip()

    # Initialize dictionaries
    cookies = {}
    headers = {}

    # Split raw headers into lines
    lines = raw_headers.split("\n")

    # Process each line
    for line in lines:
        key, value = line.split(": ", 1)  # Split each line into key and value by the first colon
        # if key == "Mobile-Token":
        #     # This is assumed to be a cookie
        #     cookies[key] = value
        # else:
        #     # Everything else is treated as a header
        headers[key] = value

    # Adjust the 'Content-Length' value as per your logic; here it is corrected to '71'
    headers['Content-Length'] = '71'

    # Output the dictionaries
    # print("Cookies:")
    # print(cookies)
    # print("\nHeaders:")
    # print(headers)
    return headers
