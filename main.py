from urllib.request import urlopen
import json
from constant import local_host, core_books, query

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    connection = urlopen(local_host+core_books+query)
    response = connection.read()
    # Decode UTF-8 bytes to Unicode, and convert single quotes
    # to double quotes to make it valid JSON
    data = json.loads(response.decode('utf-8'))
    '''
    for key, value in data.items():
        if key == "response":
            for response_key, response_value in value.items():
                if response_key == "docs":
                    print(len(response_value))
    '''

    doc = data.get("response").get("docs")
    for ith_doc in doc:
        print(ith_doc)
