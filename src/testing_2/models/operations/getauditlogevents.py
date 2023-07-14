"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import audit_log_actor_type as shared_audit_log_actor_type
from ..shared import auditlogevent as shared_auditlogevent
from ..shared import errorresponse as shared_errorresponse
from dataclasses_json import Undefined, dataclass_json
from datetime import datetime
from testing_2 import utils
from typing import Optional



@dataclasses.dataclass
class GetAuditLogEventsRequest:
    workspace_gid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'workspace_gid', 'style': 'simple', 'explode': False }})
    r"""Globally unique identifier for the workspace or organization."""
    actor_gid: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'actor_gid', 'style': 'form', 'explode': True }})
    r"""Filter to events triggered by the actor with this ID."""
    actor_type: Optional[shared_audit_log_actor_type.AuditLogActorType] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'actor_type', 'style': 'form', 'explode': True }})
    r"""Filter to events with an actor of this type.
    This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.
    """
    end_at: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'end_at', 'style': 'form', 'explode': True }})
    r"""Filter to events created before this time (exclusive)."""
    event_type: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'event_type', 'style': 'form', 'explode': True }})
    r"""Filter to events of this type.
    Refer to the [Supported AuditLogEvents](/docs/supported-auditlogevents) for a full list of values.
    """
    limit: Optional[int] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'limit', 'style': 'form', 'explode': True }})
    r"""Results per page.
    The number of objects to return per page. The value must be between 1 and 100.
    """
    offset: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'offset', 'style': 'form', 'explode': True }})
    r"""Offset token.
    An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results.
    'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
    """
    resource_gid: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'resource_gid', 'style': 'form', 'explode': True }})
    r"""Filter to events with this resource ID."""
    start_at: Optional[datetime] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'start_at', 'style': 'form', 'explode': True }})
    r"""Filter to events created after this time (inclusive)."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetAuditLogEvents200ApplicationJSON:
    r"""AuditLogEvents were successfully retrieved."""
    data: Optional[list[shared_auditlogevent.AuditLogEvent]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetAuditLogEventsResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again."""
    get_audit_log_events_200_application_json_object: Optional[GetAuditLogEvents200ApplicationJSON] = dataclasses.field(default=None)
    r"""AuditLogEvents were successfully retrieved."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
