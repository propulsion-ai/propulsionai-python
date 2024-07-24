import os
from propulsionai import PropulsionAI

client = PropulsionAI(
    # This is the default and can be omitted
    bearer_token=os.environ.get("PROPULSIONAI_BEARER_TOKEN"),
)

def sync_main() -> None:
    response = client.chat.completions.create(
        deployment="<deployment_id>",
        messages=[{
            "role": "user",
            "content": "Hello, How are you?",
        }],
        stream=True,
    )
    # print(response)
    first = next(response)
    print(f"got response data: {first.to_json()}")
    
    for data in response:
        print(data.to_json())


sync_main()