# organization_exports

## Overview

An `organization_export` object represents a request to export the complete data of an organization in JSON format.

To export an organization using this API:

* Create an `organization_export`
  [request](/docs/create-an-organization-export-request)
  and store the ID that is returned.
* Request the `organization_export` every few minutes, until the
  `state` field contains ‘finished’.
* Download the file located at the URL in the `download_url` field. * Exports can take a long time, from several minutes to a few hours
  for large organizations.


*Note: These endpoints are only available to [Service Accounts](https://asana.com/guide/help/premium/service-accounts) of an [Enterprise](https://asana.com/enterprise) organization.*

### Available Operations

* [create_organization_export](#create_organization_export) - Create an organization export request
* [get_organization_export](#get_organization_export) - Get details on an org export request

## create_organization_export

This method creates a request to export an Organization. Asana will complete the export at some point after you create the request.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateOrganizationExportRequest(
    request_body=operations.CreateOrganizationExportRequestBody(
        data=shared.OrganizationExportRequest(
            organization='1331',
        ),
    ),
    limit=659669,
    offset='blanditiis',
    opt_fields=[
        'sapiente',
        'amet',
        'deserunt',
    ],
    opt_pretty=False,
)

res = s.organization_exports.create_organization_export(req)

if res.create_organization_export_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                                | Type                                                                                                     | Required                                                                                                 | Description                                                                                              |
| -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| `request`                                                                                                | [operations.CreateOrganizationExportRequest](../../models/operations/createorganizationexportrequest.md) | :heavy_check_mark:                                                                                       | The request object to use for the request.                                                               |


### Response

**[operations.CreateOrganizationExportResponse](../../models/operations/createorganizationexportresponse.md)**


## get_organization_export

Returns details of a previously-requested Organization export.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetOrganizationExportRequest(
    opt_fields=[
        'vel',
        'natus',
    ],
    opt_pretty=False,
    organization_export_gid='omnis',
)

res = s.organization_exports.get_organization_export(req)

if res.get_organization_export_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                                          | Type                                                                                               | Required                                                                                           | Description                                                                                        |
| -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `request`                                                                                          | [operations.GetOrganizationExportRequest](../../models/operations/getorganizationexportrequest.md) | :heavy_check_mark:                                                                                 | The request object to use for the request.                                                         |


### Response

**[operations.GetOrganizationExportResponse](../../models/operations/getorganizationexportresponse.md)**

