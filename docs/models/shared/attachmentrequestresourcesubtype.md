# AttachmentRequestResourceSubtype

The type of the attachment. Must be one of the given values. If not specified, a file attachment of type `asana` will be assumed. Note that if the value of `resource_subtype` is `external`, a `parent`, `name`, and `url` must also be provided.



## Values

| Name       | Value      |
| ---------- | ---------- |
| `ASANA`    | asana      |
| `DROPBOX`  | dropbox    |
| `GDRIVE`   | gdrive     |
| `ONEDRIVE` | onedrive   |
| `BOX`      | box        |
| `VIMEO`    | vimeo      |
| `EXTERNAL` | external   |