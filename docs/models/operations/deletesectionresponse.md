# DeleteSectionResponse


## Fields

| Field                                                                                                                                  | Type                                                                                                                                   | Required                                                                                                                               | Description                                                                                                                            |
| -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                                         | *str*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `error_response`                                                                                                                       | [Optional[shared.ErrorResponse]](../../models/shared/errorresponse.md)                                                                 | :heavy_minus_sign:                                                                                                                     | This usually occurs because of a missing or malformed parameter. Check the documentation and the syntax of your request and try again. |
| `status_code`                                                                                                                          | *int*                                                                                                                                  | :heavy_check_mark:                                                                                                                     | N/A                                                                                                                                    |
| `raw_response`                                                                                                                         | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                                                  | :heavy_minus_sign:                                                                                                                     | N/A                                                                                                                                    |
| `delete_section_200_application_json_object`                                                                                           | [Optional[DeleteSection200ApplicationJSON]](../../models/operations/deletesection200applicationjson.md)                                | :heavy_minus_sign:                                                                                                                     | Successfully deleted the specified section.                                                                                            |