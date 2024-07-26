import os

from propulsionai import PropulsionAI

client = PropulsionAI(
    # This is the default and can be omitted
    bearer_token=os.environ.get("PROPULSIONAI_BEARER_TOKEN"),
)

def sync_main() -> None:
    response = client.dataset.item.create(
        dataset_id=0,
        data={
            "prompt": "Hello, How are you?",
            "response": "I'm fine, thank you.",
        }
    )
    
    print(response.id)


sync_main()