# WorkspaceMembershipCompact

This object determines if a user is a member of a workspace.


## Fields

| Field                                                                 | Type                                                                  | Required                                                              | Description                                                           | Example                                                               |
| --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- | --------------------------------------------------------------------- |
| `gid`                                                                 | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | Globally unique identifier of the resource, as a string.              | 12345                                                                 |
| `resource_type`                                                       | *Optional[str]*                                                       | :heavy_minus_sign:                                                    | The base type of this resource.                                       | task                                                                  |
| `user`                                                                | [Optional[UserCompact]](../../models/shared/usercompact.md)           | :heavy_minus_sign:                                                    | N/A                                                                   |                                                                       |
| `workspace`                                                           | [Optional[WorkspaceCompact]](../../models/shared/workspacecompact.md) | :heavy_minus_sign:                                                    | N/A                                                                   |                                                                       |