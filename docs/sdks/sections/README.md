# sections

## Overview

A section is a subdivision of a project that groups tasks together. It can either be a header above a list of tasks in a list view or a column in a board view of a project.

Sections are largely a shared idiom in Asana’s API for both list and board views of a project regardless of the project’s layout.

The ‘memberships’ property when [getting a task](/docs/get-a-task) will return the information for the section or the column under ‘section’ in the response.

### Available Operations

* [add_task_for_section](#add_task_for_section) - Add task to section
* [create_section_for_project](#create_section_for_project) - Create a section in a project
* [delete_section](#delete_section) - Delete a section
* [get_section](#get_section) - Get a section
* [get_sections_for_project](#get_sections_for_project) - Get sections in a project
* [insert_section_for_project](#insert_section_for_project) - Move or Insert sections
* [update_section](#update_section) - Update a section

## add_task_for_section

Add a task to a specific, existing section. This will remove the task from other sections of the project.

The task will be inserted at the top of a section unless an insert_before or insert_after parameter is declared.

This does not work for separators (tasks with the resource_subtype of section).

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddTaskForSectionRequest(
    request_body=operations.AddTaskForSectionRequestBody(
        data=shared.SectionTaskInsertRequest(
            insert_after='987654',
            insert_before='86420',
            task='123456',
        ),
    ),
    opt_fields=[
        'quae',
    ],
    opt_pretty=False,
    section_gid='aut',
)

res = s.sections.add_task_for_section(req)

if res.add_task_for_section_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.AddTaskForSectionRequest](../../models/operations/addtaskforsectionrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.AddTaskForSectionResponse](../../models/operations/addtaskforsectionresponse.md)**


## create_section_for_project

Creates a new section in a project.
Returns the full record of the newly created section.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateSectionForProjectRequest(
    request_body=operations.CreateSectionForProjectRequestBody(
        data=shared.SectionRequest(
            insert_after='987654',
            insert_before='86420',
            name='Next Actions',
        ),
    ),
    opt_fields=[
        'itaque',
        'consequatur',
        'est',
    ],
    opt_pretty=False,
    project_gid='repellendus',
)

res = s.sections.create_section_for_project(req)

if res.create_section_for_project_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.CreateSectionForProjectRequest](../../models/operations/createsectionforprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.CreateSectionForProjectResponse](../../models/operations/createsectionforprojectresponse.md)**


## delete_section

A specific, existing section can be deleted by making a DELETE request on
the URL for that section.

Note that sections must be empty to be deleted.

The last remaining section cannot be deleted.

Returns an empty data block.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.DeleteSectionRequest(
    opt_fields=[
        'doloribus',
        'ut',
        'facilis',
        'cupiditate',
    ],
    opt_pretty=False,
    section_gid='qui',
)

res = s.sections.delete_section(req)

if res.delete_section_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteSectionRequest](../../models/operations/deletesectionrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DeleteSectionResponse](../../models/operations/deletesectionresponse.md)**


## get_section

Returns the complete record for a single section.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetSectionRequest(
    opt_fields=[
        'laudantium',
    ],
    opt_pretty=False,
    section_gid='odio',
)

res = s.sections.get_section(req)

if res.get_section_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetSectionRequest](../../models/operations/getsectionrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetSectionResponse](../../models/operations/getsectionresponse.md)**


## get_sections_for_project

Returns the compact records for all sections in the specified project.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetSectionsForProjectRequest(
    limit=580447,
    offset='voluptatibus',
    opt_fields=[
        'vero',
        'omnis',
        'quis',
        'ipsum',
    ],
    opt_pretty=False,
    project_gid='delectus',
)

res = s.sections.get_sections_for_project(req)

if res.get_sections_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetSectionsForProjectRequest](../../models/operations/getsectionsforprojectrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetSectionsForProjectResponse](../../models/operations/getsectionsforprojectresponse.md)**


## insert_section_for_project

Move sections relative to each other. One of
`before_section` or `after_section` is required.

Sections cannot be moved between projects.

Returns an empty data block.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.InsertSectionForProjectRequest(
    request_body=operations.InsertSectionForProjectRequestBody(
        data=shared.ProjectSectionInsertRequest(
            after_section='987654',
            before_section='86420',
            project='123456',
            section='321654',
        ),
    ),
    opt_fields=[
        'consectetur',
        'vero',
    ],
    opt_pretty=False,
    project_gid='tenetur',
)

res = s.sections.insert_section_for_project(req)

if res.insert_section_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.InsertSectionForProjectRequest](../../models/operations/insertsectionforprojectrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.InsertSectionForProjectResponse](../../models/operations/insertsectionforprojectresponse.md)**


## update_section

A specific, existing section can be updated by making a PUT request on
the URL for that project. Only the fields provided in the `data` block
will be updated; any unspecified fields will remain unchanged. (note that
at this time, the only field that can be updated is the `name` field.)

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated section record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateSectionRequest(
    request_body=operations.UpdateSectionRequestBody(
        data=shared.SectionRequest(
            insert_after='987654',
            insert_before='86420',
            name='Next Actions',
        ),
    ),
    opt_fields=[
        'hic',
        'distinctio',
    ],
    opt_pretty=False,
    section_gid='quod',
)

res = s.sections.update_section(req)

if res.update_section_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateSectionRequest](../../models/operations/updatesectionrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateSectionResponse](../../models/operations/updatesectionresponse.md)**

