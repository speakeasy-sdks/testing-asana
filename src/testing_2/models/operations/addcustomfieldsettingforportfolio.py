"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ..shared import addcustomfieldsettingrequest as shared_addcustomfieldsettingrequest
from ..shared import customfieldsettingresponse as shared_customfieldsettingresponse
from ..shared import errorresponse as shared_errorresponse
from dataclasses_json import Undefined, dataclass_json
from testing_2 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AddCustomFieldSettingForPortfolioRequestBody:
    r"""Information about the custom field setting."""
    data: Optional[shared_addcustomfieldsettingrequest.AddCustomFieldSettingRequest] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class AddCustomFieldSettingForPortfolioRequest:
    portfolio_gid: str = dataclasses.field(metadata={'path_param': { 'field_name': 'portfolio_gid', 'style': 'simple', 'explode': False }})
    r"""Globally unique identifier for the portfolio."""
    request_body: AddCustomFieldSettingForPortfolioRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Information about the custom field setting."""
    opt_pretty: Optional[bool] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'opt_pretty', 'style': 'form', 'explode': True }})
    r"""Provides “pretty” output.
    Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    """
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class AddCustomFieldSettingForPortfolio200ApplicationJSON:
    r"""Successfully added the custom field to the portfolio."""
    data: Optional[shared_customfieldsettingresponse.CustomFieldSettingResponse] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('data'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class AddCustomFieldSettingForPortfolioResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    add_custom_field_setting_for_portfolio_200_application_json_object: Optional[AddCustomFieldSettingForPortfolio200ApplicationJSON] = dataclasses.field(default=None)
    r"""Successfully added the custom field to the portfolio."""
    error_response: Optional[shared_errorresponse.ErrorResponse] = dataclasses.field(default=None)
    r"""This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again."""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    

