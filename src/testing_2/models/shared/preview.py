"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from dataclasses_json import Undefined, dataclass_json
from testing_2 import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class Preview:
    r"""A collection of rich text that will be displayed as a preview to another app.

    This is read-only except for a small group of whitelisted apps.
    """
    fallback: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fallback'), 'exclude': lambda f: f is None }})
    r"""Some fallback text to display if unable to display the full preview."""
    footer: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('footer'), 'exclude': lambda f: f is None }})
    r"""Text to display in the footer."""
    header: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header'), 'exclude': lambda f: f is None }})
    r"""Text to display in the header."""
    header_link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('header_link'), 'exclude': lambda f: f is None }})
    r"""Where the header will link to."""
    html_text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('html_text'), 'exclude': lambda f: f is None }})
    r"""HTML formatted text for the body of the preview."""
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Text for the body of the preview."""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""Text to display as the title."""
    title_link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title_link'), 'exclude': lambda f: f is None }})
    r"""Where to title will link to."""
    
