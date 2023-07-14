# ProjectBriefRequestInput

A *Project Brief* allows you to explain the what and why of the project to your team.


## Fields

| Field                                                                                                                                         | Type                                                                                                                                          | Required                                                                                                                                      | Description                                                                                                                                   | Example                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `html_text`                                                                                                                                   | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | HTML formatted text for the project brief.                                                                                                    | <body>This is a <strong>project brief</strong>.</body>                                                                                        |
| `text`                                                                                                                                        | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The plain text of the project brief. When writing to a project brief, you can specify either `html_text` (preferred) or `text`, but not both. | This is a project brief.                                                                                                                      |
| `title`                                                                                                                                       | *Optional[str]*                                                                                                                               | :heavy_minus_sign:                                                                                                                            | The title of the project brief.                                                                                                               | Stuff to buy — Project Brief                                                                                                                  |