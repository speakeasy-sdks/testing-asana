# UserCompact

A *user* object represents an account in Asana that can be given access to various workspaces, projects, and tasks.


## Fields

| Field                                                            | Type                                                             | Required                                                         | Description                                                      | Example                                                          |
| ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------------------------------- |
| `gid`                                                            | *Optional[str]*                                                  | :heavy_minus_sign:                                               | Globally unique identifier of the resource, as a string.         | 12345                                                            |
| `name`                                                           | *Optional[str]*                                                  | :heavy_minus_sign:                                               | *Read-only except when same user as requester*. The user’s name. | Greg Sanchez                                                     |
| `resource_type`                                                  | *Optional[str]*                                                  | :heavy_minus_sign:                                               | The base type of this resource.                                  | task                                                             |