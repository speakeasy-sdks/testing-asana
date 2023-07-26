# EnumOptionInput

Enum options are the possible values which an enum custom field can adopt. An enum custom field must contain at least 1 enum option but no more than 500.

You can add enum options to a custom field by using the `POST /custom_fields/custom_field_gid/enum_options` endpoint.

**It is not possible to remove or delete an enum option**. Instead, enum options can be disabled by updating the `enabled` field to false with the `PUT /enum_options/enum_option_gid` endpoint. Other attributes can be updated similarly.

On creation of an enum option, `enabled` is always set to `true`, meaning the enum option is a selectable value for the custom field. Setting `enabled=false` is equivalent to “trashing” the enum option in the Asana web app within the “Edit Fields” dialog. The enum option will no longer be selectable but, if the enum option value was previously set within a task, the task will retain the value.

Enum options are an ordered list and by default new enum options are inserted at the end. Ordering in relation to existing enum options can be specified on creation by using `insert_before` or `insert_after` to reference an existing enum option. Only one of `insert_before` and `insert_after` can be provided when creating a new enum option.

An enum options list can be reordered with the `POST /custom_fields/custom_field_gid/enum_options/insert` endpoint.


## Fields

| Field                                                                      | Type                                                                       | Required                                                                   | Description                                                                | Example                                                                    |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| `color`                                                                    | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The color of the enum option. Defaults to ‘none’.                          | blue                                                                       |
| `enabled`                                                                  | *Optional[bool]*                                                           | :heavy_minus_sign:                                                         | Whether or not the enum option is a selectable value for the custom field. | true                                                                       |
| `name`                                                                     | *Optional[str]*                                                            | :heavy_minus_sign:                                                         | The name of the enum option.                                               | Low                                                                        |