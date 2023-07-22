"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import usercompact as shared_usercompact
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from enum import Enum
from marshmallow import fields
from testing_2 import utils
from typing import Optional

class ProjectStatusResponseColor(str, Enum):
    r"""The color associated with the status update."""
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'
    BLUE = 'blue'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ProjectStatusResponse:
    r"""*Deprecated: new integrations should prefer the `status_update` resource.*
    A *project status* is an update on the progress of a particular project, and is sent out to all project followers when created. These updates include both text describing the update and a color code intended to represent the overall state of the project: \"green\" for projects that are on track, \"yellow\" for projects at risk, and \"red\" for projects that are behind.
    """
    color: ProjectStatusResponseColor = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color') }})
    r"""The color associated with the status update."""
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    r"""The text content of the status update."""
    author: Optional[shared_usercompact.UserCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('author'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The time at which this resource was created."""
    created_by: Optional[shared_usercompact.UserCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by'), 'exclude': lambda f: f is None }})
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    html_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_text'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). The text content of the status update with formatting as HTML."""
    modified_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modified_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The time at which this project status was last modified.
    *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the project status.*
    """
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the project status update."""
    

