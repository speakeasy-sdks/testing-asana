# GetEvents200ApplicationJSON

The full record for all events that have occurred since the sync token was created.


## Fields

| Field                                                               | Type                                                                | Required                                                            | Description                                                         | Example                                                             |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `data`                                                              | list[[shared.EventResponse](../../models/shared/eventresponse.md)]  | :heavy_minus_sign:                                                  | N/A                                                                 |                                                                     |
| `has_more`                                                          | *Optional[bool]*                                                    | :heavy_minus_sign:                                                  | Indicates whether there are more events to pull.                    | true                                                                |
| `sync`                                                              | *Optional[str]*                                                     | :heavy_minus_sign:                                                  | A sync token to be used with the next call to the /events endpoint. | de4774f6915eae04714ca93bb2f5ee81                                    |