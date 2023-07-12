# jobs

## Overview

Jobs represent processes that handle asynchronous work. A job created when an endpoint requests an action that will be handled asynchronously, such as project or task duplication.

Only the creator of the duplication process can access the duplication status of the new object.

*Note*: With any work that is handled asynchronously (e.g., [project instantation from a template](/docs/instantiate-a-project-from-a-project-template), duplicating a [task](/docs/duplicate-a-task) or [project](/docs/duplicate-a-project), etc.), the *intermittent states* of newly-created objects may not be consistent. That is, object properties may return different values each time when polled until the job `status` has returned a `succeeded` value.

### Available Operations

* [get_job](#get_job) - Get a job by id

## get_job

Returns the full record for a job.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetJobRequest(
    job_gid='enim',
    opt_fields=[
        'delectus',
        'quidem',
        'provident',
        'nam',
    ],
    opt_pretty=False,
)

res = s.jobs.get_job(req)

if res.get_job_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                            | Type                                                                 | Required                                                             | Description                                                          |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `request`                                                            | [operations.GetJobRequest](../../models/operations/getjobrequest.md) | :heavy_check_mark:                                                   | The request object to use for the request.                           |


### Response

**[operations.GetJobResponse](../../models/operations/getjobresponse.md)**

