"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from testing_2 import utils
from typing import Optional



@dataclasses.dataclass
class BatchResponseBody:
    r"""The JSON body that the invoked endpoint returned."""
    




@dataclasses.dataclass
class BatchResponseHeaders:
    r"""A map of HTTP headers specific to this result. This is primarily used for returning a `Location` header to accompany a `201 Created` result.  The parent HTTP response will contain all common headers."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BatchResponse:
    r"""A response object returned from a batch request."""
    body: Optional[BatchResponseBody] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('body'), 'exclude': lambda f: f is None }})
    r"""The JSON body that the invoked endpoint returned."""
    headers: Optional[BatchResponseHeaders] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('headers'), 'exclude': lambda f: f is None }})
    r"""A map of HTTP headers specific to this result. This is primarily used for returning a `Location` header to accompany a `201 Created` result.  The parent HTTP response will contain all common headers."""
    status_code: Optional[int] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('status_code'), 'exclude': lambda f: f is None }})
    r"""The HTTP status code that the invoked endpoint returned."""
    

