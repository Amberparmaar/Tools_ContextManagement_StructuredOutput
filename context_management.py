from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, function_tool, RunContextWrapper
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
class UserInfo(BaseModel):
   name: str
   age: int
   uid: int
  
@function_tool()
async def get_user_info(ctx:RunContextWrapper[UserInfo]):
   return f'The User {ctx.context.name} is {ctx.context.age} years old.'

@function_tool()
async def get_id(ctx:RunContextWrapper[UserInfo]):
   return f'The User id is {ctx.context.uid}.'

@function_tool()
async def is_user_adult(ctx:RunContextWrapper[UserInfo]):
    if ctx.context.age > 18:
        return f"The user {ctx.context.name} is an adult."
    else:
        return f"The user {ctx.context.name} is not an adult."

user_obj1 =UserInfo(name='Ali', age= 15, uid= 4567)
user_obj2 = UserInfo(name='Hammad', age= 19, uid= 1234)
user_obj2.name = 'Sana'

agent = Agent(
  name="Helping Agent",
  instructions="You are a helpful agent. Always return complete user info.",
  tools=[get_user_info, get_id, is_user_adult],
  #output_type=UserInfo  
)

result=Runner.run_sync(agent,'is Sana an adult? answer me using is_user_adult tool.', run_config=config, context=user_obj2)
print(type(result.final_output))
print(result.final_output)