from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY=os.environ.get('GEMINI_API_KEY')

external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config= RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True

)
@function_tool(name_override='greeting_tool')
async def greet_user():
    """Greet the user in a friendly way."""
    return f"Hello! I hope you're having a wonderful day! 😊"

@function_tool(
        name_override='quote_tool'
)
async def quote():
    """provide a quote to user."""
    return f'The only way to do great work is to love what you do. - Steve Jobs'

@function_tool(
        name_override='weather_tool'
)
async def weather_info(city:str) ->str:
    """you are helping tool , provide weather according to city name."""
    return f'The weather of {city} is sunny.'

agent = Agent(
    name='Helping Assistant',
    instructions="""You are a helpful assistant. You can tell weather of cities, quote, and greet user.
Use:
- greeting_tool for greeting the user 
- quote_tool for telling a quote
- weather_tool for city weather""",
    tools=[greet_user, quote, weather_info],
)
result=Runner.run_sync(agent, 'first greet me then tell me weather of karachi and then tell quote.', run_config=config)
print("=== Final Output ===")
print(result.final_output)
