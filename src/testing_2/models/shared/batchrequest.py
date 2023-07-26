"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from ..shared import batchrequestaction as shared_batchrequestaction
from dataclasses_json import Undefined, dataclass_json
from testing_2 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class BatchRequest:
    r"""A request object for use in a batch request."""
    actions: Optional[list[shared_batchrequestaction.BatchRequestAction]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('actions'), 'exclude': lambda f: f is None }})
    

