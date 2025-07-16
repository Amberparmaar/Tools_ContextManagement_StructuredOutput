from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool
from agents.run import RunConfig
import os
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel #pydantic ki laibrary se data ka structure bnaty hain

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

class WeatherAnswer(BaseModel):
  location: str
  temperature_c: float
  country: str

@function_tool(
        name_override='weather_tool'
)
async def weather_info(city:str, country: str) ->str:
    """you are helping tool , provide weather detail according to city name."""
    return f'The weather of {city},{country} is sunny.'

agent = Agent(
  name="StructuredWeatherAgent",
  instructions="Use the final_output tool with WeatherAnswer schema.",
  output_type=WeatherAnswer
)

result=Runner.run_sync(agent,'What is the temperature in Karachi?', run_config=config)
print(type(result.final_output))
print(result.final_output)