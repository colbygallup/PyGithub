from datetime import datetime
from typing import Any, Dict

from github.GithubObject import CompletableGithubObject
from github.NamedUser import NamedUser


class DeploymentStatus(CompletableGithubObject):
    def __repr__(self) -> str: ...
    def _initAttributes(self) -> None: ...
    def _useAttributes(self, attributes: Dict[str, Any]) -> None: ...
    @property
    def created_at(self) -> datetime: ...
    @property
    def creator(self) -> NamedUser: ...
    @property
    def deployment_url(self) -> str: ...
    @property
    def description(self) -> str: ...
    @property
    def environment(self) -> str: ...
    @property
    def environment_url(self) -> str: ...
    @property
    def log_url(self) -> str: ...
    @property
    def repository_url(self) -> str: ...
    @property
    def state(self) -> str: ...
    @property
    def target_url(self) -> str: ...
    @property
    def updated_at(self) -> datetime: ...
    @property
    def url(self) -> str: ...
    @property
    def id(self) -> int: ...
    @property
    def node_id(self) -> str: ...
