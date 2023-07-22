"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from testing_2 import utils
from typing import Optional

class AuditLogEventActorActorType(str, Enum):
    r"""The type of actor.
    Can be one of `user`, `asana`, `asana_support`, `anonymous`, or `external_administrator`.
    """
    USER = 'user'
    ASANA = 'asana'
    ASANA_SUPPORT = 'asana_support'
    ANONYMOUS = 'anonymous'
    EXTERNAL_ADMINISTRATOR = 'external_administrator'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AuditLogEventActor:
    r"""The entity that triggered the event. Will typically be a user."""
    actor_type: Optional[AuditLogEventActorActorType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actor_type'), 'exclude': lambda f: f is None }})
    r"""The type of actor.
    Can be one of `user`, `asana`, `asana_support`, `anonymous`, or `external_administrator`.
    """
    email: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('email'), 'exclude': lambda f: f is None }})
    r"""The email of the actor, if it is a user."""
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the actor, if it is a user."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the actor, if it is a user."""
    

