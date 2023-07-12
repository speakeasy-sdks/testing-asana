# attachments

## Overview

An *attachment* object represents any file attached to a task in Asana, whether it’s an uploaded file or one associated via a third-party service such as Dropbox or Google Drive.

### Available Operations

* [create_attachment_for_object](#create_attachment_for_object) - Upload an attachment
* [delete_attachment](#delete_attachment) - Delete an attachment
* [get_attachment](#get_attachment) - Get an attachment
* [get_attachments_for_object](#get_attachments_for_object) - Get attachments from an object

## create_attachment_for_object

Upload an attachment.

This method uploads an attachment on an object and returns the compact
record for the created attachment object. This is possible by either:

- Providing the URL of the external resource being attached, or
- Downloading the file content first and then uploading it as any other attachment. Note that it is not possible to attach
files from third party services such as Dropbox, Box, Vimeo & Google Drive via the API

The 100MB size limit on attachments in Asana is enforced on this endpoint.

This endpoint expects a multipart/form-data encoded request containing the full contents of the file to be uploaded.

Requests made should follow the HTTP/1.1 specification that line
terminators are of the form `CRLF` or `\r\n` outlined
[here](http://www.w3.org/Protocols/HTTP/1.1/draft-ietf-http-v11-spec-01#Basic-Rules) in order for the server to reliably and properly handle the request.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateAttachmentForObjectRequest(
    attachment_request1=shared.AttachmentRequest1(
        connect_to_app=False,
        file=shared.AttachmentRequestFile(
            content='magnam'.encode(),
            file='debitis',
        ),
        name='Lucia Goldner',
        parent='minus',
        resource_subtype=shared.AttachmentRequestResourceSubtype.EXTERNAL,
        url='placeat',
    ),
    opt_fields=[
        'iusto',
        'excepturi',
        'nisi',
    ],
    opt_pretty=False,
)

res = s.attachments.create_attachment_for_object(req)

if res.create_attachment_for_object_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateAttachmentForObjectRequest](../../models/operations/createattachmentforobjectrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.CreateAttachmentForObjectResponse](../../models/operations/createattachmentforobjectresponse.md)**


## delete_attachment

Deletes a specific, existing attachment.

Returns an empty data record.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.DeleteAttachmentRequest(
    attachment_gid='recusandae',
    opt_fields=[
        'ab',
        'quis',
        'veritatis',
        'deserunt',
    ],
    opt_pretty=False,
)

res = s.attachments.delete_attachment(req)

if res.delete_attachment_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DeleteAttachmentRequest](../../models/operations/deleteattachmentrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DeleteAttachmentResponse](../../models/operations/deleteattachmentresponse.md)**


## get_attachment

Get the full record for a single attachment.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetAttachmentRequest(
    attachment_gid='perferendis',
    opt_fields=[
        'repellendus',
        'sapiente',
    ],
    opt_pretty=False,
)

res = s.attachments.get_attachment(req)

if res.get_attachment_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetAttachmentRequest](../../models/operations/getattachmentrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetAttachmentResponse](../../models/operations/getattachmentresponse.md)**


## get_attachments_for_object

Returns the compact records for all attachments on the object.

There are three possible `parent` values for this request: `project`, `project_brief`, and `task`. For a project, an attachment refers to a file uploaded to the "Key resources" section in the project Overview. For a project brief, an attachment refers to inline files in the project brief itself. For a task, an attachment refers to a file directly associated to that task.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetAttachmentsForObjectRequest(
    limit=778157,
    offset='odit',
    opt_fields=[
        'at',
        'maiores',
        'molestiae',
        'quod',
    ],
    opt_pretty=False,
    parent='quod',
)

res = s.attachments.get_attachments_for_object(req)

if res.get_attachments_for_object_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetAttachmentsForObjectRequest](../../models/operations/getattachmentsforobjectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetAttachmentsForObjectResponse](../../models/operations/getattachmentsforobjectresponse.md)**

