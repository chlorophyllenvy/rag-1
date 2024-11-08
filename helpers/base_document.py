

from pydantic import BaseModel, Field


class Document(BaseModel):
    """Interface for interacting with a document."""

    page_content: str
    metadata: dict = Field(default_factory=dict)

    def to_dict(self):
        return self.dict(by_alias=True, exclude_unset=True) # just an example!

    def to_json(self):
        print('here is self', self)
        return self.json(by_alias=True, exclude_unset=True) # just an example!

