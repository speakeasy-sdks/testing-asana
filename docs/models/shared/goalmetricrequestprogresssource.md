# GoalMetricRequestProgressSource

This field defines how the progress value of a goal metric is being calculated. A goal's progress can be provided manually by the user, calculated automatically from contributing subgoals or projects, or managed by an integration with an external data source, such as Salesforce.


## Values

| Name                           | Value                          |
| ------------------------------ | ------------------------------ |
| `MANUAL`                       | manual                         |
| `SUBGOAL_PROGRESS`             | subgoal_progress               |
| `PROJECT_TASK_COMPLETION`      | project_task_completion        |
| `PROJECT_MILESTONE_COMPLETION` | project_milestone_completion   |
| `EXTERNAL`                     | external                       |