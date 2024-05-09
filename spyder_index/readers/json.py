from pathlib import Path
from typing import List, Optional
from pydantic import BaseModel, Field

from spyder_index.core.document import Document

from langchain_community.document_loaders import JSONLoader

class JSONReader(BaseModel):
    jq_schema: str = Field(default="")
    text_content: bool = Field(default=False)

    def load_data(self, input_file: Path, extra_info: Optional[dict] = None) -> List[Document]: 

        loader = JSONLoader(file_path=input_file,
                            jq_schema=self.jq_schema,
                            text_content=self.text_content)
        
        langchain_documents = loader.load()

        return [Document()._from_langchain_format(doc=doc) for doc in langchain_documents]