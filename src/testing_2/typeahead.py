"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from testing_2 import utils
from testing_2.models import operations, shared
from typing import Optional

class Typeahead:
    r"""The typeahead search API provides search for objects from a single workspace."""
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def typeahead_for_workspace(self, request: operations.TypeaheadForWorkspaceRequest) -> operations.TypeaheadForWorkspaceResponse:
        r"""Get objects via typeahead
        Retrieves objects in the workspace based via an auto-completion/typeahead
        search algorithm. This feature is meant to provide results quickly, so do
        not rely on this API to provide extremely accurate search results. The
        result set is limited to a single page of results with a maximum size, so
        you won’t be able to fetch large numbers of results.

        The typeahead search API provides search for objects from a single
        workspace. This endpoint should be used to query for objects when
        creating an auto-completion/typeahead search feature. This API is meant
        to provide results quickly and should not be relied upon for accurate or
        exhaustive search results. The results sets are limited in size and
        cannot be paginated.

        Queries return a compact representation of each object which is typically
        the gid and name fields. Interested in a specific set of fields or all of
        the fields?! Of course you are. Use field selectors to manipulate what
        data is included in a response.

        Resources with type `user` are returned in order of most contacted to
        least contacted. This is determined by task assignments, adding the user
        to projects, and adding the user as a follower to tasks, messages,
        etc.

        Resources with type `project` are returned in order of recency. This is
        determined when the user visits the project, is added to the project, and
        completes tasks in the project.

        Resources with type `task` are returned with priority placed on tasks
        the user is following, but no guarantee on the order of those tasks.

        Resources with type `project_template` are returned with priority
        placed on favorited project templates.

        Leaving the `query` string empty or omitted will give you results, still
        following the resource ordering above. This could be used to list users or
        projects that are relevant for the requesting user's api token.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.TypeaheadForWorkspaceRequest, base_url, '/workspaces/{workspace_gid}/typeahead', request)
        headers = {}
        query_params = utils.get_query_params(operations.TypeaheadForWorkspaceRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.TypeaheadForWorkspaceResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.TypeaheadForWorkspace200ApplicationJSON])
                res.typeahead_for_workspace_200_application_json_object = out
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out

        return res

    