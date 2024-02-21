import requests
from pathlib import Path
import json
import time

host = "http://172.30.131.12:8000"
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


def upload_lora_example(lora_fp: Path) -> requests.Response:
    endpoint = host + "/v1/engines/upload-lora"

    files = {"file": open(lora_fp, "rb")}
    resp = requests.post(endpoint, files=files, headers={
                             "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"}
                         )
    return resp


def upload_checkpoint_example(checkpoint_path: Path) -> requests.Response:
    endpoint = host + "/v1/engines/upload-checkpoint"
    files = {"file": open(checkpoint_path, "rb")}
    resp = requests.post(endpoint, files=files, headers={
        "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"})
    return resp


def test_lora_checkpoint_call() -> requests.Response:
    endpoint = host + "/v1/generation/text-to-image"
    prompt = "(jean claude van damme man:1.5) swimming with sharks comic book"
    return requests.post(endpoint, data=json.dumps({"prompt": prompt,
                                                    "image_number": 1,
                                                    "base_model_name": "pixlAnimeCartoonComic_v10.safetensors",
                                                    "loras": [{
                                                                  "model_name": "giga-Jean Claude Van Damme man_sdxl_base_1.safetensors",
                                                                  "weight": 1},
                                                              {"model_name": "EldritchComicsXL1.2.safetensors",
                                                               "weight": 1}]}),
                         headers={"Content-Type": "application/json",
                                  "X-API-KEY": "5d1c8432-a0e0-42f9-8d53-c1fd3f301b8f"})


def upload_stuff_and_test():
    # 1. upload lora
    lora_path = Path("/data/loras/giga-Jean Claude Van Damme man_sdxl_base_1.safetensors")
    resp = upload_lora_example(lora_fp=lora_path)
    print(resp.content)
    lora_path = Path("/data/loras/EldritchComicsXL1.2.safetensors")
    resp = upload_lora_example(lora_fp=lora_path)
    print(resp.content)
    # 2. upload checkpoint
    checkpoint_path = Path("/data/checkpoints/pixlAnimeCartoonComic_v10.safetensors")
    resp = upload_checkpoint_example(checkpoint_path=checkpoint_path)
    print(resp.content)
    # 3. test lora checkpoint call
    response = test_lora_checkpoint_call()
    print()


def multiple_calls(n: int = 10):
    for n in range(n):
        begin = time.time()
        response = test_lora_checkpoint_call()
        print(response.json())
        end = time.time()
        print(f"Time taken: {end - begin}")


if __name__ == "__main__":
    upload_stuff_and_test()