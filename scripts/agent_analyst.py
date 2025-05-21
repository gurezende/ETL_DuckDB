import os
import duckdb
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.duckdb import DuckDbTools

agent = Agent(
    model= Gemini(id="gemini-1.5-flash", api_key=os.environ.get("GEMINI_API_KEY")),
    tools=[DuckDbTools( connection=duckdb.connect("data.db") )], 
    show_tool_calls=True,
    description="""You are an experienced Analyst that helps people to understand the data they are working with.
                    You are given a question and you answer it in a clear and concise way.""",
    instructions="""
                    The DataByStore table has the following columns: store, product, total_qty, total_revenue, and dt.
                    The DataByProduct table has the following columns: product, total_qty, avg_price, avg_qty, total_revenue, and dt.
                    Use tables, coparisons, and calculations to answer the question.
                    If you don't know the answer, you can say 'I don't know'.""",
    expected_output="""A report like response and marketing recommendation for the store and product.""",
    memory=True
)

# Prompt
prompt = "Analyze the total quantity sold by product by store from DataByStore table. Return a report like response with totals and marketing recommendation for each store and product."

# Run the agent
agent.print_response(prompt, markdown=True, stream=False)