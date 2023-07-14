# AuditLogEventContext

The context from which this event originated.


## Fields

| Field                                                                                                                                                                                         | Type                                                                                                                                                                                          | Required                                                                                                                                                                                      | Description                                                                                                                                                                                   | Example                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `api_authentication_method`                                                                                                                                                                   | [Optional[AuditLogEventContextAPIAuthenticationMethod]](../../models/shared/auditlogeventcontextapiauthenticationmethod.md)                                                                   | :heavy_minus_sign:                                                                                                                                                                            | The authentication method used in the context of an API request.<br/>Only present if the `context_type` is `api`. Can be one of `cookie`, `oauth`, `personal_access_token`, or `service_account`. |                                                                                                                                                                                               |
| `client_ip_address`                                                                                                                                                                           | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | The IP address of the client that initiated the event, if applicable.                                                                                                                         | 1.1.1.1                                                                                                                                                                                       |
| `context_type`                                                                                                                                                                                | [Optional[AuditLogEventContextContextType]](../../models/shared/auditlogeventcontextcontexttype.md)                                                                                           | :heavy_minus_sign:                                                                                                                                                                            | The type of context.<br/>Can be one of `web`, `desktop`, `mobile`, `asana_support`, `asana`, `email`, or `api`.                                                                               | web                                                                                                                                                                                           |
| `oauth_app_name`                                                                                                                                                                              | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | The name of the OAuth App that initiated the event.<br/>Only present if the `api_authentication_method` is `oauth`.                                                                           |                                                                                                                                                                                               |
| `user_agent`                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                               | :heavy_minus_sign:                                                                                                                                                                            | The user agent of the client that initiated the event, if applicable.                                                                                                                         | Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36                                                                                     |