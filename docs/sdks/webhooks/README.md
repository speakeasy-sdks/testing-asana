# webhooks

## Overview

Webhooks allow you to subscribe to notifications about events that occur on Asana resources (e.g., tasks, projects, stories, etc.).

For a more detailed explanation of webhooks see the [overview of webhooks](/docs/overview-of-webhooks).

### Available Operations

* [create_webhook](#create_webhook) - Establish a webhook
* [delete_webhook](#delete_webhook) - Delete a webhook
* [get_webhook](#get_webhook) - Get a webhook
* [get_webhooks](#get_webhooks) - Get multiple webhooks
* [update_webhook](#update_webhook) - Update a webhook

## create_webhook

Establishing a webhook is a two-part process. First, a simple HTTP POST
request initiates the creation similar to creating any other resource.

Next, in the middle of this request comes the confirmation handshake.
When a webhook is created, we will send a test POST to the target with an
`X-Hook-Secret` header. The target must respond with a `200 OK` or `204
No Content` and a matching `X-Hook-Secret` header to confirm that this
webhook subscription is indeed expected. We strongly recommend storing
this secret to be used to verify future webhook event signatures.

The POST request to create the webhook will then return with the status
of the request. If you do not acknowledge the webhook’s confirmation
handshake it will fail to setup, and you will receive an error in
response to your attempt to create it. This means you need to be able to
receive and complete the webhook *while* the POST request is in-flight
(in other words, have a server that can handle requests asynchronously).

Invalid hostnames like localhost will recieve a 403 Forbidden status code.

```
# Request
curl -H "Authorization: Bearer <personal_access_token>" \
-X POST https://app.asana.com/api/1.0/webhooks \
-d "resource=8675309" \
-d "target=https://example.com/receive-webhook/7654"
```

```
# Handshake sent to https://example.com/
POST /receive-webhook/7654
X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81
```

```
# Handshake response sent by example.com
HTTP/1.1 200
X-Hook-Secret: b537207f20cbfa02357cf448134da559e8bd39d61597dcd5631b8012eae53e81
```

```
# Response
HTTP/1.1 201
{
  "data": {
    "gid": "43214",
    "resource": {
      "gid": "8675309",
      "name": "Bugs"
    },
    "target": "https://example.com/receive-webhook/7654",
    "active": false,
    "last_success_at": null,
    "last_failure_at": null,
    "last_failure_content": null
  }
}
```

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateWebhookRequest(
    request_body=operations.CreateWebhookRequestBody(
        data=shared.WebhookRequest(
            filters=[
                shared.WebhookRequestFilters(
                    action='changed',
                    fields_=[
                        'laborum',
                        'nam',
                        'tenetur',
                    ],
                    resource_subtype='milestone',
                    resource_type='task',
                ),
                shared.WebhookRequestFilters(
                    action='changed',
                    fields_=[
                        'alias',
                        'amet',
                    ],
                    resource_subtype='milestone',
                    resource_type='task',
                ),
                shared.WebhookRequestFilters(
                    action='changed',
                    fields_=[
                        'voluptate',
                        'unde',
                        'reiciendis',
                    ],
                    resource_subtype='milestone',
                    resource_type='task',
                ),
            ],
            resource='12345',
            target='https://example.com/receive-webhook/7654?app_specific_param=app_specific_value',
        ),
    ),
    opt_fields=[
        'repellendus',
        'delectus',
        'voluptates',
    ],
    opt_pretty=False,
)

res = s.webhooks.create_webhook(req)

if res.create_webhook_201_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.CreateWebhookRequest](../../models/operations/createwebhookrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.CreateWebhookResponse](../../models/operations/createwebhookresponse.md)**


## delete_webhook

This method *permanently* removes a webhook. Note that it may be possible to receive a request that was already in flight after deleting the webhook, but no further requests will be issued.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.DeleteWebhookRequest(
    opt_fields=[
        'est',
    ],
    opt_pretty=False,
    webhook_gid='quidem',
)

res = s.webhooks.delete_webhook(req)

if res.delete_webhook_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.DeleteWebhookRequest](../../models/operations/deletewebhookrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.DeleteWebhookResponse](../../models/operations/deletewebhookresponse.md)**


## get_webhook

Returns the full record for the given webhook.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetWebhookRequest(
    opt_fields=[
        'facere',
        'fuga',
    ],
    opt_pretty=False,
    webhook_gid='praesentium',
)

res = s.webhooks.get_webhook(req)

if res.get_webhook_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                    | Type                                                                         | Required                                                                     | Description                                                                  |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| `request`                                                                    | [operations.GetWebhookRequest](../../models/operations/getwebhookrequest.md) | :heavy_check_mark:                                                           | The request object to use for the request.                                   |


### Response

**[operations.GetWebhookResponse](../../models/operations/getwebhookresponse.md)**


## get_webhooks

Get the compact representation of all webhooks your app has registered for the authenticated user in the given workspace.

### Example Usage

```python
import testing_2
from testing_2.models import operations

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.GetWebhooksRequest(
    limit=648598,
    offset='veniam',
    opt_fields=[
        'quisquam',
    ],
    opt_pretty=False,
    resource='repudiandae',
    workspace='quasi',
)

res = s.webhooks.get_webhooks(req)

if res.get_webhooks_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                      | Type                                                                           | Required                                                                       | Description                                                                    |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| `request`                                                                      | [operations.GetWebhooksRequest](../../models/operations/getwebhooksrequest.md) | :heavy_check_mark:                                                             | The request object to use for the request.                                     |


### Response

**[operations.GetWebhooksResponse](../../models/operations/getwebhooksresponse.md)**


## update_webhook

An existing webhook's filters can be updated by making a PUT request on the URL for that webhook. Note that the webhook's previous `filters` array will be completely overwritten by the `filters` sent in the PUT request.

### Example Usage

```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.UpdateWebhookRequest(
    request_body=operations.UpdateWebhookRequestBody(
        data=shared.WebhookUpdateRequest(
            filters=[
                shared.WebhookUpdateRequestFilters(
                    action='changed',
                    fields_=[
                        'asperiores',
                        'totam',
                    ],
                    resource_subtype='milestone',
                    resource_type='task',
                ),
                shared.WebhookUpdateRequestFilters(
                    action='changed',
                    fields_=[
                        'quidem',
                        'maxime',
                    ],
                    resource_subtype='milestone',
                    resource_type='task',
                ),
                shared.WebhookUpdateRequestFilters(
                    action='changed',
                    fields_=[
                        'esse',
                    ],
                    resource_subtype='milestone',
                    resource_type='task',
                ),
            ],
        ),
    ),
    opt_fields=[
        'assumenda',
    ],
    opt_pretty=False,
    webhook_gid='ea',
)

res = s.webhooks.update_webhook(req)

if res.update_webhook_200_application_json_object is not None:
    # handle response
```

### Parameters

| Parameter                                                                          | Type                                                                               | Required                                                                           | Description                                                                        |
| ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| `request`                                                                          | [operations.UpdateWebhookRequest](../../models/operations/updatewebhookrequest.md) | :heavy_check_mark:                                                                 | The request object to use for the request.                                         |


### Response

**[operations.UpdateWebhookResponse](../../models/operations/updatewebhookresponse.md)**

