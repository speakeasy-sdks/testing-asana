# project_briefs

## Overview

A project brief object represents a rich text document that describes a project.

Please note that this API is in *preview*, and is expected to change. This API is to be used for development and testing only as an advance view into the upcoming rich text format experience in the task description. For more information, see [this post](https://forum.asana.com/t/project-brief-api-now-available-as-a-preview/150885) in the developer forum.

### Available Operations

* [create_project_brief](#create_project_brief) - Create a project brief
* [delete_project_brief](#delete_project_brief) - Delete a project brief
* [get_project_brief](#get_project_brief) - Get a project brief
* [update_project_brief](#update_project_brief) - Update a project brief

## create_project_brief

Creates a new project brief.

Returns the full record of the newly created project brief.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateProjectBriefRequest(
    request_body=operations.CreateProjectBriefRequestBodyInput(
        data=shared.ProjectBriefRequestInput(
            html_text='<body>This is a <strong>project brief</strong>.</body>',
            text='This is a project brief.',
            title='Stuff to buy — Project Brief',
        ),
    ),
    opt_fields=[
        'pariatur',
    ],
    opt_pretty=False,
    project_gid='nemo',
)

res = s.project_briefs.create_project_brief(req)

if res.create_project_brief_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.CreateProjectBriefRequest](../../models/operations/createprojectbriefrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.CreateProjectBriefResponse](../../models/operations/createprojectbriefresponse.md)**


## delete_project_brief

Deletes a specific, existing project brief.

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

req = operations.DeleteProjectBriefRequest(
    opt_fields=[
        'perferendis',
        'fugiat',
        'amet',
        'aut',
    ],
    opt_pretty=False,
    project_brief_gid='cumque',
)

res = s.project_briefs.delete_project_brief(req)

if res.delete_project_brief_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.DeleteProjectBriefRequest](../../models/operations/deleteprojectbriefrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.DeleteProjectBriefResponse](../../models/operations/deleteprojectbriefresponse.md)**


## get_project_brief

Get the full record for a project brief.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectBriefRequest(
    opt_fields=[
        'hic',
        'libero',
    ],
    opt_pretty=False,
    project_brief_gid='nobis',
)

res = s.project_briefs.get_project_brief(req)

if res.get_project_brief_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetProjectBriefRequest](../../models/operations/getprojectbriefrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetProjectBriefResponse](../../models/operations/getprojectbriefresponse.md)**


## update_project_brief

An existing project brief can be updated by making a PUT request on the URL for
that project brief. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated project brief record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateProjectBriefRequest(
    request_body=operations.UpdateProjectBriefRequestBodyInput(
        data=shared.ProjectBriefRequestInput(
            html_text='<body>This is a <strong>project brief</strong>.</body>',
            text='This is a project brief.',
            title='Stuff to buy — Project Brief',
        ),
    ),
    opt_fields=[
        'quis',
    ],
    opt_pretty=False,
    project_brief_gid='totam',
)

res = s.project_briefs.update_project_brief(req)

if res.update_project_brief_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.UpdateProjectBriefRequest](../../models/operations/updateprojectbriefrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.UpdateProjectBriefResponse](../../models/operations/updateprojectbriefresponse.md)**

