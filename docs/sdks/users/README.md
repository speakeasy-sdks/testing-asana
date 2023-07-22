# users

## Overview

A user object represents an account in Asana that can be given access to various workspaces, projects, and tasks.

Like other objects in the system, users are referred to by numerical IDs. However, the special string identifier `me` can be used anywhere a user ID is accepted, to refer to the current authenticated user (e.g, `GET /users/me`).

### Available Operations

* [get_favorites_for_user](#get_favorites_for_user) - Get a user's favorites
* [get_user](#get_user) - Get a user
* [get_users](#get_users) - Get multiple users
* [get_users_for_team](#get_users_for_team) - Get users in a team
* [get_users_for_workspace](#get_users_for_workspace) - Get users in a workspace or organization

## get_favorites_for_user

Returns all of a user's favorites in the given workspace, of the given type.
Results are given in order (The same order as Asana's sidebar).

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetFavoritesForUserRequest(
    opt_fields=[
        'esse',
    ],
    opt_pretty=False,
    resource_type=operations.GetFavoritesForUserResourceType.TAG,
    user_gid='sit',
    workspace='voluptatum',
)

res = s.users.get_favorites_for_user(req)

if res.get_favorites_for_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetFavoritesForUserRequest](../../models/operations/getfavoritesforuserrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetFavoritesForUserResponse](../../models/operations/getfavoritesforuserresponse.md)**


## get_user

Returns the full user record for the single user with the provided ID.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetUserRequest(
    opt_fields=[
        'repudiandae',
        'corporis',
        'et',
    ],
    opt_pretty=False,
    user_gid='blanditiis',
)

res = s.users.get_user(req)

if res.get_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetUserRequest](../../models/operations/getuserrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetUserResponse](../../models/operations/getuserresponse.md)**


## get_users

Returns the user records for all users in all workspaces and organizations accessible to the authenticated user. Accepts an optional workspace ID parameter.
Results are sorted by user ID.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetUsersRequest(
    limit=405942,
    offset='sed',
    opt_fields=[
        'vel',
    ],
    opt_pretty=False,
    team='nostrum',
    workspace='saepe',
)

res = s.users.get_users(req)

if res.get_users_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetUsersRequest](../../models/operations/getusersrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetUsersResponse](../../models/operations/getusersresponse.md)**


## get_users_for_team

Returns the compact records for all users that are members of the team.
Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetUsersForTeamRequest(
    offset='error',
    opt_fields=[
        'incidunt',
    ],
    opt_pretty=False,
    team_gid='reiciendis',
)

res = s.users.get_users_for_team(req)

if res.get_users_for_team_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetUsersForTeamRequest](../../models/operations/getusersforteamrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetUsersForTeamResponse](../../models/operations/getusersforteamresponse.md)**


## get_users_for_workspace

Returns the compact records for all users in the specified workspace or organization.
Results are sorted alphabetically and limited to 2000. For more results use the `/users` endpoint.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetUsersForWorkspaceRequest(
    offset='dolorem',
    opt_fields=[
        'dicta',
        'architecto',
        'occaecati',
    ],
    opt_pretty=False,
    workspace_gid='labore',
)

res = s.users.get_users_for_workspace(req)

if res.get_users_for_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetUsersForWorkspaceRequest](../../models/operations/getusersforworkspacerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetUsersForWorkspaceResponse](../../models/operations/getusersforworkspaceresponse.md)**

