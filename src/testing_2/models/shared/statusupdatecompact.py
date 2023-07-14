"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from testing_2 import utils
from typing import Optional

class StatusUpdateCompactResourceSubtype(str, Enum):
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.
    The `resource_subtype`s for `status` objects represent the type of their parent.
    """
    PROJECT_STATUS_UPDATE = 'project_status_update'
    PORTFOLIO_STATUS_UPDATE = 'portfolio_status_update'
    GOAL_STATUS_UPDATE = 'goal_status_update'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StatusUpdateCompact:
    r"""A *status update* is an update on the progress of a particular project, portfolio, or goal, and is sent out to all of its parent's followers when created. These updates include both text describing the update and a `status_type` intended to represent the overall state of the project."""
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    resource_subtype: Optional[StatusUpdateCompactResourceSubtype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_subtype'), 'exclude': lambda f: f is None }})
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.
    The `resource_subtype`s for `status` objects represent the type of their parent.
    """
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the status update."""
    
