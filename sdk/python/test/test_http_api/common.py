#
#  Copyright 2025 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#

import os

import requests

HOST_ADDRESS = os.getenv("HOST_ADDRESS", "http://127.0.0.1:9380")

DATASET_NAME_LIMIT = 128
CHAT_ASSISTANT_NAME_LIMIT = 128
INVALID_API_TOKEN = "invalid_token"


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

    file = {"file": open(f"{path}", "rb")}

    res = requests.post(url=url, headers=authorization, files=file, data=json_req)
    return res.json()


def list_document(auth, dataset_id):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/document/list?kb_id={dataset_id}"
    json = {}
    res = requests.post(url=url, headers=authorization, json=json)
    return res.json()


def list_documnets(auth, dataset_id, params=None):
    return list_document(auth, dataset_id)


def stop_parse_documents(auth, dataset_id, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/document/stop_parse"
    res = requests.post(url=url, headers=authorization, json=json_req)
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


def parse_file(auth, document_id):
    pass


def batch_create_datasets(auth, count):
    dataset_ids = []
    for i in range(count):
        dataset_name = f"test_dataset_{i}"
        res = create_dataset(auth, dataset_name)
        if res.get("code") == 0 and "data" in res and "id" in res["data"]:
            dataset_ids.append(res["data"]["id"])
        else:
            raise Exception(f"Failed to create dataset: {res}")
    return dataset_ids


def bulk_upload_documents(auth, dataset_id, count, tmp_dir):
    document_ids = []
    for i in range(count):
        file_path = tmp_dir / f"test_document_{i}.txt"
        with open(file_path, "w") as f:
            f.write(f"Test document content {i}")
        res = upload_file(auth, dataset_id, str(file_path))
        if res.get("code") == 0 and "data" in res and "id" in res["data"]:
            document_ids.append(res["data"]["id"])
        else:
            raise Exception(f"Failed to upload document: {res}")
    return document_ids


def create_chat_assistant(auth, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def batch_create_chat_assistants(auth, count):
    chat_assistant_ids = []
    for i in range(count):
        json_req = {"name": f"test_chat_assistant_{i}", "dataset_ids": []}
        res = create_chat_assistant(auth, json_req)
        if res.get("code") == 0 and "data" in res and "id" in res["data"]:
            chat_assistant_ids.append(res["data"]["id"])
        else:
            raise Exception(f"Failed to create chat assistant: {res}")
    return chat_assistant_ids


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


def delete_datasets(auth, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/kb/rm"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def delete_session_with_chat_assistants(auth, chat_assistant_id):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats/{chat_assistant_id}/sessions"
    res = requests.delete(url=url, headers=authorization)
    return res.json()


def create_session_with_chat_assistant(auth, chat_assistant_id, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats/{chat_assistant_id}/sessions"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def add_chunk(auth, dataset_id, document_id, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chunk/add"
    json_req.update({"dataset_id": dataset_id, "document_id": document_id})
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def delete_chunks(auth, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chunk/rm"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def delete_documents(auth, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/document/rm"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def update_chat_assistant(auth, chat_assistant_id, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats/{chat_assistant_id}"
    res = requests.put(url=url, headers=authorization, json=json_req)
    return res.json()


def list_datasets(auth):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/kb/list"
    res = requests.get(url=url, headers=authorization)
    return res.json()


def batch_add_chunks(auth, dataset_id, document_id, chunks):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chunk/add_batch"
    json_req = {"dataset_id": dataset_id, "document_id": document_id, "chunks": chunks}
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def retrieval_chunks(auth, dataset_id, query):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chunk/retrieval"
    json_req = {"dataset_id": dataset_id, "query": query}
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def update_chunk(auth, chunk_id, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chunk/{chunk_id}"
    res = requests.put(url=url, headers=authorization, json=json_req)
    return res.json()


def update_documnet(auth, doc_id, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/document/update"
    json_req.update({"doc_id": doc_id})
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


DOCUMENT_NAME_LIMIT = 128
FILE_API_URL = f"{HOST_ADDRESS}/v1/document"


def upload_documents(auth, dataset_id, files):
    authorization = {"Authorization": auth}
    url = f"{FILE_API_URL}/upload"
    res = requests.post(url=url, headers=authorization, files=files, data={"kb_id": dataset_id})
    return res.json()


def upload_documnets(auth, dataset_id, files):
    return upload_documents(auth, dataset_id, files)


def list_documents(auth, dataset_id):
    authorization = {"Authorization": auth}
    url = f"{FILE_API_URL}/list?kb_id={dataset_id}"
    json = {}
    res = requests.post(url=url, headers=authorization, json=json)
    return res.json()


def delete_documents(auth, json_req):
    authorization = {"Authorization": auth}
    url = f"{FILE_API_URL}/rm"
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def download_document(auth, doc_id):
    authorization = {"Authorization": auth}
    url = f"{FILE_API_URL}/get/{doc_id}"
    res = requests.get(url=url, headers=authorization)
    return res.content


def upload_documents(auth, dataset_id, files):
    authorization = {"Authorization": auth}
    url = f"{FILE_API_URL}/upload"
    res = requests.post(url=url, headers=authorization, files=files, data={"kb_id": dataset_id})
    return res.json()


def list_documents(auth, dataset_id):
    authorization = {"Authorization": auth}
    url = f"{FILE_API_URL}/list?kb_id={dataset_id}"
    json = {}
    res = requests.post(url=url, headers=authorization, json=json)
    return res.json()


SESSION_WITH_CHAT_NAME_LIMIT = 128


def batch_add_sessions_with_chat_assistant(auth, chat_assistant_id, sessions):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats/{chat_assistant_id}/sessions/batch_add"
    json_req = {"sessions": sessions}
    res = requests.post(url=url, headers=authorization, json=json_req)
    return res.json()


def list_session_with_chat_assistants(auth, chat_assistant_id):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats/{chat_assistant_id}/sessions"
    res = requests.get(url=url, headers=authorization)
    return res.json()


def update_session_with_chat_assistant(auth, chat_assistant_id, session_id, json_req):
    authorization = {"Authorization": auth}
    url = f"{HOST_ADDRESS}/v1/chats/{chat_assistant_id}/sessions/{session_id}"
    res = requests.put(url=url, headers=authorization, json=json_req)
    return res.json()
