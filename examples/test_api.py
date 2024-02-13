import requests
host = "http://172.30.131.12:7999"
import time


#
# def _post() -> requests.Response:
#     endpoint = host + "/v1/generation/text-to-image"
#     prompt = "james franco man on a boat with stacks of dollars"
#     return requests.post(endpoint, data=json.dumps({"prompt": prompt,
#                                                     "image_number": 1,
#                                                     "model_name":}), headers={"Content-Type": "application/json",
#                                                                                "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"})
#

def _get() -> requests.Response:
    endpoint = host + "/v1/engines/all-models2"
    response = requests.get(url=endpoint,
                            timeout=30,
                            headers={"Content-Type": "application/json",
                             "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"}
                            )
    print(response.json())
    return response


def upload_lora_example() -> requests.Response:
    endpoint = host + "/v1/engines/upload-lora"
    file_path = "/data/loras/zoril-james_franco_man_sdxl_base_1.safetensors"
    files = {"file": open(file_path, "rb")}
    resp = requests.post(endpoint, files=files, headers={
                             "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"}
                         )
    return resp


def upload_checkpoint_example() -> requests.Response:
    endpoint = host + "/v1/engines/upload-checkpoint"
    file_path = "/data/checkpoints/pixlAnimeCartoonComic_v10.safetensors"
    files = {"file": open(file_path, "rb")}
    begin = time.time()
    resp = requests.post(endpoint, files=files, headers={
        "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"})
    end = time.time()
    return resp



if __name__ == "__main__":
    # _get()
    resp = upload_checkpoint_example()
    print(resp.content)