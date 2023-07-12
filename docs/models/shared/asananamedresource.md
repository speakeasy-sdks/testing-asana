# AsanaNamedResource

A generic Asana Resource, containing a globally unique identifier.


## Fields

| Field                                                    | Type                                                     | Required                                                 | Description                                              | Example                                                  |
| -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- | -------------------------------------------------------- |
| `gid`                                                    | *Optional[str]*                                          | :heavy_minus_sign:                                       | Globally unique identifier of the resource, as a string. | 12345                                                    |
| `name`                                                   | *Optional[str]*                                          | :heavy_minus_sign:                                       | The name of the object.                                  | Bug Task                                                 |
| `resource_type`                                          | *Optional[str]*                                          | :heavy_minus_sign:                                       | The base type of this resource.                          | task                                                     |