"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import usercompact as shared_usercompact
from dataclasses_json import Undefined, dataclass_json
from datetime import date
from enum import Enum
from marshmallow import fields
from testing_2 import utils
from typing import Optional

class TaskRequestApprovalStatus(str, Enum):
    r"""*Conditional* Reflects the approval status of this task. This field is kept in sync with `completed`, meaning `pending` translates to false while `approved`, `rejected`, and `changes_requested` translate to true. If you set completed to true, this field will be set to `approved`."""
    PENDING = 'pending'
    APPROVED = 'approved'
    REJECTED = 'rejected'
    CHANGES_REQUESTED = 'changes_requested'

class TaskRequestAssigneeStatus(str, Enum):
    r"""*Deprecated* Scheduling status of this task for the user it is assigned to. This field can only be set if the assignee is non-null. Setting this field to \\"inbox\\" or \\"upcoming\\" inserts it at the top of the section, while the other options will insert at the bottom."""
    TODAY = 'today'
    UPCOMING = 'upcoming'
    LATER = 'later'
    NEW = 'new'
    INBOX = 'inbox'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskRequestExternal:
    r"""*OAuth Required*. *Conditional*. This field is returned only if external values are set or included by using [Opt In] (/docs/input-output-options).
    The external field allows you to store app-specific metadata on tasks, including a gid that can be used to retrieve tasks and a data blob that can store app-specific character strings. Note that you will need to authenticate with Oauth to access or modify this data. Once an external gid is set, you can use the notation `external:custom_gid` to reference your object anywhere in the API where you may use the original object gid. See the page on Custom External Data for more details.
    """
    data: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    


class TaskRequestResourceSubtype(str, Enum):
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.
    The resource_subtype `milestone` represent a single moment in time. This means tasks with this subtype cannot have a start_date.
    """
    DEFAULT_TASK = 'default_task'
    MILESTONE = 'milestone'
    SECTION = 'section'
    APPROVAL = 'approval'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TaskRequestInput:
    r"""The *task* is the basic object around which many operations in Asana are centered."""
    approval_status: Optional[TaskRequestApprovalStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('approval_status'), 'exclude': lambda f: f is None }})
    r"""*Conditional* Reflects the approval status of this task. This field is kept in sync with `completed`, meaning `pending` translates to false while `approved`, `rejected`, and `changes_requested` translate to true. If you set completed to true, this field will be set to `approved`."""
    assignee: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignee'), 'exclude': lambda f: f is None }})
    r"""Gid of a user."""
    assignee_section: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignee_section'), 'exclude': lambda f: f is None }})
    r"""The *assignee section* is a subdivision of a project that groups tasks together in the assignee's \\"My Tasks\\" list. It can either be a header above a list of tasks in a list view or a column in a board view of \\"My Tasks.\\" 
    The `assignee_section` property will be returned in the response only if the request was sent by the user who is the assignee of the task. Note that you can only write to `assignee_section` with the gid of an existing section visible in the user's \"My Tasks\" list.
    """
    assignee_status: Optional[TaskRequestAssigneeStatus] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignee_status'), 'exclude': lambda f: f is None }})
    r"""*Deprecated* Scheduling status of this task for the user it is assigned to. This field can only be set if the assignee is non-null. Setting this field to \\"inbox\\" or \\"upcoming\\" inserts it at the top of the section, while the other options will insert at the bottom."""
    completed: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completed'), 'exclude': lambda f: f is None }})
    r"""True if the task is currently marked complete, false if not."""
    completed_by: Optional[shared_usercompact.UserCompactInput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('completed_by'), 'exclude': lambda f: f is None }})
    custom_fields: Optional[dict[str, str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_fields'), 'exclude': lambda f: f is None }})
    r"""An object where each key is a Custom Field GID and each value is an enum GID, string, number, object, or array."""
    due_at: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_at'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with `due_on`."""
    due_on: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_on'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The localized date on which this task is due, or null if the task has no due date. This takes a date with `YYYY-MM-DD` format and should not be used together with `due_at`."""
    external: Optional[TaskRequestExternal] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('external'), 'exclude': lambda f: f is None }})
    r"""*OAuth Required*. *Conditional*. This field is returned only if external values are set or included by using [Opt In] (/docs/input-output-options).
    The external field allows you to store app-specific metadata on tasks, including a gid that can be used to retrieve tasks and a data blob that can store app-specific character strings. Note that you will need to authenticate with Oauth to access or modify this data. Once an external gid is set, you can use the notation `external:custom_gid` to reference your object anywhere in the API where you may use the original object gid. See the page on Custom External Data for more details.
    """
    followers: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('followers'), 'exclude': lambda f: f is None }})
    r"""*Create-Only* An array of strings identifying users. These can either be the string \\"me\\", an email, or the gid of a user. In order to change followers on an existing task use `addFollowers` and `removeFollowers`."""
    html_notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_notes'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). The notes of the text with formatting as HTML."""
    liked: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('liked'), 'exclude': lambda f: f is None }})
    r"""True if the task is liked by the authorized user, false if not."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the task."""
    notes: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('notes'), 'exclude': lambda f: f is None }})
    r"""Free-form textual information associated with the task (i.e. its description)."""
    parent: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('parent'), 'exclude': lambda f: f is None }})
    r"""Gid of a task."""
    projects: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('projects'), 'exclude': lambda f: f is None }})
    r"""*Create-Only* Array of project gids. In order to change projects on an existing task use `addProject` and `removeProject`."""
    resource_subtype: Optional[TaskRequestResourceSubtype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_subtype'), 'exclude': lambda f: f is None }})
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.
    The resource_subtype `milestone` represent a single moment in time. This means tasks with this subtype cannot have a start_date.
    """
    start_at: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_at'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""Date and time on which work begins for the task, or null if the task has no start time. This takes an ISO 8601 date string in UTC and should not be used together with `start_on`.
    *Note: `due_at` must be present in the request when setting or unsetting the `start_at` parameter.*
    """
    start_on: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_on'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The day on which work begins for the task , or null if the task has no start date. This takes a date with `YYYY-MM-DD` format and should not be used together with `start_at`.
    *Note: `due_on` or `due_at` must be present in the request when setting or unsetting the `start_on` parameter.*
    """
    tags: Optional[list[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tags'), 'exclude': lambda f: f is None }})
    r"""*Create-Only* Array of tag gids. In order to change tags on an existing task use `addTag` and `removeTag`."""
    workspace: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace'), 'exclude': lambda f: f is None }})
    r"""Gid of a workspace."""
    

