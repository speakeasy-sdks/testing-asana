# user_task_lists

## Overview

A user task list represents the tasks assigned to a particular user. This list is the user's [My Tasks](https://asana.com/guide/help/fundamentals/my-tasks) list.

### Available Operations

* [get_user_task_list](#get_user_task_list) - Get a user task list
* [get_user_task_list_for_user](#get_user_task_list_for_user) - Get a user's task list

## get_user_task_list

Returns the full record for a user task list.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetUserTaskListRequest(
    opt_fields=[
        'tempora',
        'atque',
        'fugit',
        'ut',
    ],
    opt_pretty=False,
    user_task_list_gid='fugiat',
)

res = s.user_task_lists.get_user_task_list(req)

if res.get_user_task_list_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetUserTaskListRequest](../../models/operations/getusertasklistrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetUserTaskListResponse](../../models/operations/getusertasklistresponse.md)**


## get_user_task_list_for_user

Returns the full record for a user's task list.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetUserTaskListForUserRequest(
    opt_fields=[
        'culpa',
    ],
    opt_pretty=False,
    user_gid='expedita',
    workspace='magnam',
)

res = s.user_task_lists.get_user_task_list_for_user(req)

if res.get_user_task_list_for_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetUserTaskListForUserRequest](../../models/operations/getusertasklistforuserrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetUserTaskListForUserResponse](../../models/operations/getusertasklistforuserresponse.md)**

