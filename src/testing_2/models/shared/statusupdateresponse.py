"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import like as shared_like
from ..shared import usercompact as shared_usercompact
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from testing_2 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StatusUpdateResponseParent:
    r"""A *project* represents a prioritized list of tasks in Asana or a board with columns of tasks represented as cards. It exists in a single workspace or organization and is accessible to a subset of users in that workspace or organization, depending on its permissions."""
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer."""
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    


class StatusUpdateResponseResourceSubtype(str, Enum):
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.
    The `resource_subtype`s for `status` objects represent the type of their parent.
    """
    PROJECT_STATUS_UPDATE = 'project_status_update'
    PORTFOLIO_STATUS_UPDATE = 'portfolio_status_update'
    GOAL_STATUS_UPDATE = 'goal_status_update'

class StatusUpdateResponseStatusType(str, Enum):
    r"""The type associated with the status update. This represents the current state of the object this object is on."""
    ON_TRACK = 'on_track'
    AT_RISK = 'at_risk'
    OFF_TRACK = 'off_track'
    ON_HOLD = 'on_hold'
    COMPLETE = 'complete'
    ACHIEVED = 'achieved'
    PARTIAL = 'partial'
    MISSED = 'missed'
    DROPPED = 'dropped'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StatusUpdateResponse:
    r"""A *status update* is an update on the progress of a particular project, portfolio, or goal, and is sent out to all of its parent's followers when created. These updates include both text describing the update and a `status_type` intended to represent the overall state of the project."""
    status_type: StatusUpdateResponseStatusType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_type') }})
    r"""The type associated with the status update. This represents the current state of the object this object is on."""
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    r"""The text content of the status update."""
    author: Optional[shared_usercompact.UserCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('author'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The time at which this resource was created."""
    created_by: Optional[shared_usercompact.UserCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by'), 'exclude': lambda f: f is None }})
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    hearted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hearted'), 'exclude': lambda f: f is None }})
    r"""*Deprecated - please use liked instead* True if the status is hearted by the authorized user, false if not."""
    hearts: Optional[list[shared_like.Like]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hearts'), 'exclude': lambda f: f is None }})
    r"""*Deprecated - please use likes instead* Array of likes for users who have hearted this status."""
    html_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_text'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). The text content of the status update with formatting as HTML."""
    liked: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('liked'), 'exclude': lambda f: f is None }})
    r"""True if the status is liked by the authorized user, false if not."""
    likes: Optional[list[shared_like.Like]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('likes'), 'exclude': lambda f: f is None }})
    r"""Array of likes for users who have liked this status."""
    modified_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modified_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The time at which this project status was last modified.
    *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the status.*
    """
    num_hearts: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_hearts'), 'exclude': lambda f: f is None }})
    r"""*Deprecated - please use likes instead* The number of users who have hearted this status."""
    num_likes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_likes'), 'exclude': lambda f: f is None }})
    r"""The number of users who have liked this status."""
    parent: Optional[StatusUpdateResponseParent] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parent'), 'exclude': lambda f: f is None }})
    resource_subtype: Optional[StatusUpdateResponseResourceSubtype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_subtype'), 'exclude': lambda f: f is None }})
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.
    The `resource_subtype`s for `status` objects represent the type of their parent.
    """
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the status update."""
    

