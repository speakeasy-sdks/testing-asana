# StatusUpdateRequestInput

A *status update* is an update on the progress of a particular project, portfolio, or goal, and is sent out to all of its parent's followers when created. These updates include both text describing the update and a `status_type` intended to represent the overall state of the project.


## Fields

| Field                                                                                                          | Type                                                                                                           | Required                                                                                                       | Description                                                                                                    | Example                                                                                                        |
| -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| `html_text`                                                                                                    | *Optional[str]*                                                                                                | :heavy_minus_sign:                                                                                             | [Opt In](/docs/input-output-options). The text content of the status update with formatting as HTML.           | <body>The project <strong>is</strong> moving forward according to plan...</body>                               |
| `parent`                                                                                                       | *str*                                                                                                          | :heavy_check_mark:                                                                                             | N/A                                                                                                            |                                                                                                                |
| `status_type`                                                                                                  | [StatusUpdateRequestStatusType](../../models/shared/statusupdaterequeststatustype.md)                          | :heavy_check_mark:                                                                                             | The type associated with the status update. This represents the current state of the object this object is on. |                                                                                                                |
| `text`                                                                                                         | *str*                                                                                                          | :heavy_check_mark:                                                                                             | The text content of the status update.                                                                         | The project is moving forward according to plan...                                                             |
| `title`                                                                                                        | *Optional[str]*                                                                                                | :heavy_minus_sign:                                                                                             | The title of the status update.                                                                                | Status Update - Jun 15                                                                                         |