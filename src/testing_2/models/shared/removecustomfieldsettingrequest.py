"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from testing_2 import utils


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class RemoveCustomFieldSettingRequest:
    custom_field: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('custom_field') }})
    r"""The custom field to remove from this portfolio."""
    
