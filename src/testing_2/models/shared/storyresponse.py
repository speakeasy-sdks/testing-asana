"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import dateutil.parser
from ..shared import customfieldcompact as shared_customfieldcompact
from ..shared import enumoption as shared_enumoption
from ..shared import like as shared_like
from ..shared import preview as shared_preview
from ..shared import projectcompact as shared_projectcompact
from ..shared import sectioncompact as shared_sectioncompact
from ..shared import storycompact as shared_storycompact
from ..shared import storyresponsedates as shared_storyresponsedates
from ..shared import tagcompact as shared_tagcompact
from ..shared import taskcompact as shared_taskcompact
from ..shared import usercompact as shared_usercompact
from dataclasses_json import Undefined, dataclass_json
from datetime import date, datetime
from enum import Enum
from marshmallow import fields
from testing_2 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StoryResponseNewDateValue:
    r"""*Conditional* The new value of a date custom field story."""
    due_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with `due_on`."""
    due_on: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_on'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The localized day on which this goal is due. This takes a date with format `YYYY-MM-DD`."""
    start_on: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_on'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The day on which work for this goal begins, or null if the goal has no start date. This takes a date with `YYYY-MM-DD` format, and cannot be set unless there is an accompanying due date."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StoryResponseOldDateValue:
    r"""*Conditional*. The old value of a date custom field story."""
    due_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The UTC date and time on which this task is due, or null if the task has no due time. This takes an ISO 8601 date string in UTC and should not be used together with `due_on`."""
    due_on: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('due_on'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The localized day on which this goal is due. This takes a date with format `YYYY-MM-DD`."""
    start_on: Optional[date] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('start_on'), 'encoder': utils.dateisoformat(True), 'decoder': utils.datefromisoformat, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The day on which work for this goal begins, or null if the goal has no start date. This takes a date with `YYYY-MM-DD` format, and cannot be set unless there is an accompanying due date."""
    


class StoryResponseSource(str, Enum):
    r"""The component of the Asana product the user used to trigger the story."""
    WEB = 'web'
    EMAIL = 'email'
    MOBILE = 'mobile'
    API = 'api'
    UNKNOWN = 'unknown'

class StoryResponseStickerName(str, Enum):
    r"""The name of the sticker in this story. `null` if there is no sticker."""
    GREEN_CHECKMARK = 'green_checkmark'
    PEOPLE_DANCING = 'people_dancing'
    DANCING_UNICORN = 'dancing_unicorn'
    HEART = 'heart'
    PARTY_POPPER = 'party_popper'
    PEOPLE_WAVING_FLAGS = 'people_waving_flags'
    SPLASHING_NARWHAL = 'splashing_narwhal'
    TROPHY = 'trophy'
    YETI_RIDING_UNICORN = 'yeti_riding_unicorn'
    CELEBRATING_PEOPLE = 'celebrating_people'
    DETERMINED_CLIMBERS = 'determined_climbers'
    PHOENIX_SPREADING_LOVE = 'phoenix_spreading_love'

class StoryResponseTargetResourceSubtype(str, Enum):
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.
    The resource_subtype `milestone` represent a single moment in time. This means tasks with this subtype cannot have a start_date.
    """
    DEFAULT_TASK = 'default_task'
    MILESTONE = 'milestone'
    SECTION = 'section'
    APPROVAL = 'approval'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StoryResponseTarget:
    r"""The *task* is the basic object around which many operations in Asana are centered."""
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the task."""
    resource_subtype: Optional[StoryResponseTargetResourceSubtype] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_subtype'), 'exclude': lambda f: f is None }})
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning.
    The resource_subtype `milestone` represent a single moment in time. This means tasks with this subtype cannot have a start_date.
    """
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    


