from azure.devops.connection import Connection
from azure.devops.v6_0.core.core_client import CoreClient
from azure.devops.v6_0.core.models import WebApiTeam
from msrest.authentication import BasicAuthentication
from dotenv import load_dotenv
import os

load_dotenv()

personal_access_token = os.getenv('PERSONAL_ACCESS_TOKEN')
organization_url = os.getenv("ORGANIZATION_URL")
project_id = os.getenv("PROJECT_ID")

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)

# Get a client (the "core" client provides access to projects, teams, etc)
connection.clients_v6_0.get_core_client()
core_client: CoreClient = connection.clients.get_core_client()

team = WebApiTeam(description="Test team",
                  name="Test Team")
core_client.create_team(team, project_id)
