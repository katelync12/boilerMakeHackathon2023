import requests
import os
import json

# To set your environment variables in your terminal run the following line:
# export 'BEARER_TOKEN'='<your_bearer_token>'
bearer_token = os.environ.get("BEARER_TOKEN")


def create_url():
    return "https://api.twitter.com/2/tweets/sample/stream"


def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2SampledStreamPython"
    return r


def connect_to_endpoint(url):
    # response = requests.request("GET", url, auth=bearer_oauth, stream=True)
    print('running connect')
    tweets = []
    with requests.request("GET", url, auth=bearer_oauth, stream=True) as response:
        print('Tweet endpoint status:',response.status_code)
        if response.status_code != 200:
            print("Request returned an error: {} {}".format(
                    response.status_code, response.text
                ))
            # raise Exception(
            #     "Request returned an error: {} {}".format(
            #         response.status_code, response.text
            #     )
            # )
        # for response_line in response.iter_lines():
        else:
            for i in range(5):
                try:
                    response_line = next(response.iter_lines())
                except:
                    break
                if response_line:
                    json_response = json.loads(response_line)
                    tweets.append(json_response.get('data', {}))
                    # if (json_response[])
                    print(json.dumps(json_response, indent=4, sort_keys=True))
    print("Closed stream")
    return tweets



def main():
    url = create_url()
    timeout = 0
    while True:
        connect_to_endpoint(url)
        timeout += 1


if __name__ == "__main__":
    main()
