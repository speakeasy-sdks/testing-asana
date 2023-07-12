# goals

## Overview

A goal is an object in the goal-tracking system that helps your organization drive measurable results.

### Available Operations

* [add_followers](#add_followers) - Add a collaborator to a goal
* [create_goal](#create_goal) - Create a goal
* [create_goal_metric](#create_goal_metric) - Create a goal metric
* [delete_goal](#delete_goal) - Delete a goal
* [get_goal](#get_goal) - Get a goal
* [get_goals](#get_goals) - Get goals
* [get_parent_goals_for_goal](#get_parent_goals_for_goal) - Get parent goals from a goal
* [remove_followers](#remove_followers) - Remove a collaborator from a goal
* [update_goal](#update_goal) - Update a goal
* [update_goal_metric](#update_goal_metric) - Update a goal metric

## add_followers

Adds followers to a goal. Returns the goal the followers were added to.
Each goal can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddFollowersRequest(
    request_body=operations.AddFollowersRequestBody(
        data=shared.TaskAddFollowersRequest(
            followers=[
                'quae',
                'ipsum',
                'quidem',
                'molestias',
            ],
        ),
    ),
    goal_gid='excepturi',
    opt_fields=[
        'modi',
        'praesentium',
        'rem',
        'voluptates',
    ],
    opt_pretty=False,
)

res = s.goals.add_followers(req)

if res.add_followers_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.AddFollowersRequest](../../models/operations/addfollowersrequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.AddFollowersResponse](../../models/operations/addfollowersresponse.md)**


## create_goal

Creates a new goal in a workspace or team.

Returns the full record of the newly created goal.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateGoalRequest(
    request_body=operations.CreateGoalRequestBodyInput(
        data=shared.GoalRequestInput(
            due_on='2019-09-15',
            followers=[
                'repudiandae',
            ],
            html_notes='<body>Start building brand awareness.</body>',
            is_workspace_level=True,
            liked=False,
            name='Grow web traffic by 30%',
            notes='Start building brand awareness.',
            owner='12345',
            start_on='2019-09-14',
            status='green',
            team='12345',
            time_period='12345',
            workspace='12345',
        ),
    ),
    limit=575947,
    offset='veritatis',
    opt_fields=[
        'incidunt',
        'enim',
        'consequatur',
        'est',
    ],
    opt_pretty=False,
)

res = s.goals.create_goal(req)

if res.create_goal_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateGoalRequest](../../models/operations/creategoalrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateGoalResponse](../../models/operations/creategoalresponse.md)**


## create_goal_metric

Creates and adds a goal metric to a specified goal. Note that this replaces an existing goal metric if one already exists.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateGoalMetricRequest(
    request_body=operations.CreateGoalMetricRequestBodyInput(
        data=shared.GoalMetricRequestInput(
            currency_code='EUR',
            current_number_value=8.12,
            initial_number_value=5.2,
            precision=2,
            progress_source=shared.GoalMetricRequestProgressSource.MANUAL,
            target_number_value=10.2,
            unit=shared.GoalMetricRequestUnit.PERCENTAGE,
        ),
    ),
    goal_gid='explicabo',
    opt_fields=[
        'distinctio',
        'quibusdam',
        'labore',
    ],
    opt_pretty=False,
)

res = s.goals.create_goal_metric(req)

if res.create_goal_metric_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.CreateGoalMetricRequest](../../models/operations/creategoalmetricrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.CreateGoalMetricResponse](../../models/operations/creategoalmetricresponse.md)**


## delete_goal

A specific, existing goal can be deleted by making a DELETE request on the URL for that goal.

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

req = operations.DeleteGoalRequest(
    goal_gid='modi',
    opt_fields=[
        'aliquid',
    ],
    opt_pretty=False,
)

res = s.goals.delete_goal(req)

if res.delete_goal_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteGoalRequest](../../models/operations/deletegoalrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteGoalResponse](../../models/operations/deletegoalresponse.md)**


## get_goal

Returns the complete goal record for a single goal.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetGoalRequest(
    goal_gid='cupiditate',
    opt_fields=[
        'perferendis',
        'magni',
        'assumenda',
    ],
    opt_pretty=False,
)

res = s.goals.get_goal(req)

if res.get_goal_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetGoalRequest](../../models/operations/getgoalrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetGoalResponse](../../models/operations/getgoalresponse.md)**


## get_goals

Returns compact goal records.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetGoalsRequest(
    is_workspace_level=False,
    limit=369808,
    offset='alias',
    opt_fields=[
        'dolorum',
    ],
    opt_pretty=False,
    portfolio='excepturi',
    project='tempora',
    team='facilis',
    time_periods=[
        'labore',
        'delectus',
        'eum',
    ],
    workspace='non',
)

res = s.goals.get_goals(req)

if res.get_goals_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetGoalsRequest](../../models/operations/getgoalsrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetGoalsResponse](../../models/operations/getgoalsresponse.md)**


## get_parent_goals_for_goal

Returns a compact representation of all of the parent goals of a goal.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetParentGoalsForGoalRequest(
    goal_gid='eligendi',
    opt_fields=[
        'aliquid',
        'provident',
        'necessitatibus',
    ],
    opt_pretty=False,
)

res = s.goals.get_parent_goals_for_goal(req)

if res.get_parent_goals_for_goal_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetParentGoalsForGoalRequest](../../models/operations/getparentgoalsforgoalrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetParentGoalsForGoalResponse](../../models/operations/getparentgoalsforgoalresponse.md)**


## remove_followers

Removes followers from a goal. Returns the goal the followers were removed from.
Each goal can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveFollowersRequest(
    request_body=operations.RemoveFollowersRequestBody(
        data=shared.TaskAddFollowersRequest(
            followers=[
                'officia',
                'dolor',
                'debitis',
            ],
        ),
    ),
    goal_gid='a',
    opt_fields=[
        'in',
        'in',
        'illum',
    ],
    opt_pretty=False,
)

res = s.goals.remove_followers(req)

if res.remove_followers_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.RemoveFollowersRequest](../../models/operations/removefollowersrequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.RemoveFollowersResponse](../../models/operations/removefollowersresponse.md)**


## update_goal

An existing goal can be updated by making a PUT request on the URL for
that goal. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated goal record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateGoalRequest(
    request_body=operations.UpdateGoalRequestBodyInput(
        data=shared.GoalRequestInput(
            due_on='2019-09-15',
            followers=[
                'rerum',
                'dicta',
                'magnam',
                'cumque',
            ],
            html_notes='<body>Start building brand awareness.</body>',
            is_workspace_level=True,
            liked=False,
            name='Grow web traffic by 30%',
            notes='Start building brand awareness.',
            owner='12345',
            start_on='2019-09-14',
            status='green',
            team='12345',
            time_period='12345',
            workspace='12345',
        ),
    ),
    goal_gid='facere',
    opt_fields=[
        'aliquid',
        'laborum',
    ],
    opt_pretty=False,
)

res = s.goals.update_goal(req)

if res.update_goal_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateGoalRequest](../../models/operations/updategoalrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateGoalResponse](../../models/operations/updategoalresponse.md)**


## update_goal_metric

Updates a goal's existing metric's `current_number_value` if one exists,
otherwise responds with a 400 status code.

Returns the complete updated goal metric record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateGoalMetricRequest(
    request_body=operations.UpdateGoalMetricRequestBodyInput(
        data=shared.GoalMetricCurrentValueRequestInput(
            current_number_value=8.12,
        ),
    ),
    goal_gid='accusamus',
    opt_fields=[
        'occaecati',
    ],
    opt_pretty=False,
)

res = s.goals.update_goal_metric(req)

if res.update_goal_metric_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.UpdateGoalMetricRequest](../../models/operations/updategoalmetricrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.UpdateGoalMetricResponse](../../models/operations/updategoalmetricresponse.md)**

