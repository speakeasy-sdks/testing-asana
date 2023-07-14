# OrganizationExportResponse

An *organization_export* object represents a request to export the complete data of an Organization in JSON format.


## Fields

| Field                                                                                                                                                                                                                                                                                                                                                                                                  | Type                                                                                                                                                                                                                                                                                                                                                                                                   | Required                                                                                                                                                                                                                                                                                                                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                                                            | Example                                                                                                                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `created_at`                                                                                                                                                                                                                                                                                                                                                                                           | [date](https://docs.python.org/3/library/datetime.html#date-objects)                                                                                                                                                                                                                                                                                                                                   | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                     | The time at which this resource was created.                                                                                                                                                                                                                                                                                                                                                           | 2012-02-22T02:06:58.147Z                                                                                                                                                                                                                                                                                                                                                                               |
| `download_url`                                                                                                                                                                                                                                                                                                                                                                                         | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                     | Download this URL to retreive the full export of the organization<br/>in JSON format. It will be compressed in a gzip (.gz) container.<br/><br/>*Note: May be null if the export is still in progress or<br/>failed.  If present, this URL may only be valid for 1 hour from<br/>the time of retrieval. You should avoid persisting this URL<br/>somewhere and rather refresh on demand to ensure you do not keep<br/>stale URLs.* | https://asana-export.s3.amazonaws.com/export-4632784536274-20170127-43246.json.gz?AWSAccessKeyId=xxxxxxxx                                                                                                                                                                                                                                                                                              |
| `gid`                                                                                                                                                                                                                                                                                                                                                                                                  | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                     | Globally unique identifier of the resource, as a string.                                                                                                                                                                                                                                                                                                                                               | 12345                                                                                                                                                                                                                                                                                                                                                                                                  |
| `organization`                                                                                                                                                                                                                                                                                                                                                                                         | [Optional[WorkspaceCompact]](../../models/shared/workspacecompact.md)                                                                                                                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                     | N/A                                                                                                                                                                                                                                                                                                                                                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                        |
| `resource_type`                                                                                                                                                                                                                                                                                                                                                                                        | *Optional[str]*                                                                                                                                                                                                                                                                                                                                                                                        | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                     | The base type of this resource.                                                                                                                                                                                                                                                                                                                                                                        | task                                                                                                                                                                                                                                                                                                                                                                                                   |
| `state`                                                                                                                                                                                                                                                                                                                                                                                                | [Optional[OrganizationExportResponseState]](../../models/shared/organizationexportresponsestate.md)                                                                                                                                                                                                                                                                                                    | :heavy_minus_sign:                                                                                                                                                                                                                                                                                                                                                                                     | The current state of the export.                                                                                                                                                                                                                                                                                                                                                                       | started                                                                                                                                                                                                                                                                                                                                                                                                |