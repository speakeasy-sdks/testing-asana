# tags

## Overview

A tag is a label that can be attached to any task in Asana. It exists in a single workspace or organization.

Tags have some metadata associated with them, but it is possible that we will simplify them in the future so it is not encouraged to rely too heavily on it. Unlike projects, tags do not provide any ordering on the tasks they are associated with.

### Available Operations

* [create_tag](#create_tag) - Create a tag
* [create_tag_for_workspace](#create_tag_for_workspace) - Create a tag in a workspace
* [delete_tag](#delete_tag) - Delete a tag
* [get_tag](#get_tag) - Get a tag
* [get_tags](#get_tags) - Get multiple tags
* [get_tags_for_task](#get_tags_for_task) - Get a task's tags
* [get_tags_for_workspace](#get_tags_for_workspace) - Get tags in a workspace
* [update_tag](#update_tag) - Update a tag

## create_tag

Creates a new tag in a workspace or organization.

Every tag is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the workspace parameter regardless of whether or not it is an
organization.

Returns the full record of the newly created tag.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateTagRequest(
    request_body=operations.CreateTagRequestBodyInput(
        data=shared.TagRequestInput(
            color=shared.TagRequestColor.LIGHT_GREEN,
            followers=[
                'inventore',
                'magnam',
            ],
            name='Stuff to buy',
            notes='Mittens really likes the stuff from Humboldt.',
            workspace='12345',
        ),
    ),
    opt_fields=[
        'quo',
        'consectetur',
    ],
    opt_pretty=False,
)

res = s.tags.create_tag(req)

if res.create_tag_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.CreateTagRequest](../../models/operations/createtagrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.CreateTagResponse](../../models/operations/createtagresponse.md)**


## create_tag_for_workspace

Creates a new tag in a workspace or organization.

Every tag is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the workspace parameter regardless of whether or not it is an
organization.

Returns the full record of the newly created tag.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateTagForWorkspaceRequest(
    request_body=operations.CreateTagForWorkspaceRequestBodyInput(
        data=shared.TagResponseInput(
            color=shared.TagResponseColor.LIGHT_GREEN,
            name='Stuff to buy',
            notes='Mittens really likes the stuff from Humboldt.',
            workspace=shared.WorkspaceCompactInput(
                name='My Company Workspace',
            ),
        ),
    ),
    opt_fields=[
        'aspernatur',
        'minima',
        'eaque',
        'a',
    ],
    opt_pretty=False,
    workspace_gid='libero',
)

res = s.tags.create_tag_for_workspace(req)

if res.create_tag_for_workspace_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateTagForWorkspaceRequest](../../models/operations/createtagforworkspacerequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CreateTagForWorkspaceResponse](../../models/operations/createtagforworkspaceresponse.md)**


## delete_tag

A specific, existing tag can be deleted by making a DELETE request on
the URL for that tag.

Returns an empty data record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.DeleteTagRequest(
    limit=13948,
    offset='aut',
    opt_fields=[
        'impedit',
        'aliquam',
        'fugit',
    ],
    opt_pretty=False,
    tag_gid='accusamus',
)

res = s.tags.delete_tag(req)

if res.delete_tag_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.DeleteTagRequest](../../models/operations/deletetagrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.DeleteTagResponse](../../models/operations/deletetagresponse.md)**


## get_tag

Returns the complete tag record for a single tag.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTagRequest(
    limit=79522,
    offset='non',
    opt_fields=[
        'dolorum',
    ],
    opt_pretty=False,
    tag_gid='laborum',
)

res = s.tags.get_tag(req)

if res.get_tag_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.GetTagRequest](../../models/operations/gettagrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.GetTagResponse](../../models/operations/gettagresponse.md)**


## get_tags

Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTagsRequest(
    limit=810424,
    offset='velit',
    opt_fields=[
        'autem',
        'nobis',
    ],
    opt_pretty=False,
    workspace='quas',
)

res = s.tags.get_tags(req)

if res.get_tags_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetTagsRequest](../../models/operations/gettagsrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetTagsResponse](../../models/operations/gettagsresponse.md)**


## get_tags_for_task

Get a compact representation of all of the tags the task has.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTagsForTaskRequest(
    limit=829603,
    offset='nulla',
    opt_fields=[
        'libero',
        'quasi',
    ],
    opt_pretty=False,
    task_gid='tempora',
)

res = s.tags.get_tags_for_task(req)

if res.get_tags_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTagsForTaskRequest](../../models/operations/gettagsfortaskrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetTagsForTaskResponse](../../models/operations/gettagsfortaskresponse.md)**


## get_tags_for_workspace

Returns the compact tag records for some filtered set of tags. Use one or more of the parameters provided to filter the tags returned.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTagsForWorkspaceRequest(
    limit=256139,
    offset='explicabo',
    opt_fields=[
        'ipsa',
        'molestiae',
        'magnam',
    ],
    opt_pretty=False,
    workspace_gid='odio',
)

res = s.tags.get_tags_for_workspace(req)

if res.get_tags_for_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetTagsForWorkspaceRequest](../../models/operations/gettagsforworkspacerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetTagsForWorkspaceResponse](../../models/operations/gettagsforworkspaceresponse.md)**


## update_tag

Updates the properties of a tag. Only the fields provided in the `data`
block will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the tag.

Returns the complete updated tag record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateTagRequest(
    limit=262118,
    offset='esse',
    opt_fields=[
        'rem',
        'fuga',
    ],
    opt_pretty=False,
    tag_gid='reprehenderit',
)

res = s.tags.update_tag(req)

if res.update_tag_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.UpdateTagRequest](../../models/operations/updatetagrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.UpdateTagResponse](../../models/operations/updatetagresponse.md)**

