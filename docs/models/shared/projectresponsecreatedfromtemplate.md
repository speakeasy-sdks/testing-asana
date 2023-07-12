# ProjectResponseCreatedFromTemplate

A *project template* is an object that allows new projects to be created with a predefined setup, which may include tasks, sections, Rules, etc. It simplifies the process of running a workflow that involves a similar set of work every time.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `gid`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | Globally unique identifier of the resource, as a string. | 12345                                                    |
| `name`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | Name of the project template.                            | Packing list                                             |
| `resource_type`                                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | The base type of this resource.                          | task                                                     |