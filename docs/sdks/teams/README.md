# teams

## Overview

A team is used to group related projects and people together within an organization. Each project in an organization is associated with a team.

### Available Operations

* [add_user_for_team](#add_user_for_team) - Add a user to a team
* [create_team](#create_team) - Create a team
* [get_team](#get_team) - Get a team
* [get_teams_for_user](#get_teams_for_user) - Get teams for a user
* [get_teams_for_workspace](#get_teams_for_workspace) - Get teams in a workspace
* [remove_user_for_team](#remove_user_for_team) - Remove a user from a team
* [update_team](#update_team) - Update a team

## add_user_for_team

The user making this call must be a member of the team in order to add others. The user being added must exist in the same organization as the team.

Returns the complete team membership record for the newly added user.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddUserForTeamRequest(
    request_body=operations.AddUserForTeamRequestBody(
        data=shared.TeamAddUserRequest(
            user='12345',
        ),
    ),
    opt_fields=[
        'voluptas',
    ],
    opt_pretty=False,
    team_gid='unde',
)

res = s.teams.add_user_for_team(req)

if res.add_user_for_team_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.AddUserForTeamRequest](../../models/operations/adduserforteamrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.AddUserForTeamResponse](../../models/operations/adduserforteamresponse.md)**


## create_team

Creates a team within the current workspace.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateTeamRequest(
    request_body=operations.CreateTeamRequestBodyInput(
        data=shared.TeamRequestInput(
            description='All developers should be members of this team.',
            html_description='<body><em>All</em> developers should be members of this team.</body>',
            name='Marketing',
            organization='123456789',
            visibility=shared.TeamRequestVisibility.SECRET,
        ),
    ),
    limit=382808,
    offset='sapiente',
    opt_fields=[
        'illo',
        'reiciendis',
        'perferendis',
        'corrupti',
    ],
    opt_pretty=False,
)

res = s.teams.create_team(req)

if res.create_team_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateTeamRequest](../../models/operations/createteamrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateTeamResponse](../../models/operations/createteamresponse.md)**


## get_team

Returns the full record for a single team.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTeamRequest(
    limit=979574,
    offset='incidunt',
    opt_fields=[
        'provident',
    ],
    opt_pretty=False,
    team_gid='eius',
)

res = s.teams.get_team(req)

if res.get_team_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetTeamRequest](../../models/operations/getteamrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetTeamResponse](../../models/operations/getteamresponse.md)**


## get_teams_for_user

Returns the compact records for all teams to which the given user is assigned.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTeamsForUserRequest(
    limit=896762,
    offset='ipsum',
    opt_fields=[
        'occaecati',
        'quos',
    ],
    opt_pretty=False,
    organization='voluptatibus',
    user_gid='tempora',
)

res = s.teams.get_teams_for_user(req)

if res.get_teams_for_user_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.GetTeamsForUserRequest](../../models/operations/getteamsforuserrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.GetTeamsForUserResponse](../../models/operations/getteamsforuserresponse.md)**


## get_teams_for_workspace

Returns the compact records for all teams in the workspace visible to the authorized user.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTeamsForWorkspaceRequest(
    limit=273009,
    offset='voluptate',
    opt_fields=[
        'ex',
        'sit',
        'non',
        'officiis',
    ],
    opt_pretty=False,
    workspace_gid='praesentium',
)

res = s.teams.get_teams_for_workspace(req)

if res.get_teams_for_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetTeamsForWorkspaceRequest](../../models/operations/getteamsforworkspacerequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetTeamsForWorkspaceResponse](../../models/operations/getteamsforworkspaceresponse.md)**


## remove_user_for_team

The user making this call must be a member of the team in order to remove themselves or others.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveUserForTeamRequest(
    request_body=operations.RemoveUserForTeamRequestBody(
        data=shared.TeamRemoveUserRequest(
            user='12345',
        ),
    ),
    opt_fields=[
        'quaerat',
        'incidunt',
        'ipsam',
    ],
    opt_pretty=False,
    team_gid='debitis',
)

res = s.teams.remove_user_for_team(req)

if res.remove_user_for_team_204_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.RemoveUserForTeamRequest](../../models/operations/removeuserforteamrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.RemoveUserForTeamResponse](../../models/operations/removeuserforteamresponse.md)**


## update_team

Updates a team within the current workspace.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateTeamRequest(
    request_body=operations.UpdateTeamRequestBodyInput(
        data=shared.TeamRequestInput(
            description='All developers should be members of this team.',
            html_description='<body><em>All</em> developers should be members of this team.</body>',
            name='Marketing',
            organization='123456789',
            visibility=shared.TeamRequestVisibility.REQUEST_TO_JOIN,
        ),
    ),
    limit=26522,
    offset='nobis',
    opt_fields=[
        'veniam',
        'minima',
        'recusandae',
    ],
    opt_pretty=False,
)

res = s.teams.update_team(req)

if res.update_team_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateTeamRequest](../../models/operations/updateteamrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateTeamResponse](../../models/operations/updateteamresponse.md)**

