import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.github import GithubTools
from agno.tools.file import FileTools

agent = Agent(
    model= Gemini(id="gemini-2.0-flash", api_key=os.environ.get("GEMINI_API_KEY")),
    instructions=
        """Use your tools to answer questions about the repo: https://github.com/gurezende/ETL_DuckDB
           Do not create any issues or pull requests unless explicitly asked to do so
           You are expected to write clear and concise documentation Readme files for the repo
           Briefly explain what each script does.
           Use this template:
            - Overview: what is the purpose of the project
            - Features: what are the main features, what does it do?
            - Requirements: what are the requirements to run the project
            - Code Structure: explain each script in two sentences.
            - How to Run Project: how to install and run the project
            - License: MIT License
            - Demonstration: leave blank. I will add a video later
            - Known Issues: say I had trouble adding the project to docker due to incompatibilities among the packages
            - About Me: add that the project was created by Gustavo R Santos (https://gustavorsantos.me)
           """,
    tools=[GithubTools(access_token=os.environ.get("GITHUB_ACCESS_TOKEN")),
           FileTools() ],
    expected_output="""A 'myreadme.md' file""",
    show_tool_calls=True
)

agent.print_response("Read the repo and generate a prompt to create a picture that summarizes the repo", markdown=True)