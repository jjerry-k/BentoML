from abc import ABC, abstractmethod
from typing import TypeVar

from ..types import HTTPRequest, HTTPResponse

IOPyObj = TypeVar("IOPyObj")


class IODescriptor(ABC):
    """IODescriptor describes the input/output data format of an InferenceAPI defined
    in a bentoml.Service
    """

    @abstractmethod
    def openapi_schema(self):
        pass

    @abstractmethod
    def from_http_request(self, request: HTTPRequest) -> IOPyObj:
        pass

    @abstractmethod
    def to_http_response(self, obj: IOPyObj) -> HTTPResponse:
        pass