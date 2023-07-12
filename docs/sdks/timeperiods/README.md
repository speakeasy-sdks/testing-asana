# time_periods

## Overview

A time period is an object that represents a domain-scoped date range that can be set on [goals](/docs/goals).

### Available Operations

* [get_time_period](#get_time_period) - Get a time period
* [get_time_periods](#get_time_periods) - Get time periods

## get_time_period

Returns the full record for a single time period.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetTimePeriodRequest(
    opt_fields=[
        'nulla',
        'magni',
        'aperiam',
        'saepe',
    ],
    opt_pretty=False,
    time_period_gid='numquam',
)

res = s.time_periods.get_time_period(req)

if res.get_time_period_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetTimePeriodRequest](../../models/operations/gettimeperiodrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetTimePeriodResponse](../../models/operations/gettimeperiodresponse.md)**


## get_time_periods

Returns compact time period records.

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

req = operations.GetTimePeriodsRequest(
    end_on=dateutil.parser.parse('2022-07-22').date(),
    limit=889234,
    offset='beatae',
    opt_fields=[
        'exercitationem',
        'praesentium',
        'cum',
    ],
    opt_pretty=False,
    start_on=dateutil.parser.parse('2022-04-27').date(),
    workspace='voluptatum',
)

res = s.time_periods.get_time_periods(req)

if res.get_time_periods_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                            | Type                                                                                 | Required                                                                             | Description                                                                          |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| `request`                                                                            | [operations.GetTimePeriodsRequest](../../models/operations/gettimeperiodsrequest.md) | :heavy_check_mark:                                                                   | The request object to use for the request.                                           |


### Response

**[operations.GetTimePeriodsResponse](../../models/operations/gettimeperiodsresponse.md)**

