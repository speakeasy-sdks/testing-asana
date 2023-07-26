# TaskResponseAssigneeSection

A *section* is a subdivision of a project that groups tasks together. It can either be a header above a list of tasks in a list view or a column in a board view of a project.


## Fields

| Field                                                                    | Type                                                                     | Required                                                                 | Description                                                              | Example                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ | ------------------------------------------------------------------------ |
| `gid`                                                                    | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | Globally unique identifier of the resource, as a string.                 | 12345                                                                    |
| `name`                                                                   | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The name of the section (i.e. the text displayed as the section header). | Next Actions                                                             |
| `resource_type`                                                          | *Optional[str]*                                                          | :heavy_minus_sign:                                                       | The base type of this resource.                                          | task                                                                     |