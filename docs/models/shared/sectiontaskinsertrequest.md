# SectionTaskInsertRequest


## Fields

| Field                                                                                                                               | Type                                                                                                                                | Required                                                                                                                            | Description                                                                                                                         | Example                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `insert_after`                                                                                                                      | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | An existing task within this section after which the added task should be inserted. Cannot be provided together with insert_before. | 987654                                                                                                                              |
| `insert_before`                                                                                                                     | *Optional[str]*                                                                                                                     | :heavy_minus_sign:                                                                                                                  | An existing task within this section before which the added task should be inserted. Cannot be provided together with insert_after. | 86420                                                                                                                               |
| `task`                                                                                                                              | *str*                                                                                                                               | :heavy_check_mark:                                                                                                                  | The task to add to this section.                                                                                                    | 123456                                                                                                                              |