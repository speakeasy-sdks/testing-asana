# TeamMembershipResponse

This object represents a user's connection to a team.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 | Example                                                     |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `gid`                                                       | *Optional[str]*                                             | :heavy_minus_sign:                                          | Globally unique identifier of the resource, as a string.    | 12345                                                       |
| `is_guest`                                                  | *Optional[bool]*                                            | :heavy_minus_sign:                                          | Describes if the user is a guest in the team.               | false                                                       |
| `resource_type`                                             | *Optional[str]*                                             | :heavy_minus_sign:                                          | The base type of this resource.                             | task                                                        |
| `team`                                                      | [Optional[TeamCompact]](../../models/shared/teamcompact.md) | :heavy_minus_sign:                                          | N/A                                                         |                                                             |
| `user`                                                      | [Optional[UserCompact]](../../models/shared/usercompact.md) | :heavy_minus_sign:                                          | N/A                                                         |                                                             |