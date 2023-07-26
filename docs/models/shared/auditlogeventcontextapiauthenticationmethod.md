# AuditLogEventContextAPIAuthenticationMethod

The authentication method used in the context of an API request.
Only present if the `context_type` is `api`. Can be one of `cookie`, `oauth`, `personal_access_token`, or `service_account`.


## Values

| Name                    | Value                   |
| ----------------------- | ----------------------- |
| `COOKIE`                | cookie                  |
| `OAUTH`                 | oauth                   |
| `PERSONAL_ACCESS_TOKEN` | personal_access_token   |
| `SERVICE_ACCOUNT`       | service_account         |