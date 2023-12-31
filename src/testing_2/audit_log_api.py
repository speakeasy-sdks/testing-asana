"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from testing_2 import utils
from testing_2.models import errors, operations, shared
from typing import Optional

class AuditLogAPI:
    r"""Asana's audit log is an immutable log of [important events](/docs/supported-auditlogevents) in your organization's Asana instance.

    The audit log API allows you to monitor and act upon important security and compliance-related changes. Organizations might use this API endpoint to:

    * Set up proactive alerting with a Security Information and Event Management (SIEM) tool like [Splunk](https://asana.com/guide/help/api/splunk)
    * Conduct reactive investigations when a security incident takes place
    * Visualize key domain data in aggregate to identify security trends

    Note that since the API provides insight into what is happening in an Asana instance, the data is [read-only](/docs/get-audit-log-events). That is, there are no \"write\" or \"update\" endpoints for audit log events.

    Only [Service Accounts](https://asana.com/guide/help/premium/service-accounts) in [Enterprise Domains](https://asana.com/enterprise) can access audit log API endpoints. Authentication with a Service Account's [personal access token](/docs/personal-access-token) is required.

    For a full list of supported events, see [supported AuditLogEvents](/docs/supported-auditlogevents).
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_audit_log_events(self, request: operations.GetAuditLogEventsRequest) -> operations.GetAuditLogEventsResponse:
        r"""Get audit log events
        Retrieve the audit log events that have been captured in your domain.

        This endpoint will return a list of [AuditLogEvent](/docs/audit-log-event) objects, sorted by creation time in ascending order. Note that the Audit Log API captures events from October 8th, 2021 and later. Queries for events before this date will not return results.

        There are a number of query parameters (below) that can be used to filter the set of [AuditLogEvent](/docs/audit-log-event) objects that are returned in the response. Any combination of query parameters is valid. When no filters are provided, all of the events that have been captured in your domain will match.

        The list of events will always be [paginated](/docs/pagination). The default limit is 1000 events. The next set of events can be retrieved using the `offset` from the previous response. If there are no events that match the provided filters in your domain, the endpoint will return `null` for the `next_page` field. Querying again with the same filters may return new events if they were captured after the last request. Once a response includes a `next_page` with an `offset`, subsequent requests can be made with the latest `offset` to poll for new events that match the provided filters.

        When no `offset` is provided, the response will begin with the oldest events that match the provided filters. It is important to note that [AuditLogEvent](/docs/audit-log-event) objects will be permanently deleted from our systems after 90 days. If you wish to keep a permanent record of these events, we recommend using a SIEM tool to ingest and store these logs.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetAuditLogEventsRequest, base_url, '/workspaces/{workspace_gid}/audit_log_events', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetAuditLogEventsRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetAuditLogEventsResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetAuditLogEvents200ApplicationJSON])
                res.get_audit_log_events_200_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    