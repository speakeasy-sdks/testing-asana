"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import statusupdatecompact as shared_statusupdatecompact
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from testing_2 import utils
from typing import Optional



@dataclasses.dataclass
class GetStatusesForObjectRequest:
    parent: str = dataclasses.field(metadata={'query_param': { 'field_name': 'parent', 'style': 'form', 'explode': True }})
    r"""Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal."""
    created_since: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'created_since', 'style': 'form', 'explode': True }})
    r"""Only return statuses that have been created since the given time."""
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Results per page.
    The number of objects to return per page. The value must be between 1 and 100.
    """
    offset: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Offset token.
    An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
    'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    """
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
class GetStatusesForObject200ApplicationJSON:
    r"""Successfully retrieved the specified object's status updates."""
    data: Optional[list[shared_statusupdatecompact.StatusUpdateCompact]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetStatusesForObjectResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again."""
    get_statuses_for_object_200_application_json_object: Optional[GetStatusesForObject200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successfully retrieved the specified object's status updates."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

