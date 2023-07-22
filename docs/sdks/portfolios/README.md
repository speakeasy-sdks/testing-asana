# portfolios

## Overview

A portfolio gives a high-level overview of the status of multiple initiatives in Asana. Portfolios provide a dashboard overview of the state of multiple projects, including a progress report and the most recent [status update](/docs/asana-statuses).
Portfolios have some restrictions on size. Each portfolio has a max of 500 items and, like projects, a maximum of 20 custom fields.

### Available Operations

* [add_custom_field_setting_for_portfolio](#add_custom_field_setting_for_portfolio) - Add a custom field to a portfolio
* [add_item_for_portfolio](#add_item_for_portfolio) - Add a portfolio item
* [add_members_for_portfolio](#add_members_for_portfolio) - Add users to a portfolio
* [create_portfolio](#create_portfolio) - Create a portfolio
* [delete_portfolio](#delete_portfolio) - Delete a portfolio
* [get_items_for_portfolio](#get_items_for_portfolio) - Get portfolio items
* [get_portfolio](#get_portfolio) - Get a portfolio
* [get_portfolios](#get_portfolios) - Get multiple portfolios
* [remove_custom_field_setting_for_portfolio](#remove_custom_field_setting_for_portfolio) - Remove a custom field from a portfolio
* [remove_item_for_portfolio](#remove_item_for_portfolio) - Remove a portfolio item
* [remove_members_for_portfolio](#remove_members_for_portfolio) - Remove users from a portfolio
* [update_portfolio](#update_portfolio) - Update a portfolio

## add_custom_field_setting_for_portfolio

Custom fields are associated with portfolios by way of custom field settings.  This method creates a setting for the portfolio.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddCustomFieldSettingForPortfolioRequest(
    request_body=operations.AddCustomFieldSettingForPortfolioRequestBody(
        data=shared.AddCustomFieldSettingRequest(
            custom_field='14916',
            insert_after='1331',
            insert_before='1331',
            is_important=True,
        ),
    ),
    opt_pretty=False,
    portfolio_gid='ullam',
)

res = s.portfolios.add_custom_field_setting_for_portfolio(req)

if res.add_custom_field_setting_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                  | Type                                                                                                                       | Required                                                                                                                   | Description                                                                                                                |
| -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                  | [operations.AddCustomFieldSettingForPortfolioRequest](../../models/operations/addcustomfieldsettingforportfoliorequest.md) | :heavy_check_mark:                                                                                                         | The request object to use for the request.                                                                                 |


### Response

**[operations.AddCustomFieldSettingForPortfolioResponse](../../models/operations/addcustomfieldsettingforportfolioresponse.md)**


## add_item_for_portfolio

Add an item to a portfolio.
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

req = operations.AddItemForPortfolioRequest(
    request_body=operations.AddItemForPortfolioRequestBody(
        data=shared.PortfolioAddItemRequest(
            insert_after='1331',
            insert_before='1331',
            item='1331',
        ),
    ),
    opt_fields=[
        'quos',
        'sint',
        'accusantium',
    ],
    opt_pretty=False,
    portfolio_gid='mollitia',
)

res = s.portfolios.add_item_for_portfolio(req)

if res.add_item_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                      | Type                                                                                           | Required                                                                                       | Description                                                                                    |
| ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `request`                                                                                      | [operations.AddItemForPortfolioRequest](../../models/operations/additemforportfoliorequest.md) | :heavy_check_mark:                                                                             | The request object to use for the request.                                                     |


### Response

**[operations.AddItemForPortfolioResponse](../../models/operations/additemforportfolioresponse.md)**


## add_members_for_portfolio

Adds the specified list of users as members of the portfolio.
Returns the updated portfolio record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.AddMembersForPortfolioRequest(
    request_body=operations.AddMembersForPortfolioRequestBody(
        data=shared.AddMembersRequest(
            members='521621,621373',
        ),
    ),
    opt_fields=[
        'mollitia',
        'ad',
        'eum',
        'dolor',
    ],
    opt_pretty=False,
    portfolio_gid='necessitatibus',
)

res = s.portfolios.add_members_for_portfolio(req)

if res.add_members_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.AddMembersForPortfolioRequest](../../models/operations/addmembersforportfoliorequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.AddMembersForPortfolioResponse](../../models/operations/addmembersforportfolioresponse.md)**


## create_portfolio

Creates a new portfolio in the given workspace with the supplied name.

Note that portfolios created in the Asana UI may have some state
(like the “Priority” custom field) which is automatically added
to the portfolio when it is created. Portfolios created via our
API will *not* be created with the same initial state to allow
integrations to create their own starting state on a portfolio.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreatePortfolioRequest(
    request_body=operations.CreatePortfolioRequestBodyInput(
        data=shared.PortfolioRequestInput(
            color=shared.PortfolioRequestColor.LIGHT_GREEN,
            name='Bug Portfolio',
            public=False,
            workspace='167589',
        ),
    ),
    opt_fields=[
        'nemo',
    ],
    opt_pretty=False,
)

res = s.portfolios.create_portfolio(req)

if res.create_portfolio_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.CreatePortfolioRequest](../../models/operations/createportfoliorequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.CreatePortfolioResponse](../../models/operations/createportfolioresponse.md)**


## delete_portfolio

An existing portfolio can be deleted by making a DELETE request on
the URL for that portfolio.

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

req = operations.DeletePortfolioRequest(
    opt_fields=[
        'iure',
    ],
    opt_pretty=False,
    portfolio_gid='doloribus',
)

res = s.portfolios.delete_portfolio(req)

if res.delete_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.DeletePortfolioRequest](../../models/operations/deleteportfoliorequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.DeletePortfolioResponse](../../models/operations/deleteportfolioresponse.md)**


## get_items_for_portfolio

Get a list of the items in compact form in a portfolio.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetItemsForPortfolioRequest(
    limit=891924,
    offset='eius',
    opt_fields=[
        'deleniti',
        'facilis',
        'in',
        'architecto',
    ],
    opt_pretty=False,
    portfolio_gid='architecto',
)

res = s.portfolios.get_items_for_portfolio(req)

if res.get_items_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                        | Type                                                                                             | Required                                                                                         | Description                                                                                      |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `request`                                                                                        | [operations.GetItemsForPortfolioRequest](../../models/operations/getitemsforportfoliorequest.md) | :heavy_check_mark:                                                                               | The request object to use for the request.                                                       |


### Response

**[operations.GetItemsForPortfolioResponse](../../models/operations/getitemsforportfolioresponse.md)**


## get_portfolio

Returns the complete portfolio record for a single portfolio.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetPortfolioRequest(
    opt_fields=[
        'ullam',
        'expedita',
        'nihil',
        'repellat',
    ],
    opt_pretty=False,
    portfolio_gid='quibusdam',
)

res = s.portfolios.get_portfolio(req)

if res.get_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                        | Type                                                                             | Required                                                                         | Description                                                                      |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| `request`                                                                        | [operations.GetPortfolioRequest](../../models/operations/getportfoliorequest.md) | :heavy_check_mark:                                                               | The request object to use for the request.                                       |


### Response

**[operations.GetPortfolioResponse](../../models/operations/getportfolioresponse.md)**


## get_portfolios

Returns a list of the portfolios in compact representation that are owned by the current API user.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetPortfoliosRequest(
    limit=149448,
    offset='saepe',
    opt_fields=[
        'accusantium',
        'consequuntur',
        'praesentium',
        'natus',
    ],
    opt_pretty=False,
    owner='magni',
    workspace='sunt',
)

res = s.portfolios.get_portfolios(req)

if res.get_portfolios_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.GetPortfoliosRequest](../../models/operations/getportfoliosrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.GetPortfoliosResponse](../../models/operations/getportfoliosresponse.md)**


## remove_custom_field_setting_for_portfolio

Removes a custom field setting from a portfolio.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveCustomFieldSettingForPortfolioRequest(
    request_body=operations.RemoveCustomFieldSettingForPortfolioRequestBody(
        data=shared.RemoveCustomFieldSettingRequest(
            custom_field='14916',
        ),
    ),
    opt_pretty=False,
    portfolio_gid='quo',
)

res = s.portfolios.remove_custom_field_setting_for_portfolio(req)

if res.remove_custom_field_setting_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                        | Type                                                                                                                             | Required                                                                                                                         | Description                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                        | [operations.RemoveCustomFieldSettingForPortfolioRequest](../../models/operations/removecustomfieldsettingforportfoliorequest.md) | :heavy_check_mark:                                                                                                               | The request object to use for the request.                                                                                       |


### Response

**[operations.RemoveCustomFieldSettingForPortfolioResponse](../../models/operations/removecustomfieldsettingforportfolioresponse.md)**


## remove_item_for_portfolio

Remove an item from a portfolio.
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

req = operations.RemoveItemForPortfolioRequest(
    request_body=operations.RemoveItemForPortfolioRequestBody(
        data=shared.PortfolioRemoveItemRequest(
            item='1331',
        ),
    ),
    opt_fields=[
        'pariatur',
        'maxime',
        'ea',
        'excepturi',
    ],
    opt_pretty=False,
    portfolio_gid='odit',
)

res = s.portfolios.remove_item_for_portfolio(req)

if res.remove_item_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                            | Type                                                                                                 | Required                                                                                             | Description                                                                                          |
| ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `request`                                                                                            | [operations.RemoveItemForPortfolioRequest](../../models/operations/removeitemforportfoliorequest.md) | :heavy_check_mark:                                                                                   | The request object to use for the request.                                                           |


### Response

**[operations.RemoveItemForPortfolioResponse](../../models/operations/removeitemforportfolioresponse.md)**


## remove_members_for_portfolio

Removes the specified list of users from members of the portfolio.
Returns the updated portfolio record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.RemoveMembersForPortfolioRequest(
    request_body=operations.RemoveMembersForPortfolioRequestBody(
        data=shared.RemoveMembersRequest(
            members='521621,621373',
        ),
    ),
    opt_fields=[
        'accusantium',
        'ab',
    ],
    opt_pretty=False,
    portfolio_gid='maiores',
)

res = s.portfolios.remove_members_for_portfolio(req)

if res.remove_members_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                  | Type                                                                                                       | Required                                                                                                   | Description                                                                                                |
| ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                  | [operations.RemoveMembersForPortfolioRequest](../../models/operations/removemembersforportfoliorequest.md) | :heavy_check_mark:                                                                                         | The request object to use for the request.                                                                 |


### Response

**[operations.RemoveMembersForPortfolioResponse](../../models/operations/removemembersforportfolioresponse.md)**


## update_portfolio

An existing portfolio can be updated by making a PUT request on the URL for
that portfolio. Only the fields provided in the `data` block will be updated;
any unspecified fields will remain unchanged.

Returns the complete updated portfolio record.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdatePortfolioRequest(
    request_body=operations.UpdatePortfolioRequestBodyInput(
        data=shared.PortfolioRequestInput(
            color=shared.PortfolioRequestColor.LIGHT_GREEN,
            name='Bug Portfolio',
            public=False,
            workspace='167589',
        ),
    ),
    opt_fields=[
        'ipsam',
        'voluptate',
        'autem',
    ],
    opt_pretty=False,
    portfolio_gid='nam',
)

res = s.portfolios.update_portfolio(req)

if res.update_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                              | Type                                                                                   | Required                                                                               | Description                                                                            |
| -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| `request`                                                                              | [operations.UpdatePortfolioRequest](../../models/operations/updateportfoliorequest.md) | :heavy_check_mark:                                                                     | The request object to use for the request.                                             |


### Response

**[operations.UpdatePortfolioResponse](../../models/operations/updateportfolioresponse.md)**

