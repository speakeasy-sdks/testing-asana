# testing-2

<!-- Start SDK Installation -->
## SDK Installation

```bash
pip install git+https://github.com/speakeasy-sdks/testing-asana.git
```
<!-- End SDK Installation -->

## SDK Example Usage
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

<!-- Start SDK Available Operations -->
## Available Resources and Operations


### [attachments](docs/sdks/attachments/README.md)

* [create_attachment_for_object](docs/sdks/attachments/README.md#create_attachment_for_object) - Upload an attachment
* [delete_attachment](docs/sdks/attachments/README.md#delete_attachment) - Delete an attachment
* [get_attachment](docs/sdks/attachments/README.md#get_attachment) - Get an attachment
* [get_attachments_for_object](docs/sdks/attachments/README.md#get_attachments_for_object) - Get attachments from an object

### [audit_log_api](docs/sdks/auditlogapi/README.md)

* [get_audit_log_events](docs/sdks/auditlogapi/README.md#get_audit_log_events) - Get audit log events

### [batch_api](docs/sdks/batchapi/README.md)

* [create_batch_request](docs/sdks/batchapi/README.md#create_batch_request) - Submit parallel requests

### [custom_field_settings](docs/sdks/customfieldsettings/README.md)

* [get_custom_field_settings_for_portfolio](docs/sdks/customfieldsettings/README.md#get_custom_field_settings_for_portfolio) - Get a portfolio's custom fields
* [get_custom_field_settings_for_project](docs/sdks/customfieldsettings/README.md#get_custom_field_settings_for_project) - Get a project's custom fields

### [custom_fields](docs/sdks/customfields/README.md)

* [create_custom_field](docs/sdks/customfields/README.md#create_custom_field) - Create a custom field
* [create_enum_option_for_custom_field](docs/sdks/customfields/README.md#create_enum_option_for_custom_field) - Create an enum option
* [delete_custom_field](docs/sdks/customfields/README.md#delete_custom_field) - Delete a custom field
* [get_custom_field](docs/sdks/customfields/README.md#get_custom_field) - Get a custom field
* [get_custom_fields_for_workspace](docs/sdks/customfields/README.md#get_custom_fields_for_workspace) - Get a workspace's custom fields
* [insert_enum_option_for_custom_field](docs/sdks/customfields/README.md#insert_enum_option_for_custom_field) - Reorder a custom field's enum
* [update_custom_field](docs/sdks/customfields/README.md#update_custom_field) - Update a custom field
* [update_enum_option](docs/sdks/customfields/README.md#update_enum_option) - Update an enum option

### [events](docs/sdks/events/README.md)

* [get_events](docs/sdks/events/README.md#get_events) - Get events on a resource

### [goal_relationships](docs/sdks/goalrelationships/README.md)

* [add_supporting_relationship](docs/sdks/goalrelationships/README.md#add_supporting_relationship) - Add a supporting goal relationship
* [get_goal_relationship](docs/sdks/goalrelationships/README.md#get_goal_relationship) - Get a goal relationship
* [get_goal_relationships](docs/sdks/goalrelationships/README.md#get_goal_relationships) - Get goal relationships
* [remove_supporting_relationship](docs/sdks/goalrelationships/README.md#remove_supporting_relationship) - Removes a supporting goal relationship
* [update_goal_relationship](docs/sdks/goalrelationships/README.md#update_goal_relationship) - Update a goal relationship

### [goals](docs/sdks/goals/README.md)

* [add_followers](docs/sdks/goals/README.md#add_followers) - Add a collaborator to a goal
* [create_goal](docs/sdks/goals/README.md#create_goal) - Create a goal
* [create_goal_metric](docs/sdks/goals/README.md#create_goal_metric) - Create a goal metric
* [delete_goal](docs/sdks/goals/README.md#delete_goal) - Delete a goal
* [get_goal](docs/sdks/goals/README.md#get_goal) - Get a goal
* [get_goals](docs/sdks/goals/README.md#get_goals) - Get goals
* [get_parent_goals_for_goal](docs/sdks/goals/README.md#get_parent_goals_for_goal) - Get parent goals from a goal
* [remove_followers](docs/sdks/goals/README.md#remove_followers) - Remove a collaborator from a goal
* [update_goal](docs/sdks/goals/README.md#update_goal) - Update a goal
* [update_goal_metric](docs/sdks/goals/README.md#update_goal_metric) - Update a goal metric

### [jobs](docs/sdks/jobs/README.md)

* [get_job](docs/sdks/jobs/README.md#get_job) - Get a job by id

### [organization_exports](docs/sdks/organizationexports/README.md)

* [create_organization_export](docs/sdks/organizationexports/README.md#create_organization_export) - Create an organization export request
* [get_organization_export](docs/sdks/organizationexports/README.md#get_organization_export) - Get details on an org export request

### [portfolio_memberships](docs/sdks/portfoliomemberships/README.md)

* [get_portfolio_membership](docs/sdks/portfoliomemberships/README.md#get_portfolio_membership) - Get a portfolio membership
* [get_portfolio_memberships](docs/sdks/portfoliomemberships/README.md#get_portfolio_memberships) - Get multiple portfolio memberships
* [get_portfolio_memberships_for_portfolio](docs/sdks/portfoliomemberships/README.md#get_portfolio_memberships_for_portfolio) - Get memberships from a portfolio

### [portfolios](docs/sdks/portfolios/README.md)

* [add_custom_field_setting_for_portfolio](docs/sdks/portfolios/README.md#add_custom_field_setting_for_portfolio) - Add a custom field to a portfolio
* [add_item_for_portfolio](docs/sdks/portfolios/README.md#add_item_for_portfolio) - Add a portfolio item
* [add_members_for_portfolio](docs/sdks/portfolios/README.md#add_members_for_portfolio) - Add users to a portfolio
* [create_portfolio](docs/sdks/portfolios/README.md#create_portfolio) - Create a portfolio
* [delete_portfolio](docs/sdks/portfolios/README.md#delete_portfolio) - Delete a portfolio
* [get_items_for_portfolio](docs/sdks/portfolios/README.md#get_items_for_portfolio) - Get portfolio items
* [get_portfolio](docs/sdks/portfolios/README.md#get_portfolio) - Get a portfolio
* [get_portfolios](docs/sdks/portfolios/README.md#get_portfolios) - Get multiple portfolios
* [remove_custom_field_setting_for_portfolio](docs/sdks/portfolios/README.md#remove_custom_field_setting_for_portfolio) - Remove a custom field from a portfolio
* [remove_item_for_portfolio](docs/sdks/portfolios/README.md#remove_item_for_portfolio) - Remove a portfolio item
* [remove_members_for_portfolio](docs/sdks/portfolios/README.md#remove_members_for_portfolio) - Remove users from a portfolio
* [update_portfolio](docs/sdks/portfolios/README.md#update_portfolio) - Update a portfolio

### [project_briefs](docs/sdks/projectbriefs/README.md)

* [create_project_brief](docs/sdks/projectbriefs/README.md#create_project_brief) - Create a project brief
* [delete_project_brief](docs/sdks/projectbriefs/README.md#delete_project_brief) - Delete a project brief
* [get_project_brief](docs/sdks/projectbriefs/README.md#get_project_brief) - Get a project brief
* [update_project_brief](docs/sdks/projectbriefs/README.md#update_project_brief) - Update a project brief

### [project_memberships](docs/sdks/projectmemberships/README.md)

* [get_project_membership](docs/sdks/projectmemberships/README.md#get_project_membership) - Get a project membership
* [get_project_memberships_for_project](docs/sdks/projectmemberships/README.md#get_project_memberships_for_project) - Get memberships from a project

### [project_statuses](docs/sdks/projectstatuses/README.md)

* [create_project_status_for_project](docs/sdks/projectstatuses/README.md#create_project_status_for_project) - Create a project status
* [delete_project_status](docs/sdks/projectstatuses/README.md#delete_project_status) - Delete a project status
* [get_project_status](docs/sdks/projectstatuses/README.md#get_project_status) - Get a project status
* [get_project_statuses_for_project](docs/sdks/projectstatuses/README.md#get_project_statuses_for_project) - Get statuses from a project

### [project_templates](docs/sdks/projecttemplates/README.md)

* [get_project_template](docs/sdks/projecttemplates/README.md#get_project_template) - Get a project template
* [get_project_templates](docs/sdks/projecttemplates/README.md#get_project_templates) - Get multiple project templates
* [get_project_templates_for_team](docs/sdks/projecttemplates/README.md#get_project_templates_for_team) - Get a team's project templates
* [instantiate_project](docs/sdks/projecttemplates/README.md#instantiate_project) - Instantiate a project from a project template

### [projects](docs/sdks/projects/README.md)

* [add_custom_field_setting_for_project](docs/sdks/projects/README.md#add_custom_field_setting_for_project) - Add a custom field to a project
* [add_followers_for_project](docs/sdks/projects/README.md#add_followers_for_project) - Add followers to a project
* [add_members_for_project](docs/sdks/projects/README.md#add_members_for_project) - Add users to a project
* [create_project](docs/sdks/projects/README.md#create_project) - Create a project
* [create_project_for_team](docs/sdks/projects/README.md#create_project_for_team) - Create a project in a team
* [create_project_for_workspace](docs/sdks/projects/README.md#create_project_for_workspace) - Create a project in a workspace
* [delete_project](docs/sdks/projects/README.md#delete_project) - Delete a project
* [duplicate_project](docs/sdks/projects/README.md#duplicate_project) - Duplicate a project
* [get_project](docs/sdks/projects/README.md#get_project) - Get a project
* [get_projects](docs/sdks/projects/README.md#get_projects) - Get multiple projects
* [get_projects_for_task](docs/sdks/projects/README.md#get_projects_for_task) - Get projects a task is in
* [get_projects_for_team](docs/sdks/projects/README.md#get_projects_for_team) - Get a team's projects
* [get_projects_for_workspace](docs/sdks/projects/README.md#get_projects_for_workspace) - Get all projects in a workspace
* [get_task_counts_for_project](docs/sdks/projects/README.md#get_task_counts_for_project) - Get task count of a project
* [project_save_as_template](docs/sdks/projects/README.md#project_save_as_template) - Create a project template from a project
* [remove_custom_field_setting_for_project](docs/sdks/projects/README.md#remove_custom_field_setting_for_project) - Remove a custom field from a project
* [remove_followers_for_project](docs/sdks/projects/README.md#remove_followers_for_project) - Remove followers from a project
* [remove_members_for_project](docs/sdks/projects/README.md#remove_members_for_project) - Remove users from a project
* [update_project](docs/sdks/projects/README.md#update_project) - Update a project

### [sections](docs/sdks/sections/README.md)

* [add_task_for_section](docs/sdks/sections/README.md#add_task_for_section) - Add task to section
* [create_section_for_project](docs/sdks/sections/README.md#create_section_for_project) - Create a section in a project
* [delete_section](docs/sdks/sections/README.md#delete_section) - Delete a section
* [get_section](docs/sdks/sections/README.md#get_section) - Get a section
* [get_sections_for_project](docs/sdks/sections/README.md#get_sections_for_project) - Get sections in a project
* [insert_section_for_project](docs/sdks/sections/README.md#insert_section_for_project) - Move or Insert sections
* [update_section](docs/sdks/sections/README.md#update_section) - Update a section

### [status_updates](docs/sdks/statusupdates/README.md)

* [create_status_for_object](docs/sdks/statusupdates/README.md#create_status_for_object) - Create a status update
* [delete_status](docs/sdks/statusupdates/README.md#delete_status) - Delete a status update
* [get_status](docs/sdks/statusupdates/README.md#get_status) - Get a status update
* [get_statuses_for_object](docs/sdks/statusupdates/README.md#get_statuses_for_object) - Get status updates from an object

### [stories](docs/sdks/stories/README.md)

* [create_story_for_task](docs/sdks/stories/README.md#create_story_for_task) - Create a story on a task
* [delete_story](docs/sdks/stories/README.md#delete_story) - Delete a story
* [get_stories_for_task](docs/sdks/stories/README.md#get_stories_for_task) - Get stories from a task
* [get_story](docs/sdks/stories/README.md#get_story) - Get a story
* [update_story](docs/sdks/stories/README.md#update_story) - Update a story

### [tags](docs/sdks/tags/README.md)

* [create_tag](docs/sdks/tags/README.md#create_tag) - Create a tag
* [create_tag_for_workspace](docs/sdks/tags/README.md#create_tag_for_workspace) - Create a tag in a workspace
* [delete_tag](docs/sdks/tags/README.md#delete_tag) - Delete a tag
* [get_tag](docs/sdks/tags/README.md#get_tag) - Get a tag
* [get_tags](docs/sdks/tags/README.md#get_tags) - Get multiple tags
* [get_tags_for_task](docs/sdks/tags/README.md#get_tags_for_task) - Get a task's tags
* [get_tags_for_workspace](docs/sdks/tags/README.md#get_tags_for_workspace) - Get tags in a workspace
* [update_tag](docs/sdks/tags/README.md#update_tag) - Update a tag

### [tasks](docs/sdks/tasks/README.md)

* [add_dependencies_for_task](docs/sdks/tasks/README.md#add_dependencies_for_task) - Set dependencies for a task
* [add_dependents_for_task](docs/sdks/tasks/README.md#add_dependents_for_task) - Set dependents for a task
* [add_followers_for_task](docs/sdks/tasks/README.md#add_followers_for_task) - Add followers to a task
* [add_project_for_task](docs/sdks/tasks/README.md#add_project_for_task) - Add a project to a task
* [add_tag_for_task](docs/sdks/tasks/README.md#add_tag_for_task) - Add a tag to a task
* [create_subtask_for_task](docs/sdks/tasks/README.md#create_subtask_for_task) - Create a subtask
* [create_task](docs/sdks/tasks/README.md#create_task) - Create a task
* [delete_task](docs/sdks/tasks/README.md#delete_task) - Delete a task
* [duplicate_task](docs/sdks/tasks/README.md#duplicate_task) - Duplicate a task
* [get_dependencies_for_task](docs/sdks/tasks/README.md#get_dependencies_for_task) - Get dependencies from a task
* [get_dependents_for_task](docs/sdks/tasks/README.md#get_dependents_for_task) - Get dependents from a task
* [get_subtasks_for_task](docs/sdks/tasks/README.md#get_subtasks_for_task) - Get subtasks from a task
* [get_task](docs/sdks/tasks/README.md#get_task) - Get a task
* [get_tasks](docs/sdks/tasks/README.md#get_tasks) - Get multiple tasks
* [get_tasks_for_project](docs/sdks/tasks/README.md#get_tasks_for_project) - Get tasks from a project
* [get_tasks_for_section](docs/sdks/tasks/README.md#get_tasks_for_section) - Get tasks from a section
* [get_tasks_for_tag](docs/sdks/tasks/README.md#get_tasks_for_tag) - Get tasks from a tag
* [get_tasks_for_user_task_list](docs/sdks/tasks/README.md#get_tasks_for_user_task_list) - Get tasks from a user task list
* [remove_dependencies_for_task](docs/sdks/tasks/README.md#remove_dependencies_for_task) - Unlink dependencies from a task
* [remove_dependents_for_task](docs/sdks/tasks/README.md#remove_dependents_for_task) - Unlink dependents from a task
* [remove_follower_for_task](docs/sdks/tasks/README.md#remove_follower_for_task) - Remove followers from a task
* [remove_project_for_task](docs/sdks/tasks/README.md#remove_project_for_task) - Remove a project from a task
* [remove_tag_for_task](docs/sdks/tasks/README.md#remove_tag_for_task) - Remove a tag from a task
* [search_tasks_for_workspace](docs/sdks/tasks/README.md#search_tasks_for_workspace) - Search tasks in a workspace
* [set_parent_for_task](docs/sdks/tasks/README.md#set_parent_for_task) - Set the parent of a task
* [update_task](docs/sdks/tasks/README.md#update_task) - Update a task

### [team_memberships](docs/sdks/teammemberships/README.md)

* [get_team_membership](docs/sdks/teammemberships/README.md#get_team_membership) - Get a team membership
* [get_team_memberships](docs/sdks/teammemberships/README.md#get_team_memberships) - Get team memberships
* [get_team_memberships_for_team](docs/sdks/teammemberships/README.md#get_team_memberships_for_team) - Get memberships from a team
* [get_team_memberships_for_user](docs/sdks/teammemberships/README.md#get_team_memberships_for_user) - Get memberships from a user

### [teams](docs/sdks/teams/README.md)

* [add_user_for_team](docs/sdks/teams/README.md#add_user_for_team) - Add a user to a team
* [create_team](docs/sdks/teams/README.md#create_team) - Create a team
* [get_team](docs/sdks/teams/README.md#get_team) - Get a team
* [get_teams_for_user](docs/sdks/teams/README.md#get_teams_for_user) - Get teams for a user
* [get_teams_for_workspace](docs/sdks/teams/README.md#get_teams_for_workspace) - Get teams in a workspace
* [remove_user_for_team](docs/sdks/teams/README.md#remove_user_for_team) - Remove a user from a team
* [update_team](docs/sdks/teams/README.md#update_team) - Update a team

### [time_periods](docs/sdks/timeperiods/README.md)

* [get_time_period](docs/sdks/timeperiods/README.md#get_time_period) - Get a time period
* [get_time_periods](docs/sdks/timeperiods/README.md#get_time_periods) - Get time periods

### [typeahead](docs/sdks/typeahead/README.md)

* [typeahead_for_workspace](docs/sdks/typeahead/README.md#typeahead_for_workspace) - Get objects via typeahead

### [user_task_lists](docs/sdks/usertasklists/README.md)

* [get_user_task_list](docs/sdks/usertasklists/README.md#get_user_task_list) - Get a user task list
* [get_user_task_list_for_user](docs/sdks/usertasklists/README.md#get_user_task_list_for_user) - Get a user's task list

### [users](docs/sdks/users/README.md)

* [get_favorites_for_user](docs/sdks/users/README.md#get_favorites_for_user) - Get a user's favorites
* [get_user](docs/sdks/users/README.md#get_user) - Get a user
* [get_users](docs/sdks/users/README.md#get_users) - Get multiple users
* [get_users_for_team](docs/sdks/users/README.md#get_users_for_team) - Get users in a team
* [get_users_for_workspace](docs/sdks/users/README.md#get_users_for_workspace) - Get users in a workspace or organization

### [webhooks](docs/sdks/webhooks/README.md)

* [create_webhook](docs/sdks/webhooks/README.md#create_webhook) - Establish a webhook
* [delete_webhook](docs/sdks/webhooks/README.md#delete_webhook) - Delete a webhook
* [get_webhook](docs/sdks/webhooks/README.md#get_webhook) - Get a webhook
* [get_webhooks](docs/sdks/webhooks/README.md#get_webhooks) - Get multiple webhooks
* [update_webhook](docs/sdks/webhooks/README.md#update_webhook) - Update a webhook

### [workspace_memberships](docs/sdks/workspacememberships/README.md)

* [get_workspace_membership](docs/sdks/workspacememberships/README.md#get_workspace_membership) - Get a workspace membership
* [get_workspace_memberships_for_user](docs/sdks/workspacememberships/README.md#get_workspace_memberships_for_user) - Get workspace memberships for a user
* [get_workspace_memberships_for_workspace](docs/sdks/workspacememberships/README.md#get_workspace_memberships_for_workspace) - Get the workspace memberships for a workspace

### [workspaces](docs/sdks/workspaces/README.md)

* [add_user_for_workspace](docs/sdks/workspaces/README.md#add_user_for_workspace) - Add a user to a workspace or organization
* [get_workspace](docs/sdks/workspaces/README.md#get_workspace) - Get a workspace
* [get_workspaces](docs/sdks/workspaces/README.md#get_workspaces) - Get multiple workspaces
* [remove_user_for_workspace](docs/sdks/workspaces/README.md#remove_user_for_workspace) - Remove a user from a workspace or organization
* [update_workspace](docs/sdks/workspaces/README.md#update_workspace) - Update a workspace
<!-- End SDK Available Operations -->

### Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

### Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
