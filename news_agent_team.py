from phi.agent import Agent
from agents.business_news_agent import business_news_agent
from agents.climate_news_agent import climate_news_agent
from agents.sports_news_agent import sports_news_agent
from agents.health_news_agent import health_news_agent
from agents.crime_news_agent import crime_news_agent
from agents.military_news_agent import military_news_agent
from agents.science_and_technology_news_agent import science_and_technology_news_agent
from agents.political_news_agent import political_news_agent
from agents.financial_news_agent import financial_news_agent
from phi.playground import Playground, serve_playground_app
from phi.model.openai import OpenAIChat


agent_team = Agent(
    name="chief news editor",
    model=OpenAIChat(id="gpt-4o-mini"),
    team=[business_news_agent, crime_news_agent, financial_news_agent, political_news_agent,
          science_and_technology_news_agent, sports_news_agent, military_news_agent, health_news_agent,
          climate_news_agent],
    instructions=["Always use tools to fulfil the user query. Always give the link to sources "],
    show_tool_calls=True,
    reasoning=False,
    markdown=True,
    show_full_reasoning=True,
    add_datetime_to_instructions=True,
    stream=True
)

app = Playground(agents=[agent_team]).get_app()

if __name__ == "__main__":
    serve_playground_app("news_agent_team:app", reload=True)
