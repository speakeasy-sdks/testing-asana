# project_memberships

## Overview

With the introduction of “comment-only” projects in Asana, a user’s membership in a project comes with associated permissions. These permissions (i.e., whether a user has full access to the project or comment-only access) are accessible through the project memberships endpoints described here.

### Available Operations

* [get_project_membership](#get_project_membership) - Get a project membership
* [get_project_memberships_for_project](#get_project_memberships_for_project) - Get memberships from a project

## get_project_membership

Returns the complete project record for a single project membership.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectMembershipRequest(
    opt_fields=[
        'eaque',
        'quis',
    ],
    opt_pretty=False,
    project_membership_gid='nesciunt',
)

res = s.project_memberships.get_project_membership(req)

if res.get_project_membership_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetProjectMembershipRequest](../../models/operations/getprojectmembershiprequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetProjectMembershipResponse](../../models/operations/getprojectmembershipresponse.md)**


## get_project_memberships_for_project

Returns the compact project membership records for the project.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectMembershipsForProjectRequest(
    limit=179490,
    offset='perferendis',
    opt_fields=[
        'minus',
    ],
    opt_pretty=False,
    project_gid='quam',
    user='dolor',
)

res = s.project_memberships.get_project_memberships_for_project(req)

if res.get_project_memberships_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.GetProjectMembershipsForProjectRequest](../../models/operations/getprojectmembershipsforprojectrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.GetProjectMembershipsForProjectResponse](../../models/operations/getprojectmembershipsforprojectresponse.md)**

