import requests
import json

host = "http://172.30.131.12:7999"




def _post() -> requests.Response:
    endpoint = host + "/v1/generation/text-to-image"
    prompt = "james franco man on a boat with stacks of dollars"
    return requests.post(endpoint, data=json.dumps({"prompt": prompt,
                                                    "image_number": 1,
                                                    "model_name": }), headers={"Content-Type": "application/json",
                                                                               "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"})


def _get() -> requests.Response:
    endpoint = host + "/v1/engines/all-models"
    print(endpoint)
    response = requests.get(url=endpoint,
                            timeout=30)
    return response



if __name__ == "__main__":
    resp = _get()
    print()