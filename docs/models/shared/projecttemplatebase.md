# ProjectTemplateBase

A *project template* is an object that allows new projects to be created with a predefined setup, which may include tasks, sections, Rules, etc. It simplifies the process of running a workflow that involves a similar set of work every time.


## Fields

| Field                                                                                                                               | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `color`                                                                                                                             | [Optional[ProjectTemplateBaseColor]](../../models/shared/projecttemplatebasecolor.md)                                               | :heavy_minus_sign:                                                                                                                  | Color of the project template.                                                                                                      | light-green                                                                                                                         |
| `description`                                                                                                                       | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Free-form textual information associated with the project template                                                                  | These are things we need to pack for a trip.                                                                                        |
| `gid`                                                                                                                               | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Globally unique identifier of the resource, as a string.                                                                            | 12345                                                                                                                               |
| `html_description`                                                                                                                  | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | The description of the project template with formatting as HTML.                                                                    | <body>These are things we need to pack for a trip.</body>                                                                           |
| `name`                                                                                                                              | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | Name of the project template.                                                                                                       | Packing list                                                                                                                        |
| `owner`                                                                                                                             | [Optional[ProjectTemplateBaseOwner]](../../models/shared/projecttemplatebaseowner.md)                                               | :heavy_minus_sign:                                                                                                                  | The current owner of the project template, may be null.                                                                             |                                                                                                                                     |
| `public`                                                                                                                            | *Optional[bool]*                                                                                                                    | :heavy_minus_sign:                                                                                                                  | True if the project template is public to its team.                                                                                 | false                                                                                                                               |
| `requested_dates`                                                                                                                   | list[[DateVariableCompact](../../models/shared/datevariablecompact.md)]                                                             | :heavy_minus_sign:                                                                                                                  | Array of date variables in this project template. Calendar dates must be provided for these variables when instantiating a project. |                                                                                                                                     |
| `resource_type`                                                                                                                     | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | The base type of this resource.                                                                                                     | task                                                                                                                                |
| `team`                                                                                                                              | [Optional[TeamCompact]](../../models/shared/teamcompact.md)                                                                         | :heavy_minus_sign:                                                                                                                  | N/A                                                                                                                                 |                                                                                                                                     |