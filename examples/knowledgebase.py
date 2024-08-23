import os
from pathlib import Path

from propulsionai import PropulsionAI

client = PropulsionAI(
    # This is the default and can be omitted
    bearer_token=os.environ.get("PROPULSIONAI_BEARER_TOKEN"),
)


def sync_kb() -> None:
    knowledgebase = client.knowledgebase.create(name="weather", description="A knowledgebase for weather", tags="uppto")
    print(f"Knowledgebase created with id: ", knowledgebase.code)
    # read ./12025248.pdf and convert it to bytes
    file_path = Path("examples/12025248.pdf")
    if knowledgebase.code:
        with open(file_path, "rb") as f:
            file_bytes = f.read()
            upload_file_response = client.knowledgebase.file.upload(
                knowledgebase_code=knowledgebase.code, file=file_bytes
            )
            print(f"File uploaded with id: ", upload_file_response.id)
        if upload_file_response.id:
            # delete the file
            delete_file_response = client.knowledgebase.file.delete(
                knowledgebase_code=knowledgebase.code, file_id=upload_file_response.id
            )
            print(f"File deleted with id: ", delete_file_response.id)

def sync_main() -> None:
    response = client.chat.completions.create(
        deployment="<deployment_id>",
        knowledgebases=["<knowledgebase_id_1>","<knowledgebase_id_2>"],
        messages=[
            {
                "role": "user",
                "content": "Hello, How are you?",
            }
        ],
        stream=False,
    )

    print(response)

    stream = client.chat.completions.create(
        deployment="<deployment_id>",
        knowledgebases=["<knowledgebase_id_1>","<knowledgebase_id_2>"],
        messages=[
            {
                "role": "user",
                "content": "Hello, How are you?",
            }
        ],
        stream=True,
    )
    # print(response)
    first = next(stream)
    print(f"got response data: {first.to_json()}")

    for data in stream:
        print(data.to_json())

sync_main()
