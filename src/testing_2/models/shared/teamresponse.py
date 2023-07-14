"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from testing_2 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeamResponseOrganization:
    r"""A *workspace* is the highest-level organizational unit in Asana. All projects and tasks have an associated workspace."""
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the workspace."""
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    


class TeamResponseVisibility(str, Enum):
    r"""The visibility of the team to users in the same organization"""
    SECRET = 'secret'
    REQUEST_TO_JOIN = 'request_to_join'
    PUBLIC = 'public'


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class TeamResponse:
    r"""A *team* is used to group related projects and people together within an organization. Each project in an organization is associated with a team."""
    description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). The description of the team."""
    gid: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('gid'), 'exclude': lambda f: f is None }})
    r"""Globally unique identifier of the resource, as a string."""
    html_description: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_description'), 'exclude': lambda f: f is None }})
    r"""[Opt In](/docs/input-output-options). The description of the team with formatting as HTML."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    r"""The name of the team."""
    organization: Optional[TeamResponseOrganization] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('organization'), 'exclude': lambda f: f is None }})
    permalink_url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('permalink_url'), 'exclude': lambda f: f is None }})
    r"""A url that points directly to the object within Asana."""
    resource_type: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resource_type'), 'exclude': lambda f: f is None }})
    r"""The base type of this resource."""
    visibility: Optional[TeamResponseVisibility] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('visibility'), 'exclude': lambda f: f is None }})
    r"""The visibility of the team to users in the same organization"""
    
