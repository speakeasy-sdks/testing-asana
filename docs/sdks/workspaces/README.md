# workspaces

## Overview

A *workspace* is the highest-level organizational unit in Asana. All projects and tasks have an associated workspace.

An *organization* is a special kind of workspace that represents a company. In an organization, you can group your projects into teams. You can read more about how organizations work on the Asana Guide. To tell if your workspace is an organization or not, check its `is_organization` property.

Over time, we intend to migrate most workspaces into organizations and to release more organization-specific functionality. We may eventually deprecate using workspace-based APIs for organizations. Currently, and until after some reasonable grace period following any further announcements, you can still reference organizations in any `workspace` parameter.

### Available Operations

* [add_user_for_workspace](#add_user_for_workspace) - Add a user to a workspace or organization
* [get_workspace](#get_workspace) - Get a workspace
* [get_workspaces](#get_workspaces) - Get multiple workspaces
* [remove_user_for_workspace](#remove_user_for_workspace) - Remove a user from a workspace or organization
* [update_workspace](#update_workspace) - Update a workspace

## add_user_for_workspace

Add a user to a workspace or organization.
The user can be referenced by their globally unique user ID or their email address. Returns the full user record for the invited user.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddUserForWorkspaceRequest(
    request_body=operations.AddUserForWorkspaceRequestBody(
        data=shared.WorkspaceAddUserRequest(
            user='12345',
        ),
    ),
    opt_fields=[
        'recusandae',
    ],
    opt_pretty=False,
    workspace_gid='dolorum',
)

res = s.workspaces.add_user_for_workspace(req)

if res.add_user_for_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.AddUserForWorkspaceRequest](../../models/operations/adduserforworkspacerequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.AddUserForWorkspaceResponse](../../models/operations/adduserforworkspaceresponse.md)**


## get_workspace

Returns the full workspace record for a single workspace.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetWorkspaceRequest(
    opt_fields=[
        'labore',
        'reiciendis',
        'doloremque',
        'repudiandae',
    ],
    opt_pretty=False,
    workspace_gid='dicta',
)

res = s.workspaces.get_workspace(req)

if res.get_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetWorkspaceRequest](../../models/operations/getworkspacerequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetWorkspaceResponse](../../models/operations/getworkspaceresponse.md)**


## get_workspaces

Returns the compact records for all workspaces visible to the authorized user.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetWorkspacesRequest(
    limit=36033,
    offset='beatae',
    opt_fields=[
        'enim',
    ],
    opt_pretty=False,
)

res = s.workspaces.get_workspaces(req)

if res.get_workspaces_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetWorkspacesRequest](../../models/operations/getworkspacesrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetWorkspacesResponse](../../models/operations/getworkspacesresponse.md)**


## remove_user_for_workspace

Remove a user from a workspace or organization.
The user making this call must be an admin in the workspace. The user can be referenced by their globally unique user ID or their email address.
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

req = operations.RemoveUserForWorkspaceRequest(
    request_body=operations.RemoveUserForWorkspaceRequestBody(
        data=shared.WorkspaceRemoveUserRequest(
            user='12345',
        ),
    ),
    opt_fields=[
        'velit',
        'a',
    ],
    opt_pretty=False,
    workspace_gid='molestias',
)

res = s.workspaces.remove_user_for_workspace(req)

if res.remove_user_for_workspace_204_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveUserForWorkspaceRequest](../../models/operations/removeuserforworkspacerequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.RemoveUserForWorkspaceResponse](../../models/operations/removeuserforworkspaceresponse.md)**


## update_workspace

A specific, existing workspace can be updated by making a PUT request on the URL for that workspace. Only the fields provided in the data block will be updated; any unspecified fields will remain unchanged.
Currently the only field that can be modified for a workspace is its name.
Returns the complete, updated workspace record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateWorkspaceRequest(
    request_body=operations.UpdateWorkspaceRequestBodyInput(
        data=shared.WorkspaceRequestInput(
            name='My Company Workspace',
        ),
    ),
    opt_fields=[
        'saepe',
        'consequuntur',
    ],
    opt_pretty=False,
    workspace_gid='occaecati',
)

res = s.workspaces.update_workspace(req)

if res.update_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdateWorkspaceRequest](../../models/operations/updateworkspacerequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdateWorkspaceResponse](../../models/operations/updateworkspaceresponse.md)**

