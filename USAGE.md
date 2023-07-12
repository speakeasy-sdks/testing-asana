<!-- Start SDK Example Usage -->
```python
import testing_2
from testing_2.models import operations, shared

s = testing_2.Testing2(
    security=shared.Security(
        oauth2="",
    ),
)

req = operations.CreateAttachmentForObjectRequest(
    attachment_request1=shared.AttachmentRequest1(
        connect_to_app=False,
        file=shared.AttachmentRequestFile(
            content='corrupti'.encode(),
            file='provident',
        ),
        name='Ellis Mitchell',
        parent='illum',
        resource_subtype=shared.AttachmentRequestResourceSubtype.EXTERNAL,
        url='vel',
    ),
    opt_fields=[
        'deserunt',
        'suscipit',
        'iure',
    ],
    opt_pretty=False,
)

res = s.attachments.create_attachment_for_object(req)

if res.create_attachment_for_object_200_application_json_object is not None:
    # handle response
```
<!-- End SDK Example Usage -->