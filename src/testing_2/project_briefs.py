"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from testing_2 import utils
from testing_2.models import errors, operations, shared
from typing import Optional

class ProjectBriefs:
    r"""A project brief object represents a rich text document that describes a project.

    Please note that this API is in *preview*, and is expected to change. This API is to be used for development and testing only as an advance view into the upcoming rich text format experience in the task description. For more information, see [this post](https://forum.asana.com/t/project-brief-api-now-available-as-a-preview/150885) in the developer forum.
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def create_project_brief(self, request: operations.CreateProjectBriefRequest) -> operations.CreateProjectBriefResponse:
        r"""Create a project brief
        Creates a new project brief.

        Returns the full record of the newly created project brief.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.CreateProjectBriefRequest, base_url, '/projects/{project_gid}/project_briefs', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.CreateProjectBriefRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.CreateProjectBriefResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.CreateProjectBrief201ApplicationJSON])
                res.create_project_brief_201_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def delete_project_brief(self, request: operations.DeleteProjectBriefRequest) -> operations.DeleteProjectBriefResponse:
        r"""Delete a project brief
        Deletes a specific, existing project brief.

        Returns an empty data record.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.DeleteProjectBriefRequest, base_url, '/project_briefs/{project_brief_gid}', request)
        headers = {}
        query_params = utils.get_query_params(operations.DeleteProjectBriefRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('DELETE', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.DeleteProjectBriefResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.DeleteProjectBrief200ApplicationJSON])
                res.delete_project_brief_200_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_project_brief(self, request: operations.GetProjectBriefRequest) -> operations.GetProjectBriefResponse:
        r"""Get a project brief
        Get the full record for a project brief.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetProjectBriefRequest, base_url, '/project_briefs/{project_brief_gid}', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetProjectBriefRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProjectBriefResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetProjectBrief200ApplicationJSON])
                res.get_project_brief_200_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 402, 403, 404, 424, 500, 501, 503, 504]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def update_project_brief(self, request: operations.UpdateProjectBriefRequest) -> operations.UpdateProjectBriefResponse:
        r"""Update a project brief
        An existing project brief can be updated by making a PUT request on the URL for
        that project brief. Only the fields provided in the `data` block will be updated;
        any unspecified fields will remain unchanged.

        Returns the complete updated project brief record.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.UpdateProjectBriefRequest, base_url, '/project_briefs/{project_brief_gid}', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        if data is None and form is None:
            raise Exception('request body is required')
        query_params = utils.get_query_params(operations.UpdateProjectBriefRequest, request)
        headers['Accept'] = 'application/json'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('PUT', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.UpdateProjectBriefResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.UpdateProjectBrief200ApplicationJSON])
                res.update_project_brief_200_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    