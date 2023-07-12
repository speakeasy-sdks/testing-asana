# custom_field_settings

## Overview

Custom fields are attached to a particular project with the custom field settings resource. This resource both represents the many-to-many join of the custom field and project as well as stores information that is relevant to that particular pairing. For instance, the `is_important` property determines some possible application-specific handling of that custom field.

### Available Operations

* [get_custom_field_settings_for_portfolio](#get_custom_field_settings_for_portfolio) - Get a portfolio's custom fields
* [get_custom_field_settings_for_project](#get_custom_field_settings_for_project) - Get a project's custom fields

## get_custom_field_settings_for_portfolio

Returns a list of all of the custom fields settings on a portfolio, in compact form.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetCustomFieldSettingsForPortfolioRequest(
    limit=612096,
    offset='dolor',
    opt_fields=[
        'laboriosam',
        'hic',
        'saepe',
    ],
    opt_pretty=False,
    portfolio_gid='fuga',
)

res = s.custom_field_settings.get_custom_field_settings_for_portfolio(req)

if res.get_custom_field_settings_for_portfolio_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                    | Type                                                                                                                         | Required                                                                                                                     | Description                                                                                                                  |
| ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                                    | [operations.GetCustomFieldSettingsForPortfolioRequest](../../models/operations/getcustomfieldsettingsforportfoliorequest.md) | :heavy_check_mark:                                                                                                           | The request object to use for the request.                                                                                   |


### Response

**[operations.GetCustomFieldSettingsForPortfolioResponse](../../models/operations/getcustomfieldsettingsforportfolioresponse.md)**


## get_custom_field_settings_for_project

Returns a list of all of the custom fields settings on a project, in compact form. Note that, as in all queries to collections which return compact representation, `opt_fields` can be used to include more data than is returned in the compact representation. See the [getting started guide on input/output options](https://developers.asana.com/docs/#input-output-options) for more information.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetCustomFieldSettingsForProjectRequest(
    limit=449950,
    offset='corporis',
    opt_fields=[
        'iure',
        'saepe',
        'quidem',
    ],
    opt_pretty=False,
    project_gid='architecto',
)

res = s.custom_field_settings.get_custom_field_settings_for_project(req)

if res.get_custom_field_settings_for_project_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                                | Type                                                                                                                     | Required                                                                                                                 | Description                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| `request`                                                                                                                | [operations.GetCustomFieldSettingsForProjectRequest](../../models/operations/getcustomfieldsettingsforprojectrequest.md) | :heavy_check_mark:                                                                                                       | The request object to use for the request.                                                                               |


### Response

**[operations.GetCustomFieldSettingsForProjectResponse](../../models/operations/getcustomfieldsettingsforprojectresponse.md)**

