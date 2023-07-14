"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
from enum import Enum
from typing import Optional



@dataclasses.dataclass
class AttachmentRequestFile:
    content: bytes = dataclasses.field(metadata={'multipart_form': { 'content': True }})
    file: str = dataclasses.field(metadata={'multipart_form': { 'field_name': 'file' }})
    


class AttachmentRequestResourceSubtype(str, Enum):
    r"""The type of the attachment. Must be one of the given values. If not specified, a file attachment of type `asana` will be assumed. Note that if the value of `resource_subtype` is `external`, a `parent`, `name`, and `url` must also be provided."""
    ASANA = 'asana'
    DROPBOX = 'dropbox'
    GDRIVE = 'gdrive'
    ONEDRIVE = 'onedrive'
    BOX = 'box'
    VIMEO = 'vimeo'
    EXTERNAL = 'external'



@dataclasses.dataclass
class AttachmentRequest1:
    r"""The file you want to upload.

    *Note when using curl:*

    Be sure to add an `‘@’` before the file path, and use the `--form`
    option instead of the `-d` option.

    When uploading PDFs with curl, force the content-type to be pdf by
    appending the content type to the file path: `--form
    \"file=@file.pdf;type=application/pdf\"`.
    """
    connect_to_app: Optional[bool] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'connect_to_app' }})
    r"""*Optional*. Only relevant for external attachments with a parent task. A boolean indicating whether the current app should be connected with the attachment for the purposes of showing an app components widget. Requires the app to have been added to a project the parent task is in."""
    file: Optional[AttachmentRequestFile] = dataclasses.field(default=None, metadata={'multipart_form': { 'file': True }})
    r"""Required for `asana` attachments."""
    name: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'name' }})
    r"""The name of the external resource being attached. Required for attachments of type `external`."""
    parent: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'parent' }})
    r"""Required identifier of the parent task, project, or project_brief, as a string."""
    resource_subtype: Optional[AttachmentRequestResourceSubtype] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'resource_subtype' }})
    r"""The type of the attachment. Must be one of the given values. If not specified, a file attachment of type `asana` will be assumed. Note that if the value of `resource_subtype` is `external`, a `parent`, `name`, and `url` must also be provided."""
    url: Optional[str] = dataclasses.field(default=None, metadata={'multipart_form': { 'field_name': 'url' }})
    r"""The URL of the external resource being attached. Required for attachments of type `external`."""
    
