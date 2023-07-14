# portfolio_memberships

## Overview

This object determines if a user is a member of a portfolio.

### Available Operations

* [get_portfolio_membership](#get_portfolio_membership) - Get a portfolio membership
* [get_portfolio_memberships](#get_portfolio_memberships) - Get multiple portfolio memberships
* [get_portfolio_memberships_for_portfolio](#get_portfolio_memberships_for_portfolio) - Get memberships from a portfolio

## get_portfolio_membership

Returns the complete portfolio record for a single portfolio membership.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetPortfolioMembershipRequest(
    opt_fields=[
        'perferendis',
        'nihil',
    ],
    opt_pretty=False,
    portfolio_membership_gid='magnam',
)

res = s.portfolio_memberships.get_portfolio_membership(req)

if res.get_portfolio_membership_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.GetPortfolioMembershipRequest](../../models/operations/getportfoliomembershiprequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.GetPortfolioMembershipResponse](../../models/operations/getportfoliomembershipresponse.md)**


## get_portfolio_memberships

Returns a list of portfolio memberships in compact representation. You must specify `portfolio`, `portfolio` and `user`, or `workspace` and `user`.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetPortfolioMembershipsRequest(
    limit=716075,
    offset='id',
    opt_fields=[
        'labore',
        'suscipit',
    ],
    opt_pretty=False,
    portfolio='natus',
    user='nobis',
    workspace='eum',
)

res = s.portfolio_memberships.get_portfolio_memberships(req)

if res.get_portfolio_memberships_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                              | Type                                                                                                   | Required                                                                                               | Description                                                                                            |
| ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `request`                                                                                              | [operations.GetPortfolioMembershipsRequest](../../models/operations/getportfoliomembershipsrequest.md) | :heavy_check_mark:                                                                                     | The request object to use for the request.                                                             |


### Response

**[operations.GetPortfolioMembershipsResponse](../../models/operations/getportfoliomembershipsresponse.md)**


## get_portfolio_memberships_for_portfolio

Returns the compact portfolio membership records for the portfolio.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetPortfolioMembershipsForPortfolioRequest(
    limit=878453,
    offset='aspernatur',
    opt_fields=[
        'magnam',
    ],
    opt_pretty=False,
    portfolio_gid='et',
    user='excepturi',
)

res = s.portfolio_memberships.get_portfolio_memberships_for_portfolio(req)

if res.get_portfolio_memberships_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                      | Type                                                                                                                           | Required                                                                                                                       | Description                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                      | [operations.GetPortfolioMembershipsForPortfolioRequest](../../models/operations/getportfoliomembershipsforportfoliorequest.md) | :heavy_check_mark:                                                                                                             | The request object to use for the request.                                                                                     |


### Response

**[operations.GetPortfolioMembershipsForPortfolioResponse](../../models/operations/getportfoliomembershipsforportfolioresponse.md)**

