import requests
import json

host = "http://172.30.131.12:7999"


def _post() -> requests.Response:
    endpoint = host + "/v1/generation/text-to-image"
    prompt = "small abstract tree of life tattoo with geometric shapes in a techno style, the tattoo has circle around it in the style of zen Buddhism"
    return requests.post(endpoint, data=json.dumps({"prompt": prompt,
                                                    "image_number": 1}), headers={"Content-Type": "application/json",
                                                                               "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"})

if __name__ == "__main__":
    response = _post()
    print(response.content)