# WorkspaceResponse

A *workspace* is the highest-level organizational unit in Asana. All projects and tasks have an associated workspace.


## Fields

| Field                                                      | Type                                                       | Required                                                   | Description                                                | Example                                                    |
| ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- | ---------------------------------------------------------- |
| `email_domains`                                            | list[*str*]                                                | :heavy_minus_sign:                                         | The email domains that are associated with this workspace. |                                                            |
| `gid`                                                      | *Optional[str]*                                            | :heavy_minus_sign:                                         | Globally unique identifier of the resource, as a string.   | 12345                                                      |
| `is_organization`                                          | *Optional[bool]*                                           | :heavy_minus_sign:                                         | Whether the workspace is an *organization*.                | false                                                      |
| `name`                                                     | *Optional[str]*                                            | :heavy_minus_sign:                                         | The name of the workspace.                                 | My Company Workspace                                       |
| `resource_type`                                            | *Optional[str]*                                            | :heavy_minus_sign:                                         | The base type of this resource.                            | task                                                       |