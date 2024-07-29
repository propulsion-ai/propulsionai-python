import sys  # type: ignore
import json  # type: ignore
from pathlib import Path
from propulsionai import PropulsionAI

client = PropulsionAI(
    # This is the default and can be omitted
    bearer_token="UFJPRFVDVElPTiQxNDEkRDlYNzEySFg0M0ZaMzI4UUFUOUNNWkQ3REs3MTRa",
    # base_url="https://npapi.propulsionhq.com/api/v2",
    base_url="http://localhost:2999/api/v2",
)


def sync_main() -> None:
    knowledgebase = client.knowledgebase.create(name="weather", description="A knowledgebase for weather", tags="uppto")
    print(f"Knowledgebase created with id: ", knowledgebase.id)
    # read ./12025248.pdf and convert it to bytes
    file_path = Path('examples/12025248.pdf')
    if knowledgebase.id:
      with open(file_path, 'rb') as f:
          file_bytes = f.read()
          upload_file_response = client.knowledgebase.file.upload(
              knowledgebase_id=knowledgebase.id,
              file=file_bytes
          )
          print(f"File uploaded with id: ", upload_file_response.id)
      if upload_file_response.id:
         # delete the file
          delete_file_response = client.knowledgebase.file.delete(knowledgebase_id=knowledgebase.id, file_id=upload_file_response.id);
          print(f"File deleted with id: ", delete_file_response.id)



sync_main()
