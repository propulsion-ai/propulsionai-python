# Models

Types:

```python
from propulsionai.types import ModelChatResponse, ModelEpResponse
```

Methods:

- <code title="post /api/v1/{model_id}/run">client.models.<a href="./src/propulsionai/resources/models.py">chat</a>(model_id, \*\*<a href="src/propulsionai/types/model_chat_params.py">params</a>) -> <a href="./src/propulsionai/types/model_chat_response.py">ModelChatResponse</a></code>
- <code title="post /api/v1/chat/{deployment_tag}">client.models.<a href="./src/propulsionai/resources/models.py">ep</a>(deployment_tag, \*\*<a href="src/propulsionai/types/model_ep_params.py">params</a>) -> <a href="./src/propulsionai/types/model_ep_response.py">ModelEpResponse</a></code>

# Datasets

## Tasks

Methods:

- <code title="post /api/v1/dataset/{dataset_id}/task">client.datasets.tasks.<a href="./src/propulsionai/resources/datasets/tasks.py">create</a>(dataset_id, \*\*<a href="src/propulsionai/types/datasets/task_create_params.py">params</a>) -> None</code>
