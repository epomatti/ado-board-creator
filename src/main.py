from typing import Collection
from azure.devops.connection import Connection
from azure.devops.v6_0.core.core_client import CoreClient
from azure.devops.v6_0.member_entitlement_management.member_entitlement_management_client import MemberEntitlementManagementClient
from azure.devops.v6_0.core.models import WebApiTeam
from msrest.authentication import BasicAuthentication
from dotenv import load_dotenv
import os

load_dotenv()

personal_access_token = os.getenv('PERSONAL_ACCESS_TOKEN')
organization_url = os.getenv('ORGANIZATION_URL')
project_id = os.getenv('PROJECT_ID')
member_id = os.getenv('MEMBER_ID')

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
core_client: CoreClient = connection.clients.get_core_client()

teams: list = core_client.get_teams(project_id=project_id)
team_name = 'Test team'
team_exists = False
team_id = None

for i in teams:
    if(i.name == team_name):
        team_exists = True
        team_id = i.id
        print("Found existing team")
        break

if(not team_exists):
    request_team = WebApiTeam(name=team_name)
    team: WebApiTeam = core_client.create_team(request_team, project_id)
    team_id = team.id
    print("Created new team")

#member_entitlement_management_client: MemberEntitlementManagementClient = connection.clients_v6_0.get_member_entitlement_management_client()
