"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import usercompact as shared_usercompact
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from enum import Enum
from marshmallow import fields
from testing_2 import utils
from typing import Optional

class ProjectRequestColor(str, Enum):
    r"""Color of the project."""
    DARK_PINK = 'dark-pink'
    DARK_GREEN = 'dark-green'
    DARK_BLUE = 'dark-blue'
    DARK_RED = 'dark-red'
    DARK_TEAL = 'dark-teal'
    DARK_BROWN = 'dark-brown'
    DARK_ORANGE = 'dark-orange'
    DARK_PURPLE = 'dark-purple'
    DARK_WARM_GRAY = 'dark-warm-gray'
    LIGHT_PINK = 'light-pink'
    LIGHT_GREEN = 'light-green'
    LIGHT_BLUE = 'light-blue'
    LIGHT_RED = 'light-red'
    LIGHT_TEAL = 'light-teal'
    LIGHT_BROWN = 'light-brown'
    LIGHT_ORANGE = 'light-orange'
    LIGHT_PURPLE = 'light-purple'
    LIGHT_WARM_GRAY = 'light-warm-gray'

class ProjectRequestCurrentStatusColor(str, Enum):
    r"""The color associated with the status update."""
    GREEN = 'green'
    YELLOW = 'yellow'
    RED = 'red'
    BLUE = 'blue'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ProjectRequestCurrentStatusInput:
    r"""*Deprecated: new integrations should prefer the `status_update` resource.*
    A *project status* is an update on the progress of a particular project, and is sent out to all project followers when created. These updates include both text describing the update and a color code intended to represent the overall state of the project: \"green\" for projects that are on track, \"yellow\" for projects at risk, and \"red\" for projects that are behind.
    """
    color: ProjectRequestCurrentStatusColor = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color') }})
    r"""The color associated with the status update."""
    text: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text') }})
    r"""The text content of the status update."""
    author: Optional[shared_usercompact.UserCompactInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('author'), 'exclude': lambda f: f is None }})
    created_by: Optional[shared_usercompact.UserCompactInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by'), 'exclude': lambda f: f is None }})
    html_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_text'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). The text content of the status update with formatting as HTML."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the project status update."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ProjectRequestCurrentStatusUpdateInput:
    r"""A *status update* is an update on the progress of a particular project, portfolio, or goal, and is sent out to all of its parent's followers when created. These updates include both text describing the update and a `status_type` intended to represent the overall state of the project."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the status update."""
    


class ProjectRequestDefaultView(str, Enum):
    r"""The default view (list, board, calendar, or timeline) of a project."""
    LIST = 'list'
    BOARD = 'board'
    CALENDAR = 'calendar'
    TIMELINE = 'timeline'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ProjectRequestWorkspaceInput:
    r"""A *workspace* is the highest-level organizational unit in Asana. All projects and tasks have an associated workspace."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the workspace."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class ProjectRequestInput:
    r"""A *project* represents a prioritized list of tasks in Asana or a board with columns of tasks represented as cards. It exists in a single workspace or organization and is accessible to a subset of users in that workspace or organization, depending on its permissions."""
    archived: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('archived'), 'exclude': lambda f: f is None }})
    r"""True if the project is archived, false if not. Archived projects do not show in the UI by default and may be treated differently for queries."""
    color: Optional[ProjectRequestColor] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('color'), 'exclude': lambda f: f is None }})
    r"""Color of the project."""
    current_status: Optional[ProjectRequestCurrentStatusInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_status'), 'exclude': lambda f: f is None }})
    r"""*Deprecated: new integrations should prefer the `current_status_update` resource.*"""
    current_status_update: Optional[ProjectRequestCurrentStatusUpdateInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_status_update'), 'exclude': lambda f: f is None }})
    r"""The latest `status_update` posted to this project."""
    custom_fields: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_fields'), 'exclude': lambda f: f is None }})
    r"""An object where each key is a Custom Field GID and each value is an enum GID, string, number, or object."""
    default_view: Optional[ProjectRequestDefaultView] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('default_view'), 'exclude': lambda f: f is None }})
    r"""The default view (list, board, calendar, or timeline) of a project."""
    due_date: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_date'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""*Deprecated: new integrations should prefer the `due_on` field.*"""
    due_on: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_on'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The day on which this project is due. This takes a date with format YYYY-MM-DD."""
    followers: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('followers'), 'exclude': lambda f: f is None }})
    r"""*Create-only*. Comma separated string of users. Followers are a subset of members who have opted in to receive \\"tasks added\\" notifications for a project."""
    html_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_notes'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). The notes of the project with formatting as HTML."""
    is_template: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_template'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). *Deprecated - please use a project template endpoint instead (more in [this forum post](https://forum.asana.com/t/a-new-api-for-project-templates/156432)).* Determines if the project is a template."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""Name of the project. This is generally a short sentence fragment that fits on a line in the UI for maximum readability. However, it can be longer."""
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Free-form textual information associated with the project (ie., its description)."""
    owner: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('owner'), 'exclude': lambda f: f is None }})
    r"""The current owner of the project, may be null."""
    public: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public'), 'exclude': lambda f: f is None }})
    r"""True if the project is public to its team."""
    start_on: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_on'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The day on which work for this project begins, or null if the project has no start date. This takes a date with `YYYY-MM-DD` format. *Note: `due_on` or `due_at` must be present in the request when setting or unsetting the `start_on` parameter. Additionally, `start_on` and `due_on` cannot be the same date.*"""
    team: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('team'), 'exclude': lambda f: f is None }})
    r"""The team that this project is shared with."""
    workspace: Optional[ProjectRequestWorkspaceInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace'), 'exclude': lambda f: f is None }})
    
