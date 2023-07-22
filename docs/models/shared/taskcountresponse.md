# TaskCountResponse

A response object returned from the task count endpoint.


## Fields

| Field                                             | Type                                              | Required                                          | Description                                       | Example                                           |
| ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- | ------------------------------------------------- |
| `num_completed_milestones`                        | *Optional[int]*                                   | :heavy_minus_sign:                                | The number of completed milestones in a project.  | 3                                                 |
| `num_completed_tasks`                             | *Optional[int]*                                   | :heavy_minus_sign:                                | The number of completed tasks in a project.       | 150                                               |
| `num_incomplete_milestones`                       | *Optional[int]*                                   | :heavy_minus_sign:                                | The number of incomplete milestones in a project. | 7                                                 |
| `num_incomplete_tasks`                            | *Optional[int]*                                   | :heavy_minus_sign:                                | The number of incomplete tasks in a project.      | 50                                                |
| `num_milestones`                                  | *Optional[int]*                                   | :heavy_minus_sign:                                | The number of milestones in a project.            | 10                                                |
| `num_tasks`                                       | *Optional[int]*                                   | :heavy_minus_sign:                                | The number of tasks in a project.                 | 200                                               |