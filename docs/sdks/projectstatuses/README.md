# project_statuses

## Overview

*Deprecated: new integrations should prefer using [status updates](/docs/asana-statuses)*

A project status is an update on the progress of a particular project,
and is sent out to all project followers when created. These updates
include both text describing the update and a color code intended to
represent the overall state of the project: "green" for projects that
are on track, "yellow" for projects at risk, "red" for projects that
are behind, and "blue" for projects on hold.

Project statuses can be created and deleted, but not modified.

### Available Operations

* [create_project_status_for_project](#create_project_status_for_project) - Create a project status
* [delete_project_status](#delete_project_status) - Delete a project status
* [get_project_status](#get_project_status) - Get a project status
* [get_project_statuses_for_project](#get_project_statuses_for_project) - Get statuses from a project

## create_project_status_for_project

*Deprecated: new integrations should prefer the `/status_updates` route.*

Creates a new status update on the project.

Returns the full record of the newly created project status update.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateProjectStatusForProjectRequest(
    request_body=operations.CreateProjectStatusForProjectRequestBodyInput(
        data=shared.ProjectStatusRequestInput(
            color=shared.ProjectStatusRequestColor.BLUE,
            html_text='<body>The project <strong>is</strong> moving forward according to plan...</body>',
            text='The project is moving forward according to plan...',
            title='Status Update - Jun 15',
        ),
    ),
    opt_fields=[
        'hic',
        'recusandae',
    ],
    opt_pretty=False,
    project_gid='omnis',
)

res = s.project_statuses.create_project_status_for_project(req)

if res.create_project_status_for_project_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                          | Type                                                                                                               | Required                                                                                                           | Description                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                          | [operations.CreateProjectStatusForProjectRequest](../../models/operations/createprojectstatusforprojectrequest.md) | :heavy_check_mark:                                                                                                 | The request object to use for the request.                                                                         |


### Response

**[operations.CreateProjectStatusForProjectResponse](../../models/operations/createprojectstatusforprojectresponse.md)**


## delete_project_status

*Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*

Deletes a specific, existing project status update.

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

req = operations.DeleteProjectStatusRequest(
    opt_fields=[
        'perspiciatis',
        'voluptatem',
        'porro',
    ],
    opt_pretty=False,
    project_status_gid='consequuntur',
)

res = s.project_statuses.delete_project_status(req)

if res.delete_project_status_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.DeleteProjectStatusRequest](../../models/operations/deleteprojectstatusrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.DeleteProjectStatusResponse](../../models/operations/deleteprojectstatusresponse.md)**


## get_project_status

*Deprecated: new integrations should prefer the `/status_updates/{status_gid}` route.*

Returns the complete record for a single status update.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectStatusRequest(
    opt_fields=[
        'error',
        'eaque',
        'occaecati',
    ],
    opt_pretty=False,
    project_status_gid='rerum',
)

res = s.project_statuses.get_project_status(req)

if res.get_project_status_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.GetProjectStatusRequest](../../models/operations/getprojectstatusrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.GetProjectStatusResponse](../../models/operations/getprojectstatusresponse.md)**


## get_project_statuses_for_project

*Deprecated: new integrations should prefer the `/status_updates` route.*

Returns the compact project status update records for all updates on the project.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectStatusesForProjectRequest(
    limit=237893,
    offset='asperiores',
    opt_fields=[
        'modi',
        'iste',
        'dolorum',
        'deleniti',
    ],
    opt_pretty=False,
    project_gid='pariatur',
)

res = s.project_statuses.get_project_statuses_for_project(req)

if res.get_project_statuses_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.GetProjectStatusesForProjectRequest](../../models/operations/getprojectstatusesforprojectrequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.GetProjectStatusesForProjectResponse](../../models/operations/getprojectstatusesforprojectresponse.md)**

