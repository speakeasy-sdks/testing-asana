"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from testing_2 import utils
from typing import Optional

class StatusUpdateRequestStatusType(str, Enum):
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
class StatusUpdateRequestInput:
    r"""A *status update* is an update on the progress of a particular project, portfolio, or goal, and is sent out to all of its parent's followers when created. These updates include both text describing the update and a `status_type` intended to represent the overall state of the project."""
    parent: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parent') }})
    status_type: StatusUpdateRequestStatusType = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_type') }})
    r"""The type associated with the status update. This represents the current state of the object this object is on."""
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    r"""The text content of the status update."""
    html_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_text'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). The text content of the status update with formatting as HTML."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the status update."""
    

