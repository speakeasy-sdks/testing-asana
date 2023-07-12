# goal_relationships

## Overview

A goal relationship is an object representing the relationship between a goal and another goal, a project, or a portfolio.

### Available Operations

* [add_supporting_relationship](#add_supporting_relationship) - Add a supporting goal relationship
* [get_goal_relationship](#get_goal_relationship) - Get a goal relationship
* [get_goal_relationships](#get_goal_relationships) - Get goal relationships
* [remove_supporting_relationship](#remove_supporting_relationship) - Removes a supporting goal relationship
* [update_goal_relationship](#update_goal_relationship) - Update a goal relationship

## add_supporting_relationship

Creates a goal relationship by adding a supporting resource to a given goal.

Returns the newly created goal relationship record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddSupportingRelationshipRequest(
    request_body=operations.AddSupportingRelationshipRequestBody(
        data=shared.GoalAddSupportingRelationshipRequest(
            contribution_weight=1,
            insert_after='1331',
            insert_before='1331',
            supporting_resource='12345',
        ),
    ),
    goal_gid='quasi',
    opt_fields=[
        'voluptatibus',
        'vero',
        'nihil',
        'praesentium',
    ],
    opt_pretty=False,
)

res = s.goal_relationships.add_supporting_relationship(req)

if res.add_supporting_relationship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.AddSupportingRelationshipRequest](../../models/operations/addsupportingrelationshiprequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.AddSupportingRelationshipResponse](../../models/operations/addsupportingrelationshipresponse.md)**


## get_goal_relationship

Returns the complete updated goal relationship record for a single goal relationship.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetGoalRelationshipRequest(
    goal_relationship_gid='voluptatibus',
    opt_fields=[
        'omnis',
    ],
    opt_pretty=False,
)

res = s.goal_relationships.get_goal_relationship(req)

if res.get_goal_relationship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetGoalRelationshipRequest](../../models/operations/getgoalrelationshiprequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetGoalRelationshipResponse](../../models/operations/getgoalrelationshipresponse.md)**


## get_goal_relationships

Returns compact goal relationship records.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetGoalRelationshipsRequest(
    opt_fields=[
        'cum',
        'perferendis',
    ],
    opt_pretty=False,
    resource_subtype='doloremque',
    supported_goal='reprehenderit',
)

res = s.goal_relationships.get_goal_relationships(req)

if res.get_goal_relationships_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetGoalRelationshipsRequest](../../models/operations/getgoalrelationshipsrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetGoalRelationshipsResponse](../../models/operations/getgoalrelationshipsresponse.md)**


## remove_supporting_relationship

Removes a goal relationship for a given parent goal.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveSupportingRelationshipRequest(
    request_body=operations.RemoveSupportingRelationshipRequestBody(
        data=shared.GoalRemoveSupportingRelationshipRequest(
            supporting_resource='12345',
        ),
    ),
    goal_gid='ut',
    opt_fields=[
        'dicta',
        'corporis',
        'dolore',
        'iusto',
    ],
    opt_pretty=False,
)

res = s.goal_relationships.remove_supporting_relationship(req)

if res.remove_supporting_relationship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                        | Type                                                                                                             | Required                                                                                                         | Description                                                                                                      |
| ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                        | [operations.RemoveSupportingRelationshipRequest](../../models/operations/removesupportingrelationshiprequest.md) | :heavy_check_mark:                                                                                               | The request object to use for the request.                                                                       |


### Response

**[operations.RemoveSupportingRelationshipResponse](../../models/operations/removesupportingrelationshipresponse.md)**


## update_goal_relationship

An existing goal relationship can be updated by making a PUT request on the URL for
that goal relationship. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated goal relationship record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateGoalRelationshipRequest(
    request_body=operations.UpdateGoalRelationshipRequestBodyInput(
        data=shared.GoalRelationshipRequestInput(
            contribution_weight=1,
            supported_goal=shared.GoalRelationshipRequestSupportedGoalInput(
                name='Grow web traffic by 30%',
                owner=shared.GoalRelationshipRequestSupportedGoalOwnerInput(
                    name='Greg Sanchez',
                ),
            ),
            supporting_resource=shared.GoalRelationshipRequestSupportingResourceInput(
                name='Stuff to buy',
            ),
        ),
    ),
    goal_relationship_gid='dicta',
    opt_fields=[
        'enim',
        'accusamus',
        'commodi',
    ],
    opt_pretty=False,
)

res = s.goal_relationships.update_goal_relationship(req)

if res.update_goal_relationship_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.UpdateGoalRelationshipRequest](../../models/operations/updategoalrelationshiprequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.UpdateGoalRelationshipResponse](../../models/operations/updategoalrelationshipresponse.md)**

