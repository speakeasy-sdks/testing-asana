# EnumOptionInsertRequest


## Fields

| Field                                                                                                                                                     | Type                                                                                                                                                      | Required                                                                                                                                                  | Description                                                                                                                                               | Example                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after_enum_option`                                                                                                                                       | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | An existing enum option within this custom field after which the new enum option should be inserted. Cannot be provided together with before_enum_option. | 12345                                                                                                                                                     |
| `before_enum_option`                                                                                                                                      | *Optional[str]*                                                                                                                                           | :heavy_minus_sign:                                                                                                                                        | An existing enum option within this custom field before which the new enum option should be inserted. Cannot be provided together with after_enum_option. | 12345                                                                                                                                                     |
| `enum_option`                                                                                                                                             | *str*                                                                                                                                                     | :heavy_check_mark:                                                                                                                                        | The gid of the enum option to relocate.                                                                                                                   | 97285                                                                                                                                                     |