class StoryResponseType(str, Enum):
    COMMENT = 'comment'
    SYSTEM = 'system'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class StoryResponse:
    r"""A story represents an activity associated with an object in the Asana system."""
    assignee: Optional[shared_usercompact.UserCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('assignee'), 'exclude': lambda f: f is None }})
    created_at: Optional[datetime] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_at'), 'encoder': utils.datetimeisoformat(True), 'decoder': dateutil.parser.isoparse, 'mm_field': fields.DateTime(format='iso'), 'exclude': lambda f: f is None }})
    r"""The time at which this resource was created."""
    created_by: Optional[shared_usercompact.UserCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('created_by'), 'exclude': lambda f: f is None }})
    custom_field: Optional[shared_customfieldcompact.CustomFieldCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_field'), 'exclude': lambda f: f is None }})
    dependency: Optional[shared_taskcompact.TaskCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dependency'), 'exclude': lambda f: f is None }})
    duplicate_of: Optional[shared_taskcompact.TaskCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duplicate_of'), 'exclude': lambda f: f is None }})
    duplicated_from: Optional[shared_taskcompact.TaskCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('duplicated_from'), 'exclude': lambda f: f is None }})
    follower: Optional[shared_usercompact.UserCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('follower'), 'exclude': lambda f: f is None }})
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    hearted: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hearted'), 'exclude': lambda f: f is None }})
    r"""*Deprecated - please use likes instead*
    *Conditional*. True if the story is hearted by the authorized user, false if not.
    """
    hearts: Optional[list[shared_like.Like]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('hearts'), 'exclude': lambda f: f is None }})
    r"""*Deprecated - please use likes instead*

    *Conditional*. Array of likes for users who have hearted this story.
    """
    html_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_text'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). HTML formatted text for a comment. This will not include the name of the creator."""
    is_editable: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_editable'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. Whether the text of the story can be edited after creation."""
    is_edited: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_edited'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. Whether the text of the story has been edited after creation."""
    is_pinned: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('is_pinned'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. Whether the story should be pinned on the resource."""
    liked: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('liked'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. True if the story is liked by the authorized user, false if not."""
    likes: Optional[list[shared_like.Like]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('likes'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. Array of likes for users who have liked this story."""
    new_approval_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_approval_status'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. The new value of approval status."""
    new_date_value: Optional[StoryResponseNewDateValue] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_date_value'), 'exclude': lambda f: f is None }})
    new_dates: Optional[shared_storyresponsedates.StoryResponseDates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_dates'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    new_enum_value: Optional[shared_enumoption.EnumOption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_enum_value'), 'exclude': lambda f: f is None }})
    new_multi_enum_values: Optional[list[shared_enumoption.EnumOption]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_multi_enum_values'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. The new value of a multi-enum custom field story."""
    new_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_name'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    new_number_value: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_number_value'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    new_people_value: Optional[list[shared_usercompact.UserCompact]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_people_value'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. The new value of a people custom field story."""
    new_resource_subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_resource_subtype'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    new_section: Optional[shared_sectioncompact.SectionCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_section'), 'exclude': lambda f: f is None }})
    new_text_value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('new_text_value'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    num_hearts: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_hearts'), 'exclude': lambda f: f is None }})
    r"""*Deprecated - please use likes instead*

    *Conditional*. The number of users who have hearted this story.
    """
    num_likes: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_likes'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. The number of users who have liked this story."""
    old_approval_status: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_approval_status'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. The old value of approval status."""
    old_date_value: Optional[StoryResponseOldDateValue] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_date_value'), 'exclude': lambda f: f is None }})
    old_dates: Optional[shared_storyresponsedates.StoryResponseDates] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_dates'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    old_enum_value: Optional[shared_enumoption.EnumOption] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_enum_value'), 'exclude': lambda f: f is None }})
    old_multi_enum_values: Optional[list[shared_enumoption.EnumOption]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_multi_enum_values'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. The old value of a multi-enum custom field story."""
    old_name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_name'), 'exclude': lambda f: f is None }})
    r"""*Conditional*'"""
    old_number_value: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_number_value'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    old_people_value: Optional[list[shared_usercompact.UserCompact]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_people_value'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. The old value of a people custom field story."""
    old_resource_subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_resource_subtype'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    old_section: Optional[shared_sectioncompact.SectionCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_section'), 'exclude': lambda f: f is None }})
    old_text_value: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('old_text_value'), 'exclude': lambda f: f is None }})
    r"""*Conditional*"""
    previews: Optional[list[shared_preview.Preview]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('previews'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. A collection of previews to be displayed in the story.

    *Note: This property only exists for comment stories.*
    """
    project: Optional[shared_projectcompact.ProjectCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('project'), 'exclude': lambda f: f is None }})
    resource_subtype: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_subtype'), 'exclude': lambda f: f is None }})
    r"""The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning."""
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    source: Optional[StoryResponseSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('source'), 'exclude': lambda f: f is None }})
    r"""The component of the Asana product the user used to trigger the story."""
    sticker_name: Optional[StoryResponseStickerName] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sticker_name'), 'exclude': lambda f: f is None }})
    r"""The name of the sticker in this story. `null` if there is no sticker."""
    story: Optional[shared_storycompact.StoryCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('story'), 'exclude': lambda f: f is None }})
    tag: Optional[shared_tagcompact.TagCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tag'), 'exclude': lambda f: f is None }})
    target: Optional[StoryResponseTarget] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target'), 'exclude': lambda f: f is None }})
    task: Optional[shared_taskcompact.TaskCompact] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('task'), 'exclude': lambda f: f is None }})
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""The plain text of the comment to add. Cannot be used with html_text."""
    type: Optional[StoryResponseType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('type'), 'exclude': lambda f: f is None }})
    

