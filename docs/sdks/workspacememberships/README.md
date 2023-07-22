# workspace_memberships

## Overview

This object determines if a user is a member of a workspace.

### Available Operations

* [get_workspace_membership](#get_workspace_membership) - Get a workspace membership
* [get_workspace_memberships_for_user](#get_workspace_memberships_for_user) - Get workspace memberships for a user
* [get_workspace_memberships_for_workspace](#get_workspace_memberships_for_workspace) - Get the workspace memberships for a workspace

## get_workspace_membership

Returns the complete workspace record for a single workspace membership.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetWorkspaceMembershipRequest(
    opt_fields=[
        'error',
        'officiis',
        'officiis',
    ],
    opt_pretty=False,
    workspace_membership_gid='accusamus',
)

res = s.workspace_memberships.get_workspace_membership(req)

if res.get_workspace_membership_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetWorkspaceMembershipRequest](../../models/operations/getworkspacemembershiprequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetWorkspaceMembershipResponse](../../models/operations/getworkspacemembershipresponse.md)**


## get_workspace_memberships_for_user

Returns the compact workspace membership records for the user.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetWorkspaceMembershipsForUserRequest(
    limit=618826,
    offset='minima',
    opt_fields=[
        'ex',
    ],
    opt_pretty=False,
    user_gid='maiores',
)

res = s.workspace_memberships.get_workspace_memberships_for_user(req)

if res.get_workspace_memberships_for_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                            | Type                                                                                                                 | Required                                                                                                             | Description                                                                                                          |
| -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                            | [operations.GetWorkspaceMembershipsForUserRequest](../../models/operations/getworkspacemembershipsforuserrequest.md) | :heavy_check_mark:                                                                                                   | The request object to use for the request.                                                                           |


### Response

**[operations.GetWorkspaceMembershipsForUserResponse](../../models/operations/getworkspacemembershipsforuserresponse.md)**


## get_workspace_memberships_for_workspace

Returns the compact workspace membership records for the workspace.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetWorkspaceMembershipsForWorkspaceRequest(
    limit=544647,
    offset='at',
    opt_fields=[
        'blanditiis',
        'suscipit',
        'repudiandae',
    ],
    opt_pretty=False,
    user='atque',
    workspace_gid='atque',
)

res = s.workspace_memberships.get_workspace_memberships_for_workspace(req)

if res.get_workspace_memberships_for_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetWorkspaceMembershipsForWorkspaceRequest](../../models/operations/getworkspacemembershipsforworkspacerequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetWorkspaceMembershipsForWorkspaceResponse](../../models/operations/getworkspacemembershipsforworkspaceresponse.md)**

