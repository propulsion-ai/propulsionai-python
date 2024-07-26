import os

from propulsionai import PropulsionAI

client = PropulsionAI(
    # This is the default and can be omitted
    bearer_token=os.environ.get("PROPULSIONAI_BEARER_TOKEN"),
)

def sync_main() -> None:
    response = client.dataset.create(
        name="My Dataset"
    )
    
    print(response.id)


sync_main()