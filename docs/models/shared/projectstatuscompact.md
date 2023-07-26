# ProjectStatusCompact

*Deprecated: new integrations should prefer the `status_update` resource.*
A *project status* is an update on the progress of a particular project, and is sent out to all project followers when created. These updates include both text describing the update and a color code intended to represent the overall state of the project: "green" for projects that are on track, "yellow" for projects at risk, and "red" for projects that are behind.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `gid`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | Globally unique identifier of the resource, as a string. | 12345                                                    |
| `resource_type`                                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | The base type of this resource.                          | task                                                     |
| `title`                                                  | *Optional[str]*                                          | :heavy_minus_sign:                                       | The title of the project status update.                  | Status Update - Jun 15                                   |