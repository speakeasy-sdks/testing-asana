# AuditLogEventResource

The primary object that was affected by this event.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `email`                                                          | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The email of the resource, if applicable.                        |                                                                  |
| `gid`                                                            | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Globally unique identifier of the resource.                      | 1111                                                             |
| `name`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The name of the resource.                                        | Example Task                                                     |
| `resource_subtype`                                               | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The subtype of resource. Most resources will not have a subtype. | milestone                                                        |
| `resource_type`                                                  | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The type of resource.                                            | task                                                             |