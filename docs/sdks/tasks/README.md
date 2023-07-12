# tasks

## Overview

The task is the basic object around which many operations in Asana are centered. In the Asana application, multiple tasks populate the middle pane according to some view parameters, and the set of selected tasks determines the more detailed information presented in the details pane.

Sections are unique in that they will be included in the `memberships` field of task objects returned in the API when the task is within a section. They can also be used to manipulate the ordering of a task within a project.

[Queries](/docs/get-multiple-tasks) return a [compact representation of each task object](/docs/task-compact). To retrieve *all* fields or *specific set* of the fields, use [field selectors](/docs/input-output-options) to manipulate what data is included in a response.

### Available Operations

* [add_dependencies_for_task](#add_dependencies_for_task) - Set dependencies for a task
* [add_dependents_for_task](#add_dependents_for_task) - Set dependents for a task
* [add_followers_for_task](#add_followers_for_task) - Add followers to a task
* [add_project_for_task](#add_project_for_task) - Add a project to a task
* [add_tag_for_task](#add_tag_for_task) - Add a tag to a task
* [create_subtask_for_task](#create_subtask_for_task) - Create a subtask
* [create_task](#create_task) - Create a task
* [delete_task](#delete_task) - Delete a task
* [duplicate_task](#duplicate_task) - Duplicate a task
* [get_dependencies_for_task](#get_dependencies_for_task) - Get dependencies from a task
* [get_dependents_for_task](#get_dependents_for_task) - Get dependents from a task
* [get_subtasks_for_task](#get_subtasks_for_task) - Get subtasks from a task
* [get_task](#get_task) - Get a task
* [get_tasks](#get_tasks) - Get multiple tasks
* [get_tasks_for_project](#get_tasks_for_project) - Get tasks from a project
* [get_tasks_for_section](#get_tasks_for_section) - Get tasks from a section
* [get_tasks_for_tag](#get_tasks_for_tag) - Get tasks from a tag
* [get_tasks_for_user_task_list](#get_tasks_for_user_task_list) - Get tasks from a user task list
* [remove_dependencies_for_task](#remove_dependencies_for_task) - Unlink dependencies from a task
* [remove_dependents_for_task](#remove_dependents_for_task) - Unlink dependents from a task
* [remove_follower_for_task](#remove_follower_for_task) - Remove followers from a task
* [remove_project_for_task](#remove_project_for_task) - Remove a project from a task
* [remove_tag_for_task](#remove_tag_for_task) - Remove a tag from a task
* [search_tasks_for_workspace](#search_tasks_for_workspace) - Search tasks in a workspace
* [set_parent_for_task](#set_parent_for_task) - Set the parent of a task
* [update_task](#update_task) - Update a task

## add_dependencies_for_task

Marks a set of tasks as dependencies of this task, if they are not already dependencies. *A task can have at most 30 dependents and dependencies combined*.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddDependenciesForTaskRequest(
    request_body=operations.AddDependenciesForTaskRequestBody(
        data=shared.ModifyDependenciesRequest(
            dependencies=[
                'fugiat',
                'ut',
                'eum',
            ],
        ),
    ),
    opt_fields=[
        'assumenda',
        'eos',
    ],
    opt_pretty=False,
    task_gid='praesentium',
)

res = s.tasks.add_dependencies_for_task(req)

if res.add_dependencies_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.AddDependenciesForTaskRequest](../../models/operations/adddependenciesfortaskrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.AddDependenciesForTaskResponse](../../models/operations/adddependenciesfortaskresponse.md)**


## add_dependents_for_task

Marks a set of tasks as dependents of this task, if they are not already dependents. *A task can have at most 30 dependents and dependencies combined*.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddDependentsForTaskRequest(
    request_body=operations.AddDependentsForTaskRequestBody(
        data=shared.ModifyDependentsRequest(
            dependents=[
                'veritatis',
                'ipsa',
                'id',
                'quidem',
            ],
        ),
    ),
    opt_fields=[
        'quo',
    ],
    opt_pretty=False,
    task_gid='illum',
)

res = s.tasks.add_dependents_for_task(req)

if res.add_dependents_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.AddDependentsForTaskRequest](../../models/operations/adddependentsfortaskrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.AddDependentsForTaskResponse](../../models/operations/adddependentsfortaskresponse.md)**


## add_followers_for_task

Adds followers to a task. Returns an empty data block.
Each task can be associated with zero or more followers in the system.
Requests to add/remove followers, if successful, will return the complete updated task record, described above.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddFollowersForTaskRequest(
    request_body=operations.AddFollowersForTaskRequestBody(
        data=shared.TaskAddFollowersRequest(
            followers=[
                'fuga',
                'eius',
                'eos',
                'voluptas',
            ],
        ),
    ),
    opt_fields=[
        'cupiditate',
    ],
    opt_pretty=False,
    task_gid='consequatur',
)

res = s.tasks.add_followers_for_task(req)

if res.add_followers_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.AddFollowersForTaskRequest](../../models/operations/addfollowersfortaskrequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.AddFollowersForTaskResponse](../../models/operations/addfollowersfortaskresponse.md)**


## add_project_for_task

Adds the task to the specified project, in the optional location
specified. If no location arguments are given, the task will be added to
the end of the project.

`addProject` can also be used to reorder a task within a project or
section that already contains it.

At most one of `insert_before`, `insert_after`, or `section` should be
specified. Inserting into a section in an non-order-dependent way can be
done by specifying section, otherwise, to insert within a section in a
particular place, specify `insert_before` or `insert_after` and a task
within the section to anchor the position of this task.

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

req = operations.AddProjectForTaskRequest(
    request_body=operations.AddProjectForTaskRequestBody(
        data=shared.TaskAddProjectRequest(
            insert_after='124816',
            insert_before='432134',
            project='13579',
            section='987654',
        ),
    ),
    opt_fields=[
        'debitis',
        'ipsam',
    ],
    opt_pretty=False,
    task_gid='aspernatur',
)

res = s.tasks.add_project_for_task(req)

if res.add_project_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                  | Type                                                                                       | Required                                                                                   | Description                                                                                |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| `request`                                                                                  | [operations.AddProjectForTaskRequest](../../models/operations/addprojectfortaskrequest.md) | :heavy_check_mark:                                                                         | The request object to use for the request.                                                 |


### Response

**[operations.AddProjectForTaskResponse](../../models/operations/addprojectfortaskresponse.md)**


## add_tag_for_task

Adds a tag to a task. Returns an empty data block.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddTagForTaskRequest(
    request_body=operations.AddTagForTaskRequestBody(
        data=shared.TaskAddTagRequest(
            tag='13579',
        ),
    ),
    opt_fields=[
        'quo',
    ],
    opt_pretty=False,
    task_gid='esse',
)

res = s.tasks.add_tag_for_task(req)

if res.add_tag_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.AddTagForTaskRequest](../../models/operations/addtagfortaskrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.AddTagForTaskResponse](../../models/operations/addtagfortaskresponse.md)**


## create_subtask_for_task

Creates a new subtask and adds it to the parent task. Returns the full record for the newly created subtask.

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

req = operations.CreateSubtaskForTaskRequest(
    request_body=operations.CreateSubtaskForTaskRequestBodyInput(
        data=shared.TaskRequestInput(
            approval_status=shared.TaskRequestApprovalStatus.PENDING,
            assignee='12345',
            assignee_section='12345',
            assignee_status=shared.TaskRequestAssigneeStatus.UPCOMING,
            completed=False,
            completed_by=shared.UserCompactInput(
                name='Greg Sanchez',
            ),
            custom_fields={
                "aperiam": 'distinctio',
                "quod": 'dignissimos',
                "inventore": 'nihil',
                "totam": 'accusamus',
            },
            due_at=dateutil.parser.parse('2019-09-15T02:06:58.147Z').date(),
            due_on=dateutil.parser.parse('2019-09-15').date(),
            external=shared.TaskRequestExternal(
                data='A blob of information.',
                gid='1234',
            ),
            followers=[
                'odio',
                'occaecati',
            ],
            html_notes='<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>',
            liked=True,
            name='Bug Task',
            notes='Mittens really likes the stuff from Humboldt.',
            parent='12345',
            projects=[
                'sapiente',
                'dolores',
            ],
            resource_subtype=shared.TaskRequestResourceSubtype.DEFAULT_TASK,
            start_at=dateutil.parser.parse('2019-09-14T02:06:58.147Z').date(),
            start_on=dateutil.parser.parse('2019-09-14').date(),
            tags=[
                'molestiae',
                'accusantium',
                'porro',
            ],
            workspace='12345',
        ),
    ),
    opt_fields=[
        'quas',
        'praesentium',
    ],
    opt_pretty=False,
    task_gid='consequuntur',
)

res = s.tasks.create_subtask_for_task(req)

if res.create_subtask_for_task_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.CreateSubtaskForTaskRequest](../../models/operations/createsubtaskfortaskrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.CreateSubtaskForTaskResponse](../../models/operations/createsubtaskfortaskresponse.md)**


## create_task

Creating a new task is as easy as POSTing to the `/tasks` endpoint with a
data block containing the fields you’d like to set on the task. Any
unspecified fields will take on default values.

Every task is required to be created in a specific workspace, and this
workspace cannot be changed once set. The workspace need not be set
explicitly if you specify `projects` or a `parent` task instead.

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

req = operations.CreateTaskRequest(
    request_body=operations.CreateTaskRequestBodyInput(
        data=shared.TaskRequestInput(
            approval_status=shared.TaskRequestApprovalStatus.PENDING,
            assignee='12345',
            assignee_section='12345',
            assignee_status=shared.TaskRequestAssigneeStatus.UPCOMING,
            completed=False,
            completed_by=shared.UserCompactInput(
                name='Greg Sanchez',
            ),
            custom_fields={
                "fugit": 'fuga',
                "mollitia": 'incidunt',
                "atque": 'explicabo',
            },
            due_at=dateutil.parser.parse('2019-09-15T02:06:58.147Z').date(),
            due_on=dateutil.parser.parse('2019-09-15').date(),
            external=shared.TaskRequestExternal(
                data='A blob of information.',
                gid='1234',
            ),
            followers=[
                'nisi',
                'fugit',
            ],
            html_notes='<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>',
            liked=True,
            name='Bug Task',
            notes='Mittens really likes the stuff from Humboldt.',
            parent='12345',
            projects=[
                'consequuntur',
                'ratione',
                'explicabo',
                'saepe',
            ],
            resource_subtype=shared.TaskRequestResourceSubtype.DEFAULT_TASK,
            start_at=dateutil.parser.parse('2019-09-14T02:06:58.147Z').date(),
            start_on=dateutil.parser.parse('2019-09-14').date(),
            tags=[
                'atque',
                'et',
                'esse',
            ],
            workspace='12345',
        ),
    ),
    opt_fields=[
        'accusamus',
        'veritatis',
        'esse',
        'quod',
    ],
    opt_pretty=False,
)

res = s.tasks.create_task(req)

if res.create_task_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.CreateTaskRequest](../../models/operations/createtaskrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.CreateTaskResponse](../../models/operations/createtaskresponse.md)**


## delete_task

A specific, existing task can be deleted by making a DELETE request on
the URL for that task. Deleted tasks go into the “trash” of the user
making the delete request. Tasks can be recovered from the trash within a
period of 30 days; afterward they are completely removed from the system.

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

req = operations.DeleteTaskRequest(
    opt_fields=[
        'vero',
        'aliquid',
        'quasi',
    ],
    opt_pretty=False,
    task_gid='saepe',
)

res = s.tasks.delete_task(req)

if res.delete_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.DeleteTaskRequest](../../models/operations/deletetaskrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.DeleteTaskResponse](../../models/operations/deletetaskresponse.md)**


## duplicate_task

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

req = operations.DuplicateTaskRequest(
    request_body=operations.DuplicateTaskRequestBody(
        data=shared.TaskDuplicateRequest(
            include=shared.TaskDuplicateRequestInclude.TAGS,
            name='New Task Name',
        ),
    ),
    opt_fields=[
        'molestiae',
        'rerum',
        'occaecati',
    ],
    opt_pretty=False,
    task_gid='minima',
)

res = s.tasks.duplicate_task(req)

if res.duplicate_task_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DuplicateTaskRequest](../../models/operations/duplicatetaskrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DuplicateTaskResponse](../../models/operations/duplicatetaskresponse.md)**


## get_dependencies_for_task

Returns the compact representations of all of the dependencies of a task.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetDependenciesForTaskRequest(
    limit=716244,
    offset='eligendi',
    opt_fields=[
        'culpa',
    ],
    opt_pretty=False,
    task_gid='tempore',
)

res = s.tasks.get_dependencies_for_task(req)

if res.get_dependencies_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetDependenciesForTaskRequest](../../models/operations/getdependenciesfortaskrequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetDependenciesForTaskResponse](../../models/operations/getdependenciesfortaskresponse.md)**


## get_dependents_for_task

Returns the compact representations of all of the dependents of a task.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetDependentsForTaskRequest(
    limit=240020,
    offset='cumque',
    opt_fields=[
        'consequatur',
    ],
    opt_pretty=False,
    task_gid='minus',
)

res = s.tasks.get_dependents_for_task(req)

if res.get_dependents_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetDependentsForTaskRequest](../../models/operations/getdependentsfortaskrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetDependentsForTaskResponse](../../models/operations/getdependentsfortaskresponse.md)**


## get_subtasks_for_task

Returns a compact representation of all of the subtasks of a task.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetSubtasksForTaskRequest(
    limit=308286,
    offset='sapiente',
    opt_fields=[
        'esse',
    ],
    opt_pretty=False,
    task_gid='blanditiis',
)

res = s.tasks.get_subtasks_for_task(req)

if res.get_subtasks_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetSubtasksForTaskRequest](../../models/operations/getsubtasksfortaskrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetSubtasksForTaskResponse](../../models/operations/getsubtasksfortaskresponse.md)**


## get_task

Returns the complete task record for a single task.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTaskRequest(
    opt_fields=[
        'a',
        'nulla',
        'quas',
    ],
    opt_pretty=False,
    task_gid='esse',
)

res = s.tasks.get_task(req)

if res.get_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                              | Type                                                                   | Required                                                               | Description                                                            |
| ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| `request`                                                              | [operations.GetTaskRequest](../../models/operations/gettaskrequest.md) | :heavy_check_mark:                                                     | The request object to use for the request.                             |


### Response

**[operations.GetTaskResponse](../../models/operations/gettaskresponse.md)**


## get_tasks

Returns the compact task records for some filtered set of tasks. Use one or more of the parameters provided to filter the tasks returned. You must specify a `project` or `tag` if you do not specify `assignee` and `workspace`.

For more complex task retrieval, use [workspaces/{workspace_gid}/tasks/search](/docs/search-tasks-in-a-workspace).

### Example Usage

```python
import testing_2
import dateutil.parser
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTasksRequest(
    assignee='quasi',
    completed_since=dateutil.parser.isoparse('2012-02-22T02:06:58.158Z'),
    limit=951875,
    modified_since=dateutil.parser.isoparse('2021-11-06T16:50:22.586Z'),
    offset='pariatur',
    opt_fields=[
        'quia',
        'eveniet',
        'asperiores',
        'facere',
    ],
    opt_pretty=False,
    project='veritatis',
    section='consequuntur',
    workspace='quasi',
)

res = s.tasks.get_tasks(req)

if res.get_tasks_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                | Type                                                                     | Required                                                                 | Description                                                              |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `request`                                                                | [operations.GetTasksRequest](../../models/operations/gettasksrequest.md) | :heavy_check_mark:                                                       | The request object to use for the request.                               |


### Response

**[operations.GetTasksResponse](../../models/operations/gettasksresponse.md)**


## get_tasks_for_project

Returns the compact task records for all tasks within the given project, ordered by their priority within the project. Tasks can exist in more than one project at a time.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTasksForProjectRequest(
    completed_since='similique',
    limit=633608,
    offset='aliquid',
    opt_fields=[
        'quae',
        'earum',
        'vel',
        'in',
    ],
    opt_pretty=False,
    project_gid='eius',
)

res = s.tasks.get_tasks_for_project(req)

if res.get_tasks_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetTasksForProjectRequest](../../models/operations/gettasksforprojectrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetTasksForProjectResponse](../../models/operations/gettasksforprojectresponse.md)**


## get_tasks_for_section

*Board view only*: Returns the compact section records for all tasks within the given section.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTasksForSectionRequest(
    limit=727697,
    offset='illum',
    opt_fields=[
        'accusantium',
        'aliquam',
        'sapiente',
    ],
    opt_pretty=False,
    section_gid='dicta',
)

res = s.tasks.get_tasks_for_section(req)

if res.get_tasks_for_section_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                    | Type                                                                                         | Required                                                                                     | Description                                                                                  |
| -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| `request`                                                                                    | [operations.GetTasksForSectionRequest](../../models/operations/gettasksforsectionrequest.md) | :heavy_check_mark:                                                                           | The request object to use for the request.                                                   |


### Response

**[operations.GetTasksForSectionResponse](../../models/operations/gettasksforsectionresponse.md)**


## get_tasks_for_tag

Returns the compact task records for all tasks with the given tag. Tasks can have more than one tag at a time.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTasksForTagRequest(
    limit=355369,
    offset='reprehenderit',
    opt_fields=[
        'nisi',
        'aut',
    ],
    opt_pretty=False,
    tag_gid='voluptatum',
)

res = s.tasks.get_tasks_for_tag(req)

if res.get_tasks_for_tag_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTasksForTagRequest](../../models/operations/gettasksfortagrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetTasksForTagResponse](../../models/operations/gettasksfortagresponse.md)**


## get_tasks_for_user_task_list

Returns the compact list of tasks in a user’s My Tasks list.
*Note: Access control is enforced for this endpoint as with all Asana API endpoints, meaning a user’s private tasks will be filtered out if the API-authenticated user does not have access to them.*
*Note: Both complete and incomplete tasks are returned by default unless they are filtered out (for example, setting `completed_since=now` will return only incomplete tasks, which is the default view for “My Tasks” in Asana.)*

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTasksForUserTaskListRequest(
    completed_since='qui',
    limit=845358,
    offset='ex',
    opt_fields=[
        'itaque',
        'dolorum',
        'architecto',
    ],
    opt_pretty=False,
    user_task_list_gid='omnis',
)

res = s.tasks.get_tasks_for_user_task_list(req)

if res.get_tasks_for_user_task_list_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetTasksForUserTaskListRequest](../../models/operations/gettasksforusertasklistrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetTasksForUserTaskListResponse](../../models/operations/gettasksforusertasklistresponse.md)**


## remove_dependencies_for_task

Unlinks a set of dependencies from this task.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveDependenciesForTaskRequest(
    request_body=operations.RemoveDependenciesForTaskRequestBody(
        data=shared.ModifyDependenciesRequest(
            dependencies=[
                'quasi',
                'at',
                'et',
                'voluptate',
            ],
        ),
    ),
    opt_fields=[
        'minima',
    ],
    opt_pretty=False,
    task_gid='veritatis',
)

res = s.tasks.remove_dependencies_for_task(req)

if res.remove_dependencies_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.RemoveDependenciesForTaskRequest](../../models/operations/removedependenciesfortaskrequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.RemoveDependenciesForTaskResponse](../../models/operations/removedependenciesfortaskresponse.md)**


## remove_dependents_for_task

Unlinks a set of dependents from this task.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveDependentsForTaskRequest(
    request_body=operations.RemoveDependentsForTaskRequestBody(
        data=shared.ModifyDependentsRequest(
            dependents=[
                'adipisci',
            ],
        ),
    ),
    opt_fields=[
        'temporibus',
        'accusantium',
        'rem',
    ],
    opt_pretty=False,
    task_gid='aut',
)

res = s.tasks.remove_dependents_for_task(req)

if res.remove_dependents_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.RemoveDependentsForTaskRequest](../../models/operations/removedependentsfortaskrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.RemoveDependentsForTaskResponse](../../models/operations/removedependentsfortaskresponse.md)**


## remove_follower_for_task

Removes each of the specified followers from the task if they are following. Returns the complete, updated record for the affected task.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveFollowerForTaskRequest(
    request_body=operations.RemoveFollowerForTaskRequestBody(
        data=shared.TaskRemoveFollowersRequest(
            followers=[
                'eum',
                'mollitia',
                'ab',
            ],
        ),
    ),
    opt_fields=[
        'non',
        'voluptatem',
        'dolor',
    ],
    opt_pretty=False,
    task_gid='occaecati',
)

res = s.tasks.remove_follower_for_task(req)

if res.remove_follower_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.RemoveFollowerForTaskRequest](../../models/operations/removefollowerfortaskrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.RemoveFollowerForTaskResponse](../../models/operations/removefollowerfortaskresponse.md)**


## remove_project_for_task

Removes the task from the specified project. The task will still exist in
the system, but it will not be in the project anymore.

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

req = operations.RemoveProjectForTaskRequest(
    request_body=operations.RemoveProjectForTaskRequestBody(
        data=shared.TaskRemoveProjectRequest(
            project='13579',
        ),
    ),
    opt_fields=[
        'impedit',
        'explicabo',
    ],
    opt_pretty=False,
    task_gid='voluptas',
)

res = s.tasks.remove_project_for_task(req)

if res.remove_project_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.RemoveProjectForTaskRequest](../../models/operations/removeprojectfortaskrequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.RemoveProjectForTaskResponse](../../models/operations/removeprojectfortaskresponse.md)**


## remove_tag_for_task

Removes a tag from a task. Returns an empty data block.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveTagForTaskRequest(
    request_body=operations.RemoveTagForTaskRequestBody(
        data=shared.TaskRemoveTagRequest(
            tag='13579',
        ),
    ),
    opt_fields=[
        'dignissimos',
    ],
    opt_pretty=False,
    task_gid='dicta',
)

res = s.tasks.remove_tag_for_task(req)

if res.remove_tag_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.RemoveTagForTaskRequest](../../models/operations/removetagfortaskrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.RemoveTagForTaskResponse](../../models/operations/removetagfortaskresponse.md)**


## search_tasks_for_workspace

To mirror the functionality of the Asana web app's advanced search feature, the Asana API has a task search endpoint that allows you to build complex filters to find and retrieve the exact data you need.
#### Premium access
Like the Asana web product's advance search feature, this search endpoint will only be available to premium Asana users. A user is premium if any of the following is true:

- The workspace in which the search is being performed is a premium workspace - The user is a member of a premium team inside the workspace

Even if a user is only a member of a premium team inside a non-premium workspace, search will allow them to find data anywhere in the workspace, not just inside the premium team. Making a search request using credentials of a non-premium user will result in a `402 Payment Required` error.
#### Pagination
Search results are not stable; repeating the same query multiple times may return the data in a different order, even if the data do not change. Because of this, the traditional [pagination](https://developers.asana.com/docs/#pagination) available elsewhere in the Asana API is not available here. However, you can paginate manually by sorting the search results by their creation time and then modifying each subsequent query to exclude data you have already seen. Page sizes are limited to a maximum of 100 items, and can be specified by the `limit` query parameter.
#### Eventual consistency
Changes in Asana (regardless of whether they’re made though the web product or the API) are forwarded to our search infrastructure to be indexed. This process can take between 10 and 60 seconds to complete under normal operation, and longer during some production incidents. Making a change to a task that would alter its presence in a particular search query will not be reflected immediately. This is also true of the advanced search feature in the web product.
#### Rate limits
You may receive a `429 Too Many Requests` response if you hit any of our [rate limits](https://developers.asana.com/docs/#rate-limits).
#### Custom field parameters
| Parameter name | Custom field type | Accepted type |
|---|---|---|
| custom_fields.{gid}.is_set | All | Boolean |
| custom_fields.{gid}.value | Text | String |
| custom_fields.{gid}.value | Number | Number |
| custom_fields.{gid}.value | Enum | Enum option ID |
| custom_fields.{gid}.starts_with | Text only | String |
| custom_fields.{gid}.ends_with | Text only | String |
| custom_fields.{gid}.contains | Text only | String |
| custom_fields.{gid}.less_than | Number only | Number |
| custom_fields.{gid}.greater_than | Number only | Number |


For example, if the gid of the custom field is 12345, these query parameter to find tasks where it is set would be `custom_fields.12345.is_set=true`. To match an exact value for an enum custom field, use the gid of the desired enum option and not the name of the enum option: `custom_fields.12345.value=67890`.

**Not Supported**: searching for multiple exact matches of a custom field, searching for multi-enum custom field

*Note: If you specify `projects.any` and `sections.any`, you will receive tasks for the project **and** tasks for the section. If you're looking for only tasks in a section, omit the `projects.any` from the request.*

### Example Usage

```python
import testing_2
import dateutil.parser
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.SearchTasksForWorkspaceRequest(
    assigned_by_any='maiores',
    assigned_by_not='natus',
    assignee_any='velit',
    assignee_not='voluptatibus',
    commented_on_by_not='voluptas',
    completed=False,
    completed_at_after=dateutil.parser.isoparse('2022-11-12T00:03:51.639Z'),
    completed_at_before=dateutil.parser.isoparse('2022-09-09T19:48:26.093Z'),
    completed_on=dateutil.parser.parse('2022-03-03').date(),
    completed_on_after=dateutil.parser.parse('2021-05-21').date(),
    completed_on_before=dateutil.parser.parse('2022-05-12').date(),
    created_at_after=dateutil.parser.isoparse('2021-11-23T22:16:07.257Z'),
    created_at_before=dateutil.parser.isoparse('2022-09-08T20:16:51.473Z'),
    created_by_any='porro',
    created_by_not='quod',
    created_on=dateutil.parser.parse('2022-12-06').date(),
    created_on_after=dateutil.parser.parse('2022-04-26').date(),
    created_on_before=dateutil.parser.parse('2022-03-29').date(),
    due_at_after=dateutil.parser.isoparse('2022-05-14T14:45:53.115Z'),
    due_at_before=dateutil.parser.isoparse('2021-02-23T09:04:41.843Z'),
    due_on=dateutil.parser.parse('2021-04-17').date(),
    due_on_after=dateutil.parser.parse('2022-07-03').date(),
    due_on_before=dateutil.parser.parse('2022-02-22').date(),
    followers_not='labore',
    has_attachment=False,
    is_blocked=False,
    is_blocking=False,
    is_subtask=False,
    liked_by_not='possimus',
    modified_at_after=dateutil.parser.isoparse('2021-07-11T02:16:12.828Z'),
    modified_at_before=dateutil.parser.isoparse('2022-07-21T19:01:11.341Z'),
    modified_on=dateutil.parser.parse('2022-01-12').date(),
    modified_on_after=dateutil.parser.parse('2021-11-29').date(),
    modified_on_before=dateutil.parser.parse('2021-10-22').date(),
    opt_fields=[
        'cum',
    ],
    opt_pretty=False,
    portfolios_any='consectetur',
    projects_all='in',
    projects_any='exercitationem',
    projects_not='earum',
    resource_subtype=operations.SearchTasksForWorkspaceResourceSubtype.MILESTONE,
    sections_all='numquam',
    sections_any='doloribus',
    sections_not='suscipit',
    sort_ascending=False,
    sort_by=operations.SearchTasksForWorkspaceSortBy.MODIFIED_AT,
    start_on=dateutil.parser.parse('2021-03-11').date(),
    start_on_after=dateutil.parser.parse('2022-02-10').date(),
    start_on_before=dateutil.parser.parse('2022-01-03').date(),
    tags_all='adipisci',
    tags_any='non',
    tags_not='amet',
    teams_any='beatae',
    text='dignissimos',
    workspace_gid='a',
)

res = s.tasks.search_tasks_for_workspace(req)

if res.search_tasks_for_workspace_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.SearchTasksForWorkspaceRequest](../../models/operations/searchtasksforworkspacerequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.SearchTasksForWorkspaceResponse](../../models/operations/searchtasksforworkspaceresponse.md)**


## set_parent_for_task

parent, or no parent task at all. Returns an empty data block. When using `insert_before` and `insert_after`, at most one of those two options can be specified, and they must already be subtasks of the parent.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.SetParentForTaskRequest(
    request_body=operations.SetParentForTaskRequestBody(
        data=shared.TaskSetParentRequest(
            insert_after='null',
            insert_before='124816',
            parent='987654',
        ),
    ),
    opt_fields=[
        'consectetur',
        'corporis',
        'harum',
        'laboriosam',
    ],
    opt_pretty=False,
    task_gid='ipsa',
)

res = s.tasks.set_parent_for_task(req)

if res.set_parent_for_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                | Type                                                                                     | Required                                                                                 | Description                                                                              |
| ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| `request`                                                                                | [operations.SetParentForTaskRequest](../../models/operations/setparentfortaskrequest.md) | :heavy_check_mark:                                                                       | The request object to use for the request.                                               |


### Response

**[operations.SetParentForTaskResponse](../../models/operations/setparentfortaskresponse.md)**


## update_task

A specific, existing task can be updated by making a PUT request on the
URL for that task. Only the fields provided in the `data` block will be
updated; any unspecified fields will remain unchanged.

When using this method, it is best to specify only those fields you wish
to change, or else you may overwrite changes made by another user since
you last retrieved the task.

Returns the complete updated task record.

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

req = operations.UpdateTaskRequest(
    request_body=operations.UpdateTaskRequestBodyInput(
        data=shared.TaskRequestInput(
            approval_status=shared.TaskRequestApprovalStatus.PENDING,
            assignee='12345',
            assignee_section='12345',
            assignee_status=shared.TaskRequestAssigneeStatus.UPCOMING,
            completed=False,
            completed_by=shared.UserCompactInput(
                name='Greg Sanchez',
            ),
            custom_fields={
                "libero": 'vitae',
                "accusamus": 'similique',
                "tempora": 'aspernatur',
                "voluptas": 'voluptas',
            },
            due_at=dateutil.parser.parse('2019-09-15T02:06:58.147Z').date(),
            due_on=dateutil.parser.parse('2019-09-15').date(),
            external=shared.TaskRequestExternal(
                data='A blob of information.',
                gid='1234',
            ),
            followers=[
                'minima',
                'nobis',
            ],
            html_notes='<body>Mittens <em>really</em> likes the stuff from Humboldt.</body>',
            liked=True,
            name='Bug Task',
            notes='Mittens really likes the stuff from Humboldt.',
            parent='12345',
            projects=[
                'adipisci',
                'minus',
                'dolores',
            ],
            resource_subtype=shared.TaskRequestResourceSubtype.DEFAULT_TASK,
            start_at=dateutil.parser.parse('2019-09-14T02:06:58.147Z').date(),
            start_on=dateutil.parser.parse('2019-09-14').date(),
            tags=[
                'in',
                'dolore',
                'aliquam',
            ],
            workspace='12345',
        ),
    ),
    opt_fields=[
        'temporibus',
        'ullam',
        'adipisci',
        'cum',
    ],
    opt_pretty=False,
    task_gid='blanditiis',
)

res = s.tasks.update_task(req)

if res.update_task_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.UpdateTaskRequest](../../models/operations/updatetaskrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.UpdateTaskResponse](../../models/operations/updatetaskresponse.md)**

