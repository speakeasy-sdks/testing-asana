"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import usercompact as shared_usercompact
from ..shared import usertasklistresponse as shared_usertasklistresponse
from ..shared import workspacecompact as shared_workspacecompact
from dataclasses_json import Undefined, dataclass_json
from testing_2 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WorkspaceMembershipResponseVacationDates:
    r"""Contains keys `start_on` and `end_on` for the vacation dates for the user in this workspace. If `start_on` is null, the entire `vacation_dates` object will be null. If `end_on` is before today, the entire `vacation_dates` object will be null."""
    end_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('end_on'), 'exclude': lambda f: f is None }})
    r"""The day on which the user's vacation in this workspace ends, or null if there is no end date. This is a date with `YYYY-MM-DD` format."""
    start_on: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_on'), 'exclude': lambda f: f is None }})
    r"""The day on which the user's vacation in this workspace starts. This is a date with `YYYY-MM-DD` format."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class WorkspaceMembershipResponse:
    r"""This object determines if a user is a member of a workspace."""
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    is_active: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_active'), 'exclude': lambda f: f is None }})
    r"""Reflects if this user still a member of the workspace."""
    is_admin: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_admin'), 'exclude': lambda f: f is None }})
    r"""Reflects if this user is an admin of the workspace."""
    is_guest: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_guest'), 'exclude': lambda f: f is None }})
    r"""Reflects if this user is a guest of the workspace."""
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    user: Optional[shared_usercompact.UserCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    user_task_list: Optional[shared_usertasklistresponse.UserTaskListResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_task_list'), 'exclude': lambda f: f is None }})
    vacation_dates: Optional[WorkspaceMembershipResponseVacationDates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('vacation_dates'), 'exclude': lambda f: f is None }})
    r"""Contains keys `start_on` and `end_on` for the vacation dates for the user in this workspace. If `start_on` is null, the entire `vacation_dates` object will be null. If `end_on` is before today, the entire `vacation_dates` object will be null."""
    workspace: Optional[shared_workspacecompact.WorkspaceCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('workspace'), 'exclude': lambda f: f is None }})
    

