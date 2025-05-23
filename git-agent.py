import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.github import GithubTools

agent = Agent(
    model= Gemini(id="gemini-2.0-flash", api_key=os.environ.get("GEMINI_API_KEY")),
    instructions=[
        "Use your tools to answer questions about the repo: https://github.com/gurezende/ETL_DuckDB",
        "Do not create any issues or pull requests unless explicitly asked to do so",
        "You are expected to write clear and concise documentation Readme files for the repo",
        "Briefly explain what each script does.",
    ],
    tools=[GithubTools()],
    show_tool_calls=True,
)

agent.print_response("Read the codes in the 'scripts' folder and write a 'Readme.md' file explaining the project and how to run it", markdown=True)