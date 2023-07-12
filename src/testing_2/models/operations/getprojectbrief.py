"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import projectbriefresponse as shared_projectbriefresponse
from dataclasses_json import Undefined, dataclass_json
from testing_2 import utils
from typing import Optional



@dataclasses.dataclass
class GetProjectBriefRequest:
    project_brief_gid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'project_brief_gid', 'style': 'simple', 'explode': False }})
    r"""Globally unique identifier for the project brief."""
    opt_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'opt_fields', 'style': 'form', 'explode': False }})
    r"""Defines fields to return.
    Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.
    The id of included objects will always be returned, regardless of the field options.
    """
    opt_pretty: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'opt_pretty', 'style': 'form', 'explode': True }})
    r"""Provides “pretty” output.
    Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetProjectBrief200ApplicationJSON:
    r"""Successfully retrieved the record for a project brief."""
    data: Optional[shared_projectbriefresponse.ProjectBriefResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetProjectBriefResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again."""
    get_project_brief_200_application_json_object: Optional[GetProjectBrief200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successfully retrieved the record for a project brief."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

