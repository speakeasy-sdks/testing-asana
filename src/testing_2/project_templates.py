"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from .sdkconfiguration import SDKConfiguration
from testing_2 import utils
from testing_2.models import operations, shared
from typing import Optional

class ProjectTemplates:
    r"""A project template is an object that allows new projects to be created
    with a predefined setup, which may include tasks, sections, rules, etc.
    It simplifies the process of running a workflow that involves a similar
    set of work every time.


    Project templates in organizations are shared with a single team. Currently, the
    team of a project template cannot be changed via the API.
    """
    sdk_configuration: SDKConfiguration

    def __init__(self, sdk_config: SDKConfiguration) -> None:
        self.sdk_configuration = sdk_config
        
    
    def get_project_template(self, request: operations.GetProjectTemplateRequest) -> operations.GetProjectTemplateResponse:
        r"""Get a project template
        Returns the complete project template record for a single project template.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetProjectTemplateRequest, base_url, '/project_templates/{project_template_gid}', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetProjectTemplateRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProjectTemplateResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetProjectTemplate200ApplicationJSON])
                res.get_project_template_200_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_project_templates(self, request: operations.GetProjectTemplatesRequest) -> operations.GetProjectTemplatesResponse:
        r"""Get multiple project templates
        Returns the compact project template records for all project templates in the given team or workspace.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = base_url + '/project_templates'
        headers = {}
        query_params = utils.get_query_params(operations.GetProjectTemplatesRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProjectTemplatesResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetProjectTemplates200ApplicationJSON])
                res.get_project_templates_200_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def get_project_templates_for_team(self, request: operations.GetProjectTemplatesForTeamRequest) -> operations.GetProjectTemplatesForTeamResponse:
        r"""Get a team's project templates
        Returns the compact project template records for all project templates in the team.
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.GetProjectTemplatesForTeamRequest, base_url, '/teams/{team_gid}/project_templates', request)
        headers = {}
        query_params = utils.get_query_params(operations.GetProjectTemplatesForTeamRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('GET', url, params=query_params, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.GetProjectTemplatesForTeamResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 200:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.GetProjectTemplatesForTeam200ApplicationJSON])
                res.get_project_templates_for_team_200_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    
    def instantiate_project(self, request: operations.InstantiateProjectRequest) -> operations.InstantiateProjectResponse:
        r"""Instantiate a project from a project template
        Creates and returns a job that will asynchronously handle the project instantiation.

        To form this request, it is recommended to first make a request to [get a project template](/docs/get-a-project-template). Then, from the response, copy the `gid` from the object in the `requested_dates` array. This `gid` should be used in `requested_dates` to instantiate a project.

        _Note: The body of this request will differ if your workspace is an organization. To determine if your workspace is an organization, use the [is_organization](/docs/workspace) parameter._
        """
        base_url = utils.template_url(*self.sdk_configuration.get_server_details())
        
        url = utils.generate_url(operations.InstantiateProjectRequest, base_url, '/project_templates/{project_template_gid}/instantiateProject', request)
        headers = {}
        req_content_type, data, form = utils.serialize_request_body(request, "request_body", 'json')
        if req_content_type not in ('multipart/form-data', 'multipart/mixed'):
            headers['content-type'] = req_content_type
        query_params = utils.get_query_params(operations.InstantiateProjectRequest, request)
        headers['Accept'] = 'application/json;q=1, application/json;q=0'
        headers['user-agent'] = f'speakeasy-sdk/{self.sdk_configuration.language} {self.sdk_configuration.sdk_version} {self.sdk_configuration.gen_version} {self.sdk_configuration.openapi_doc_version}'
        
        client = self.sdk_configuration.security_client
        
        http_res = client.request('POST', url, params=query_params, data=data, files=form, headers=headers)
        content_type = http_res.headers.get('Content-Type')

        res = operations.InstantiateProjectResponse(status_code=http_res.status_code, content_type=content_type, raw_response=http_res)
        
        if http_res.status_code == 201:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[operations.InstantiateProject201ApplicationJSON])
                res.instantiate_project_201_application_json_object = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)
        elif http_res.status_code in [400, 401, 403, 404, 500]:
            if utils.match_content_type(content_type, 'application/json'):
                out = utils.unmarshal_json(http_res.text, Optional[shared.ErrorResponse])
                res.error_response = out
            else:
                raise errors.SDKError(f'unknown content-type received: {content_type}', http_res.status_code, http_res.text, http_res)

        return res

    