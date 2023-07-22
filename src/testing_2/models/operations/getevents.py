"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import errorresponse as shared_errorresponse
from ..shared import eventresponse as shared_eventresponse
from dataclasses_json import Undefined, dataclass_json
from testing_2 import utils
from typing import Optional



@dataclasses.dataclass
class GetEventsRequest:
    resource: str = dataclasses.field(metadata={'query_param': { 'field_name': 'resource', 'style': 'form', 'explode': True }})
    r"""A resource ID to subscribe to. The resource can be a task or project."""
    opt_fields: Optional[list[str]] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'opt_fields', 'style': 'form', 'explode': False }})
    r"""Defines fields to return.
    Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below.
    The id of included objects will always be returned, regardless of the field options.
    """
    opt_pretty: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'opt_pretty', 'style': 'form', 'explode': True }})
    r"""Provides “pretty” output.
    Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    """
    sync: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'sync', 'style': 'form', 'explode': True }})
    r"""A sync token received from the last request, or none on first sync. Events will be returned from the point in time that the sync token was generated.
    *Note: On your first request, omit the sync token. The response will be the same as for an expired sync token, and will include a new valid sync token.If the sync token is too old (which may happen from time to time) the API will return a `412 Precondition Failed` error, and include a fresh sync token in the response.*
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetEvents200ApplicationJSON:
    r"""The full record for all events that have occurred since the sync token was created."""
    data: Optional[list[shared_eventresponse.EventResponse]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    has_more: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('has_more'), 'exclude': lambda f: f is None }})
    r"""Indicates whether there are more events to pull."""
    sync: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sync'), 'exclude': lambda f: f is None }})
    r"""A sync token to be used with the next call to the /events endpoint."""
    




@dataclasses.dataclass
class GetEventsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again."""
    get_events_200_application_json_object: Optional[GetEvents200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successfully retrieved events."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

