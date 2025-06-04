import os
import requests

HOST_ADDRESS = os.getenv("HOST_ADDRESS", "http://127.0.0.1:9380")

DATASET_NAME_LIMIT = 128
CHAT_ASSISTANT_NAME_LIMIT = 128
INVALID_API_TOKEN = "invalid_token"


def batch_create_datasets(auth, num):
    ids = []
    for i in range(num):
        url = f"{HOST_ADDRESS}/v1/kb/create"
        json = {"name": f"dataset_{i}"}
        headers = {"Authorization": auth}
        res = requests.post(url=url, headers=headers, json=json)
        if res.status_code == 200 and "data" in res.json():
            ids.append(res.json()["data"]["id"])
    return ids


def create_chat_assistant(auth, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def list_chat_assistants(auth):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats"
    res = requests.get(url=url, headers=authorization)
    return res.json()


def delete_chat_assistants(auth):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats"
    res = requests.delete(url=url, headers=authorization)
    return res.json()


def create_dataset(auth, dataset_name):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/kb/create"
    json = {"name": dataset_name}
    res = requests.post(url=url, headers=authorization, json=json)
    return res.json()


def list_dataset(auth, page_number, page_size=30):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/kb/list?page={page_number}&page_size={page_size}"
    json = {}
    res = requests.post(url=url, headers=authorization, json=json)
    return res.json()


def rm_dataset(auth, dataset_id):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/kb/rm"
    json = {"kb_id": dataset_id}
    res = requests.post(url=url, headers=authorization, json=json)
    return res.json()


def update_dataset(auth, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/kb/update"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def upload_file(auth, dataset_id, path):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/document/upload"
    json_req = {
        "kb_id": dataset_id,
    }
    with open(f"{path}", "rb") as f:
        files = {"file": f}
        res = requests.post(url=url, headers=authorization, files=files, data=json_req)
    return res.json()


def list_document(auth, dataset_id):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/document/list?kb_id={dataset_id}"
    json = {}
    res = requests.post(url=url, headers=authorization, json=json)
    return res.json()


def get_docs_info(auth, doc_ids):
    authorization = {"Authorization": auth}
    json_req = {"doc_ids": doc_ids}
    url = f"{HOST_ADDRESS}/v1/document/infos"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def parse_docs(auth, doc_ids):
    authorization = {"Authorization": auth}
    json_req = {"doc_ids": doc_ids, "run": 1}
    url = f"{HOST_ADDRESS}/v1/document/run"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def bulk_upload_documents(auth, dataset_id, num, tmp_path):
    # This is a stub implementation for bulk upload
    # In real tests, files should be created and uploaded
    document_ids = []
    for i in range(num):
        # Simulate upload of a document named ragflow_test_{i}.txt
        url = f"{HOST_ADDRESS}/v1/document/upload"
        headers = {"Authorization": auth}
        files = {"file": (f"ragflow_test_{i}.txt", b"Test content")}
        data = {"kb_id": dataset_id}
        res = requests.post(url=url, headers=headers, files=files, data=data)
        if res.status_code == 200 and "data" in res.json():
            document_ids.append(res.json()["data"][0]["id"])
    return document_ids


def add_chunk(auth, dataset_id, document_id, payload=None):
    url = f"{HOST_ADDRESS}/v1/datasets/{dataset_id}/documents/{document_id}/chunks"
    headers = {"Authorization": auth}
    res = requests.post(url=url, headers=headers, json=payload)
    return res.json()
