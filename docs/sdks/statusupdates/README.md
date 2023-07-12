# status_updates

## Overview

A status update is an update on the progress of a particular object,
and is sent out to all followers when created. These updates
include both text describing the update and a `status_type` intended to
represent the overall state of the project. These include: `on_track` for projects that
are on track, `at_risk` for projects at risk, `off_track` for projects that
are behind, and `on_hold` for projects on hold.

Status updates can be created and deleted, but not modified.

### Available Operations

* [create_status_for_object](#create_status_for_object) - Create a status update
* [delete_status](#delete_status) - Delete a status update
* [get_status](#get_status) - Get a status update
* [get_statuses_for_object](#get_statuses_for_object) - Get status updates from an object

## create_status_for_object

Creates a new status update on an object.
Returns the full record of the newly created status update.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateStatusForObjectRequest(
    request_body=operations.CreateStatusForObjectRequestBodyInput(
        data=shared.StatusUpdateRequestInput(
            html_text='<body>The project <strong>is</strong> moving forward according to plan...</body>',
            parent='odio',
            status_type=shared.StatusUpdateRequestStatusType.ACHIEVED,
            text='The project is moving forward according to plan...',
            title='Status Update - Jun 15',
        ),
    ),
    limit=708548,
    offset='vero',
    opt_fields=[
        'dolore',
        'quibusdam',
    ],
    opt_pretty=False,
)

res = s.status_updates.create_status_for_object(req)

if res.create_status_for_object_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.CreateStatusForObjectRequest](../../models/operations/createstatusforobjectrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.CreateStatusForObjectResponse](../../models/operations/createstatusforobjectresponse.md)**


## delete_status

Deletes a specific, existing status update.

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

req = operations.DeleteStatusRequest(
    opt_fields=[
        'sequi',
        'natus',
        'impedit',
        'aut',
    ],
    opt_pretty=False,
    status_gid='voluptatibus',
)

res = s.status_updates.delete_status(req)

if res.delete_status_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.DeleteStatusRequest](../../models/operations/deletestatusrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.DeleteStatusResponse](../../models/operations/deletestatusresponse.md)**


## get_status

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

req = operations.GetStatusRequest(
    opt_fields=[
        'nulla',
        'fugit',
    ],
    opt_pretty=False,
    status_gid='porro',
)

res = s.status_updates.get_status(req)

if res.get_status_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                  | Type                                                                       | Required                                                                   | Description                                                                |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `request`                                                                  | [operations.GetStatusRequest](../../models/operations/getstatusrequest.md) | :heavy_check_mark:                                                         | The request object to use for the request.                                 |


### Response

**[operations.GetStatusResponse](../../models/operations/getstatusresponse.md)**


## get_statuses_for_object

Returns the compact status update records for all updates on the object.

### Example Usage

```python
import testing_2
import dateutil.parser
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetStatusesForObjectRequest(
    created_since=dateutil.parser.isoparse('2020-01-18T09:21:05.997Z'),
    limit=478370,
    offset='eligendi',
    opt_fields=[
        'alias',
        'officia',
    ],
    opt_pretty=False,
    parent='tempora',
)

res = s.status_updates.get_statuses_for_object(req)

if res.get_statuses_for_object_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetStatusesForObjectRequest](../../models/operations/getstatusesforobjectrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetStatusesForObjectResponse](../../models/operations/getstatusesforobjectresponse.md)**

