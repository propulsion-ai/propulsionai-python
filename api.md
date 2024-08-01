# Chat

## Completions

Types:

```python
from propulsionai.types.chat import CompletionCreateResponse
```

Methods:

- <code title="post /chat/completions">client.chat.completions.<a href="./src/propulsionai/resources/chat/completions.py">create</a>(\*\*<a href="src/propulsionai/types/chat/completion_create_params.py">params</a>) -> <a href="./src/propulsionai/types/chat/completion_create_response.py">CompletionCreateResponse</a></code>

# Dataset

Types:

```python
from propulsionai.types import DatasetCreateResponse
```

Methods:

- <code title="post /dataset">client.dataset.<a href="./src/propulsionai/resources/dataset/dataset.py">create</a>(\*\*<a href="src/propulsionai/types/dataset_create_params.py">params</a>) -> <a href="./src/propulsionai/types/dataset_create_response.py">DatasetCreateResponse</a></code>

## Item

Types:

```python
from propulsionai.types.dataset import ItemCreateResponse
```

Methods:

- <code title="post /dataset/item">client.dataset.item.<a href="./src/propulsionai/resources/dataset/item.py">create</a>(\*\*<a href="src/propulsionai/types/dataset/item_create_params.py">params</a>) -> <a href="./src/propulsionai/types/dataset/item_create_response.py">ItemCreateResponse</a></code>

# Knowledgebase

Types:

```python
from propulsionai.types import Knowledgebase
```

Methods:

- <code title="post /knowledgebase">client.knowledgebase.<a href="./src/propulsionai/resources/knowledgebase/knowledgebase.py">create</a>(\*\*<a href="src/propulsionai/types/knowledgebase_create_params.py">params</a>) -> <a href="./src/propulsionai/types/knowledgebase/knowledgebase.py">Knowledgebase</a></code>

## File

Types:

```python
from propulsionai.types.knowledgebase import (
    File,
    KnowledgebaseFileUploadResponse,
    FileDeleteResponse,
)
```

Methods:

- <code title="post /knowledgebase/{knowledgebase_code}/file">client.knowledgebase.file.<a href="./src/propulsionai/resources/knowledgebase/file.py">create</a>(knowledgebase_code, \*\*<a href="src/propulsionai/types/knowledgebase/file_create_params.py">params</a>) -> <a href="./src/propulsionai/types/knowledgebase/file.py">File</a></code>
- <code title="delete /knowledgebase/{knowledgebase_code}/file/{file_id}">client.knowledgebase.file.<a href="./src/propulsionai/resources/knowledgebase/file.py">delete</a>(file_id, \*, knowledgebase_code) -> <a href="./src/propulsionai/types/knowledgebase/file_delete_response.py">FileDeleteResponse</a></code>
- <code title="post /knowledgebase/{knowledgebase_code}/file">client.knowledgebase.file.<a href="./src/propulsionai/resources/knowledgebase/file.py">upload</a>(knowledgebase_code, \*\*<a href="src/propulsionai/types/knowledgebase/file_upload_params.py">params</a>) -> <a href="./src/propulsionai/types/knowledgebase/file.py">File</a></code>

## Item

Types:

```python
from propulsionai.types.knowledgebase import KnowledgebaseItemResponse
```

Methods:

- <code title="post /knowledgebase/{knowledgebase_code}/item">client.knowledgebase.item.<a href="./src/propulsionai/resources/knowledgebase/item.py">create</a>(knowledgebase_code, \*\*<a href="src/propulsionai/types/knowledgebase/item_create_params.py">params</a>) -> <a href="./src/propulsionai/types/knowledgebase/knowledgebase_item_response.py">KnowledgebaseItemResponse</a></code>
