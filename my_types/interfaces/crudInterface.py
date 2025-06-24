from abc import ABC, abstractmethod
from typing import Optional, List, TypeVar, Generic

CreateDTO = TypeVar('CreateDTO')
UpdateDTO = TypeVar('UpdateDTO')
ReturnDTO = TypeVar('ReturnDTO')
LoadedReturnDTO = TypeVar('LoadedReturnDTO')
IDType = TypeVar('IDType')

class CrudInterface(ABC, Generic[CreateDTO, UpdateDTO, IDType]):
    @abstractmethod
    def create(self, data: CreateDTO) -> ReturnDTO:
        pass

    @abstractmethod
    def read(self, id: IDType) -> Optional[LoadedReturnDTO]:
        pass

    @abstractmethod
    def update(self, id: IDType, data: UpdateDTO) -> ReturnDTO:
        pass

    @abstractmethod
    def delete(self, id: IDType) -> None:
        pass

    @abstractmethod
    def list_all(self) -> List[ReturnDTO]:
        pass