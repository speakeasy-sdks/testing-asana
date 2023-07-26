"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from testing_2 import utils
from typing import Optional

class GoalMetricRequestProgressSource(str, Enum):
    r"""This field defines how the progress value of a goal metric is being calculated. A goal's progress can be provided manually by the user, calculated automatically from contributing subgoals or projects, or managed by an integration with an external data source, such as Salesforce."""
    MANUAL = 'manual'
    SUBGOAL_PROGRESS = 'subgoal_progress'
    PROJECT_TASK_COMPLETION = 'project_task_completion'
    PROJECT_MILESTONE_COMPLETION = 'project_milestone_completion'
    EXTERNAL = 'external'

class GoalMetricRequestUnit(str, Enum):
    r"""A supported unit of measure for the goal metric, or none."""
    NONE = 'none'
    CURRENCY = 'currency'
    PERCENTAGE = 'percentage'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GoalMetricRequestInput:
    r"""A generic Asana Resource, containing a globally unique identifier."""
    currency_code: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('currency_code'), 'exclude': lambda f: f is None }})
    r"""ISO 4217 currency code to format this custom field. This will be null if the `unit` is not `currency`."""
    current_number_value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('current_number_value'), 'exclude': lambda f: f is None }})
    r"""This number is the current value of a goal metric of type number."""
    initial_number_value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initial_number_value'), 'exclude': lambda f: f is None }})
    r"""This number is the start value of a goal metric of type number."""
    precision: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('precision'), 'exclude': lambda f: f is None }})
    r"""*Conditional*. Only relevant for goal metrics of type ‘Number’. This field dictates the number of places after the decimal to round to, i.e. 0 is integer values, 1 rounds to the nearest tenth, and so on. Must be between 0 and 6, inclusive.
    For percentage format, this may be unintuitive, as a value of 0.25 has a precision of 0, while a value of 0.251 has a precision of 1. This is due to 0.25 being displayed as 25%.
    """
    progress_source: Optional[GoalMetricRequestProgressSource] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('progress_source'), 'exclude': lambda f: f is None }})
    r"""This field defines how the progress value of a goal metric is being calculated. A goal's progress can be provided manually by the user, calculated automatically from contributing subgoals or projects, or managed by an integration with an external data source, such as Salesforce."""
    target_number_value: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('target_number_value'), 'exclude': lambda f: f is None }})
    r"""This number is the end value of a goal metric of type number. This number cannot equal `initial_number_value`."""
    unit: Optional[GoalMetricRequestUnit] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unit'), 'exclude': lambda f: f is None }})
    r"""A supported unit of measure for the goal metric, or none."""
    

