# projects

## Overview

A project represents a prioritized list of tasks in Asana or a board with columns of tasks represented as cards. A project exists in a single workspace or organization and is accessible to a subset of users in that workspace or organization, depending on its permissions.

Projects in organizations are shared with a single team. Currently, the team of a project cannot be changed via the API. Non-organization workspaces do not have teams and so you should not specify the team of project in a regular workspace.

Followers of a project are a subset of the members of that project. Followers of a project will receive all updates including tasks created, added and removed from that project. Members of the project have access to and will receive status updates of the project. Adding followers to a project will add them as members if they are not already, removing followers from a project will not affect membership.

**Note:** You can use certain project endpoints to operate on [user task lists](/docs/user-task-lists) ([My Tasks](https://asana.com/guide/help/fundamentals/my-tasks)) by substituting the `{project_gid}` with the `{user_task_list_gid}`. For example, you can perform operations on the custom fields of a [user task list](/docs/user-task-lists) by using the following projects endpoints: [Add a custom field to a project](/docs/add-a-custom-field-to-a-project), [Remove a custom field from a project](/docs/remove-a-custom-field-from-a-project) and [Get a project's custom fields](/docs/get-a-projects-custom-fields)

### Available Operations

* [add_custom_field_setting_for_project](#add_custom_field_setting_for_project) - Add a custom field to a project
* [add_followers_for_project](#add_followers_for_project) - Add followers to a project
* [add_members_for_project](#add_members_for_project) - Add users to a project
* [create_project](#create_project) - Create a project
* [create_project_for_team](#create_project_for_team) - Create a project in a team
* [create_project_for_workspace](#create_project_for_workspace) - Create a project in a workspace
* [delete_project](#delete_project) - Delete a project
* [duplicate_project](#duplicate_project) - Duplicate a project
* [get_project](#get_project) - Get a project
* [get_projects](#get_projects) - Get multiple projects
* [get_projects_for_task](#get_projects_for_task) - Get projects a task is in
* [get_projects_for_team](#get_projects_for_team) - Get a team's projects
* [get_projects_for_workspace](#get_projects_for_workspace) - Get all projects in a workspace
* [get_task_counts_for_project](#get_task_counts_for_project) - Get task count of a project
* [project_save_as_template](#project_save_as_template) - Create a project template from a project
* [remove_custom_field_setting_for_project](#remove_custom_field_setting_for_project) - Remove a custom field from a project
* [remove_followers_for_project](#remove_followers_for_project) - Remove followers from a project
* [remove_members_for_project](#remove_members_for_project) - Remove users from a project
* [update_project](#update_project) - Update a project

## add_custom_field_setting_for_project

Custom fields are associated with projects by way of custom field settings.  This method creates a setting for the project.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddCustomFieldSettingForProjectRequest(
    request_body=operations.AddCustomFieldSettingForProjectRequestBody(
        data=shared.AddCustomFieldSettingRequest(
            custom_field='14916',
            insert_after='1331',
            insert_before='1331',
            is_important=True,
        ),
    ),
    opt_pretty=False,
    project_gid='iure',
)

res = s.projects.add_custom_field_setting_for_project(req)

if res.add_custom_field_setting_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                              | Type                                                                                                                   | Required                                                                                                               | Description                                                                                                            |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                              | [operations.AddCustomFieldSettingForProjectRequest](../../models/operations/addcustomfieldsettingforprojectrequest.md) | :heavy_check_mark:                                                                                                     | The request object to use for the request.                                                                             |


### Response

**[operations.AddCustomFieldSettingForProjectResponse](../../models/operations/addcustomfieldsettingforprojectresponse.md)**


## add_followers_for_project

Adds the specified list of users as followers to the project. Followers are a subset of members who have opted in to receive "tasks added" notifications for a project. Therefore, if the users are not already members of the project, they will also become members as a result of this operation.
Returns the updated project record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddFollowersForProjectRequest(
    request_body=operations.AddFollowersForProjectRequestBody(
        data=shared.AddFollowersRequest(
            followers='521621,621373',
        ),
    ),
    opt_fields=[
        'quaerat',
        'accusamus',
    ],
    opt_pretty=False,
    project_gid='quidem',
)

res = s.projects.add_followers_for_project(req)

if res.add_followers_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.AddFollowersForProjectRequest](../../models/operations/addfollowersforprojectrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.AddFollowersForProjectResponse](../../models/operations/addfollowersforprojectresponse.md)**


## add_members_for_project

Adds the specified list of users as members of the project. Note that a user being added as a member may also be added as a *follower* as a result of this operation. This is because the user's default notification settings (i.e., in the "Notifcations" tab of "My Profile Settings") will override this endpoint's default behavior of setting "Tasks added" notifications to `false`.
Returns the updated project record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddMembersForProjectRequest(
    request_body=operations.AddMembersForProjectRequestBody(
        data=shared.AddMembersRequest(
            members='521621,621373',
        ),
    ),
    opt_fields=[
        'voluptas',
        'natus',
        'eos',
        'atque',
    ],
    opt_pretty=False,
    project_gid='sit',
)

res = s.projects.add_members_for_project(req)

if res.add_members_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.AddMembersForProjectRequest](../../models/operations/addmembersforprojectrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.AddMembersForProjectResponse](../../models/operations/addmembersforprojectresponse.md)**


## create_project

Create a new project in a workspace or team.

Every project is required to be created in a specific workspace or
organization, and this cannot be changed once set. Note that you can use
the `workspace` parameter regardless of whether or not it is an
organization.

If the workspace for your project is an organization, you must also
supply a `team` to share the project with.

Returns the full record of the newly created project.

### Example Usage

```python
import testing_2
import dateutil.parser
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateProjectRequest(
    request_body=operations.CreateProjectRequestBodyInput(
        data=shared.ProjectRequestInput(
            archived=False,
            color=shared.ProjectRequestColor.LIGHT_GREEN,
            current_status=shared.ProjectRequestCurrentStatusInput(
                author=shared.UserCompactInput(
                    name='Greg Sanchez',
                ),
                color=shared.ProjectRequestCurrentStatusColor.BLUE,
                created_by=shared.UserCompactInput(
                    name='Greg Sanchez',
                ),
                html_text='<body>The project <strong>is</strong> moving forward according to plan...</body>',
                text='The project is moving forward according to plan...',
                title='Status Update - Jun 15',
            ),
            current_status_update=shared.ProjectRequestCurrentStatusUpdateInput(
                title='Status Update - Jun 15',
            ),
            custom_fields={
                "soluta": 'dolorum',
            },
            default_view=shared.ProjectRequestDefaultView.CALENDAR,
            due_date=dateutil.parser.isoparse('2019-09-15'),
            due_on=dateutil.parser.isoparse('2019-09-15'),
            followers='12345,23456',
            html_notes='<body>These are things we need to purchase.</body>',
            is_template=False,
            name='Stuff to buy',
            notes='These are things we need to purchase.',
            owner='12345',
            public=False,
            start_on=dateutil.parser.parse('2019-09-14').date(),
            team='12345',
            workspace=shared.ProjectRequestWorkspaceInput(
                name='My Company Workspace',
            ),
        ),
    ),
    opt_fields=[
        'voluptate',
        'dolorum',
    ],
    opt_pretty=False,
)

res = s.projects.create_project(req)

if res.create_project_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateProjectRequest](../../models/operations/createprojectrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateProjectResponse](../../models/operations/createprojectresponse.md)**


## create_project_for_team

Creates a project shared with the given team.

Returns the full record of the newly created project.

### Example Usage

```python
import testing_2
import dateutil.parser
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateProjectForTeamRequest(
    request_body=operations.CreateProjectForTeamRequestBodyInput(
        data=shared.ProjectRequestInput(
            archived=False,
            color=shared.ProjectRequestColor.LIGHT_GREEN,
            current_status=shared.ProjectRequestCurrentStatusInput(
                author=shared.UserCompactInput(
                    name='Greg Sanchez',
                ),
                color=shared.ProjectRequestCurrentStatusColor.RED,
                created_by=shared.UserCompactInput(
                    name='Greg Sanchez',
                ),
                html_text='<body>The project <strong>is</strong> moving forward according to plan...</body>',
                text='The project is moving forward according to plan...',
                title='Status Update - Jun 15',
            ),
            current_status_update=shared.ProjectRequestCurrentStatusUpdateInput(
                title='Status Update - Jun 15',
            ),
            custom_fields={
                "necessitatibus": 'distinctio',
                "asperiores": 'nihil',
                "ipsum": 'voluptate',
            },
            default_view=shared.ProjectRequestDefaultView.CALENDAR,
            due_date=dateutil.parser.isoparse('2019-09-15'),
            due_on=dateutil.parser.isoparse('2019-09-15'),
            followers='12345,23456',
            html_notes='<body>These are things we need to purchase.</body>',
            is_template=False,
            name='Stuff to buy',
            notes='These are things we need to purchase.',
            owner='12345',
            public=False,
            start_on=dateutil.parser.parse('2019-09-14').date(),
            team='12345',
            workspace=shared.ProjectRequestWorkspaceInput(
                name='My Company Workspace',
            ),
        ),
    ),
    opt_fields=[
        'saepe',
        'eius',
        'aspernatur',
    ],
    opt_pretty=False,
    team_gid='perferendis',
)

res = s.projects.create_project_for_team(req)

if res.create_project_for_team_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateProjectForTeamRequest](../../models/operations/createprojectforteamrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateProjectForTeamResponse](../../models/operations/createprojectforteamresponse.md)**


## create_project_for_workspace

Returns the compact project records for all projects in the workspace.

If the workspace for your project is an organization, you must also
supply a team to share the project with.

Returns the full record of the newly created project.

### Example Usage

```python
import testing_2
import dateutil.parser
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateProjectForWorkspaceRequest(
    request_body=operations.CreateProjectForWorkspaceRequestBodyInput(
        data=shared.ProjectRequestInput(
            archived=False,
            color=shared.ProjectRequestColor.LIGHT_GREEN,
            current_status=shared.ProjectRequestCurrentStatusInput(
                author=shared.UserCompactInput(
                    name='Greg Sanchez',
                ),
                color=shared.ProjectRequestCurrentStatusColor.GREEN,
                created_by=shared.UserCompactInput(
                    name='Greg Sanchez',
                ),
                html_text='<body>The project <strong>is</strong> moving forward according to plan...</body>',
                text='The project is moving forward according to plan...',
                title='Status Update - Jun 15',
            ),
            current_status_update=shared.ProjectRequestCurrentStatusUpdateInput(
                title='Status Update - Jun 15',
            ),
            custom_fields={
                "accusamus": 'ad',
                "saepe": 'suscipit',
                "deserunt": 'provident',
                "minima": 'repellendus',
            },
            default_view=shared.ProjectRequestDefaultView.CALENDAR,
            due_date=dateutil.parser.isoparse('2019-09-15'),
            due_on=dateutil.parser.isoparse('2019-09-15'),
            followers='12345,23456',
            html_notes='<body>These are things we need to purchase.</body>',
            is_template=False,
            name='Stuff to buy',
            notes='These are things we need to purchase.',
            owner='12345',
            public=False,
            start_on=dateutil.parser.parse('2019-09-14').date(),
            team='12345',
            workspace=shared.ProjectRequestWorkspaceInput(
                name='My Company Workspace',
            ),
        ),
    ),
    opt_fields=[
        'similique',
        'alias',
        'at',
    ],
    opt_pretty=False,
    workspace_gid='quaerat',
)

res = s.projects.create_project_for_workspace(req)

if res.create_project_for_workspace_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.CreateProjectForWorkspaceRequest](../../models/operations/createprojectforworkspacerequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.CreateProjectForWorkspaceResponse](../../models/operations/createprojectforworkspaceresponse.md)**


## delete_project

A specific, existing project can be deleted by making a DELETE request on
the URL for that project.

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

req = operations.DeleteProjectRequest(
    opt_fields=[
        'vel',
        'quod',
    ],
    opt_pretty=False,
    project_gid='officiis',
)

res = s.projects.delete_project(req)

if res.delete_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteProjectRequest](../../models/operations/deleteprojectrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DeleteProjectResponse](../../models/operations/deleteprojectresponse.md)**


## duplicate_project

Creates and returns a job that will asynchronously handle the duplication.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.DuplicateProjectRequest(
    request_body=operations.DuplicateProjectRequestBody(
        data=shared.ProjectDuplicateRequest(
            include=shared.ProjectDuplicateRequestInclude.FORMS,
            name='New Project Name',
            schedule_dates=shared.ProjectDuplicateRequestScheduleDates(
                due_on='2019-05-21',
                should_skip_weekends=True,
                start_on='2019-05-21',
            ),
            team='12345',
        ),
    ),
    opt_fields=[
        'a',
        'esse',
        'harum',
    ],
    opt_pretty=False,
    project_gid='iusto',
)

res = s.projects.duplicate_project(req)

if res.duplicate_project_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.DuplicateProjectRequest](../../models/operations/duplicateprojectrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.DuplicateProjectResponse](../../models/operations/duplicateprojectresponse.md)**


## get_project

Returns the complete project record for a single project.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectRequest(
    opt_fields=[
        'quisquam',
    ],
    opt_pretty=False,
    project_gid='tenetur',
)

res = s.projects.get_project(req)

if res.get_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetProjectRequest](../../models/operations/getprojectrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetProjectResponse](../../models/operations/getprojectresponse.md)**


## get_projects

Returns the compact project records for some filtered set of projects. Use one or more of the parameters provided to filter the projects returned.
*Note: This endpoint may timeout for large domains. Try filtering by team!*

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectsRequest(
    archived=False,
    limit=229442,
    offset='tempore',
    opt_fields=[
        'numquam',
        'enim',
        'dolorem',
        'sapiente',
    ],
    opt_pretty=False,
    team='totam',
    workspace='nihil',
)

res = s.projects.get_projects(req)

if res.get_projects_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetProjectsRequest](../../models/operations/getprojectsrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetProjectsResponse](../../models/operations/getprojectsresponse.md)**


## get_projects_for_task

Returns a compact representation of all of the projects the task is in.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectsForTaskRequest(
    limit=25662,
    offset='expedita',
    opt_fields=[
        'sed',
    ],
    opt_pretty=False,
    task_gid='vel',
)

res = s.projects.get_projects_for_task(req)

if res.get_projects_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetProjectsForTaskRequest](../../models/operations/getprojectsfortaskrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetProjectsForTaskResponse](../../models/operations/getprojectsfortaskresponse.md)**


## get_projects_for_team

Returns the compact project records for all projects in the team.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectsForTeamRequest(
    archived=False,
    limit=730442,
    offset='voluptas',
    opt_fields=[
        'quam',
        'ipsum',
        'incidunt',
    ],
    opt_pretty=False,
    team_gid='qui',
)

res = s.projects.get_projects_for_team(req)

if res.get_projects_for_team_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetProjectsForTeamRequest](../../models/operations/getprojectsforteamrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetProjectsForTeamResponse](../../models/operations/getprojectsforteamresponse.md)**


## get_projects_for_workspace

Returns the compact project records for all projects in the workspace.
*Note: This endpoint may timeout for large domains. Prefer the `/teams/{team_gid}/projects` endpoint.*

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectsForWorkspaceRequest(
    archived=False,
    limit=586784,
    offset='maxime',
    opt_fields=[
        'soluta',
        'dicta',
        'laborum',
        'totam',
    ],
    opt_pretty=False,
    workspace_gid='incidunt',
)

res = s.projects.get_projects_for_workspace(req)

if res.get_projects_for_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetProjectsForWorkspaceRequest](../../models/operations/getprojectsforworkspacerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetProjectsForWorkspaceResponse](../../models/operations/getprojectsforworkspaceresponse.md)**


## get_task_counts_for_project

Get an object that holds task count fields. **All fields are excluded by default**. You must [opt in](/docs/input-output-options) using `opt_fields` to get any information from this endpoint.

This endpoint has an additional [rate limit](/docs/standard-rate-limits) and each field counts especially high against our [cost limits](/docs/cost-limits).

Milestones are just tasks, so they are included in the `num_tasks`, `num_incomplete_tasks`, and `num_completed_tasks` counts.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTaskCountsForProjectRequest(
    limit=132068,
    offset='dolores',
    opt_fields=[
        'facilis',
        'aliquid',
        'quam',
    ],
    opt_pretty=False,
    project_gid='molestias',
)

res = s.projects.get_task_counts_for_project(req)

if res.get_task_counts_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetTaskCountsForProjectRequest](../../models/operations/gettaskcountsforprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetTaskCountsForProjectResponse](../../models/operations/gettaskcountsforprojectresponse.md)**


## project_save_as_template

Creates and returns a job that will asynchronously handle the project template creation. Note that
while the resulting project template can be accessed with the API, it won't be visible in the Asana
UI until Project Templates 2.0 is launched in the app. See more in [this forum post](https://forum.asana.com/t/a-new-api-for-project-templates/156432).

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.ProjectSaveAsTemplateRequest(
    request_body=operations.ProjectSaveAsTemplateRequestBody(
        data=shared.ProjectSaveAsTemplateRequest(
            name='New Project Template',
            public=True,
            team='12345',
            workspace='12345',
        ),
    ),
    opt_fields=[
        'qui',
        'neque',
        'fugit',
        'magni',
    ],
    opt_pretty=False,
    project_gid='odio',
)

res = s.projects.project_save_as_template(req)

if res.project_save_as_template_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.ProjectSaveAsTemplateRequest](../../models/operations/projectsaveastemplaterequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.ProjectSaveAsTemplateResponse](../../models/operations/projectsaveastemplateresponse.md)**


## remove_custom_field_setting_for_project

Removes a custom field setting from a project.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveCustomFieldSettingForProjectRequest(
    request_body=operations.RemoveCustomFieldSettingForProjectRequestBody(
        data=shared.RemoveCustomFieldSettingRequest(
            custom_field='14916',
        ),
    ),
    opt_pretty=False,
    project_gid='sunt',
)

res = s.projects.remove_custom_field_setting_for_project(req)

if res.remove_custom_field_setting_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.RemoveCustomFieldSettingForProjectRequest](../../models/operations/removecustomfieldsettingforprojectrequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.RemoveCustomFieldSettingForProjectResponse](../../models/operations/removecustomfieldsettingforprojectresponse.md)**


## remove_followers_for_project

Removes the specified list of users from following the project, this will not affect project membership status.
Returns the updated project record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveFollowersForProjectRequest(
    request_body=operations.RemoveFollowersForProjectRequestBody(
        data=shared.RemoveFollowersRequest(
            followers='521621,621373',
        ),
    ),
    opt_fields=[
        'nam',
        'hic',
    ],
    opt_pretty=False,
    project_gid='voluptatem',
)

res = s.projects.remove_followers_for_project(req)

if res.remove_followers_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.RemoveFollowersForProjectRequest](../../models/operations/removefollowersforprojectrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.RemoveFollowersForProjectResponse](../../models/operations/removefollowersforprojectresponse.md)**


## remove_members_for_project

Removes the specified list of users from members of the project.
Returns the updated project record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveMembersForProjectRequest(
    request_body=operations.RemoveMembersForProjectRequestBody(
        data=shared.RemoveMembersRequest(
            members='521621,621373',
        ),
    ),
    opt_fields=[
        'soluta',
        'nobis',
        'et',
        'saepe',
    ],
    opt_pretty=False,
    project_gid='ipsum',
)

res = s.projects.remove_members_for_project(req)

if res.remove_members_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveMembersForProjectRequest](../../models/operations/removemembersforprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RemoveMembersForProjectResponse](../../models/operations/removemembersforprojectresponse.md)**


## update_project

A specific, existing project can be updated by making a PUT request on
the URL for that project. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated project record.

### Example Usage

```python
import testing_2
import dateutil.parser
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateProjectRequest(
    request_body=operations.UpdateProjectRequestBodyInput(
        data=shared.ProjectRequestInput(
            archived=False,
            color=shared.ProjectRequestColor.LIGHT_GREEN,
            current_status=shared.ProjectRequestCurrentStatusInput(
                author=shared.UserCompactInput(
                    name='Greg Sanchez',
                ),
                color=shared.ProjectRequestCurrentStatusColor.GREEN,
                created_by=shared.UserCompactInput(
                    name='Greg Sanchez',
                ),
                html_text='<body>The project <strong>is</strong> moving forward according to plan...</body>',
                text='The project is moving forward according to plan...',
                title='Status Update - Jun 15',
            ),
            current_status_update=shared.ProjectRequestCurrentStatusUpdateInput(
                title='Status Update - Jun 15',
            ),
            custom_fields={
                "quos": 'tempore',
                "cupiditate": 'aperiam',
                "delectus": 'dolorem',
            },
            default_view=shared.ProjectRequestDefaultView.CALENDAR,
            due_date=dateutil.parser.isoparse('2019-09-15'),
            due_on=dateutil.parser.isoparse('2019-09-15'),
            followers='12345,23456',
            html_notes='<body>These are things we need to purchase.</body>',
            is_template=False,
            name='Stuff to buy',
            notes='These are things we need to purchase.',
            owner='12345',
            public=False,
            start_on=dateutil.parser.parse('2019-09-14').date(),
            team='12345',
            workspace=shared.ProjectRequestWorkspaceInput(
                name='My Company Workspace',
            ),
        ),
    ),
    opt_fields=[
        'labore',
        'adipisci',
    ],
    opt_pretty=False,
    project_gid='dolorum',
)

res = s.projects.update_project(req)

if res.update_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateProjectRequest](../../models/operations/updateprojectrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateProjectResponse](../../models/operations/updateprojectresponse.md)**

