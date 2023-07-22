# TeamResponseOrganization

A *workspace* is the highest-level organizational unit in Asana. All projects and tasks have an associated workspace.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `gid`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | Globally unique identifier of the resource, as a string. | 12345                                                    |
| `name`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | The name of the workspace.                               | My Company Workspace                                     |
| `resource_type`                                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | The base type of this resource.                          | task                                                     |