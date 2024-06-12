import os
from typing import Any, Dict, Callable, Coroutine

from propulsionai import PropulsionAI

# from typing import Dict, Any, Coroutine

p8n = PropulsionAI(
    bearer_token=os.environ.get("PROPULSIONAI_BEARER_TOKEN"),
)


async def mongo_query(parameters: object) -> str:
    # Here you would normally use the parameters to form your query
    # For this example, we are returning a hardcoded response
    print(parameters)

    result = """["total_sales" = 100]"""

    return result


# Function map to map the function name to the actual function
available_function_map: Dict[str, Callable[..., Coroutine[Any, Any, str]]] = {
    "mongo_query": mongo_query,
}


async def main() -> None:
    model_chat_response = await p8n.models.chat_auto(
        "khzhgybzctm6e8m",
        tool_choice="auto",
        available_function_map=available_function_map,
        tools=[
            {
                "type": "function",
                "function": {
                    "name": "mongo_query",
                    "description": "Write a MongoDB for aggregating data.",
                    "function": "mongo_query",
                    "parameters": {
                        "collection": {
                            "type": "string",
                            "description": "Name of the collection to query",
                        },
                        "aggregate": {
                            "type": "array",
                            "description": "Array of aggregation stages",
                        },
                    },
                },
            },
        ],
        messages=[
            {
                "role": "system",
                "content": """
                You are a helpful coder - MongoDB Expert
                here is the transaction collection schema:
                {
                  _id: ObjectId,
                  user_id: ObjectId,
                  amount: Number,
                  date: Date
                  type: Enum('sales', 'refund', 'chargeback', 'dispute')
                }
                My user_id is '60b9b3b3e4b0b3b3b3b3b3b3'
            """,
            },
            {
                "role": "user",
                "content": "What are my total sales for 2022",
            },
        ],
        model="khzhgybzctm6e8m",
        wait=True,
        stream=False,
    )
    print(model_chat_response.id)
    print(model_chat_response)


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
