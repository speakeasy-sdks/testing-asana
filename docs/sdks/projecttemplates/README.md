# project_templates

## Overview

A project template is an object that allows new projects to be created
with a predefined setup, which may include tasks, sections, rules, etc.
It simplifies the process of running a workflow that involves a similar
set of work every time.


Project templates in organizations are shared with a single team. Currently, the
team of a project template cannot be changed via the API.

### Available Operations

* [get_project_template](#get_project_template) - Get a project template
* [get_project_templates](#get_project_templates) - Get multiple project templates
* [get_project_templates_for_team](#get_project_templates_for_team) - Get a team's project templates
* [instantiate_project](#instantiate_project) - Instantiate a project from a project template

## get_project_template

Returns the complete project template record for a single project template.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectTemplateRequest(
    opt_fields=[
        'nobis',
        'libero',
        'delectus',
    ],
    opt_pretty=False,
    project_template_gid='quaerat',
)

res = s.project_templates.get_project_template(req)

if res.get_project_template_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetProjectTemplateRequest](../../models/operations/getprojecttemplaterequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetProjectTemplateResponse](../../models/operations/getprojecttemplateresponse.md)**


## get_project_templates

Returns the compact project template records for all project templates in the given team or workspace.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectTemplatesRequest(
    limit=554242,
    offset='aliquid',
    opt_fields=[
        'dolorem',
    ],
    opt_pretty=False,
    team='dolor',
    workspace='qui',
)

res = s.project_templates.get_project_templates(req)

if res.get_project_templates_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.GetProjectTemplatesRequest](../../models/operations/getprojecttemplatesrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.GetProjectTemplatesResponse](../../models/operations/getprojecttemplatesresponse.md)**


## get_project_templates_for_team

Returns the compact project template records for all project templates in the team.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetProjectTemplatesForTeamRequest(
    limit=218749,
    offset='hic',
    opt_fields=[
        'cum',
        'voluptate',
        'dignissimos',
    ],
    opt_pretty=False,
    team_gid='reiciendis',
)

res = s.project_templates.get_project_templates_for_team(req)

if res.get_project_templates_for_team_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                    | Type                                                                                                         | Required                                                                                                     | Description                                                                                                  |
| ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                    | [operations.GetProjectTemplatesForTeamRequest](../../models/operations/getprojecttemplatesforteamrequest.md) | :heavy_check_mark:                                                                                           | The request object to use for the request.                                                                   |


### Response

**[operations.GetProjectTemplatesForTeamResponse](../../models/operations/getprojecttemplatesforteamresponse.md)**


## instantiate_project

Creates and returns a job that will asynchronously handle the project instantiation.

To form this request, it is recommended to first make a request to [get a project template](/docs/get-a-project-template). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.

_Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](/docs/workspace) parameter._

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

req = operations.InstantiateProjectRequest(
    request_body=operations.InstantiateProjectRequestBody(
        data=shared.ProjectTemplateInstantiateProjectRequest(
            is_strict=True,
            name='New Project Name',
            public=True,
            requested_dates=[
                shared.DateVariableRequest(
                    gid='1',
                    value=dateutil.parser.isoparse('2022-01-01'),
                ),
            ],
            team='12345',
            workspace='12345',
        ),
    ),
    opt_fields=[
        'numquam',
        'veritatis',
        'ipsa',
    ],
    opt_pretty=False,
    project_template_gid='ipsa',
)

res = s.project_templates.instantiate_project(req)

if res.instantiate_project_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.InstantiateProjectRequest](../../models/operations/instantiateprojectrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.InstantiateProjectResponse](../../models/operations/instantiateprojectresponse.md)**

