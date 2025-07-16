🤖 Agentic AI Tools with OpenAI Agents SDK (Gemini Model)
This project showcases how to use the OpenAI Agents SDK (Agentic AI pattern) with Google's Gemini API to build intelligent agents capable of:

Greeting the user

Giving inspirational quotes

Providing weather information

Understanding structured user data (like age and ID)

Generating structured weather responses using Pydantic

📁 Project Structure
.
├── simple_tools_agent.py          # Basic tools: greeting, quotes, weather
├── user_context_agent.py          # User info tools using context (RunContextWrapper)
├── structured_weather_agent.py    # Structured weather response using Pydantic
├── .env                           # Contains GEMINI_API_KEY
└── README.md                      # You are here
🛠 Requirements
Python 3.8+

openai-agents SDK

pydantic

python-dotenv

Install dependencies:

uv add openai-agents pydantic python-dotenv
🔑 .env Setup
Add your Gemini API Key in a .env file:

GEMINI_API_KEY=your_gemini_api_key_here
📜 Files Overview
1. simple_tools_agent.py
This script defines an agent with three basic tools:

greet_user: Sends a friendly greeting.

quote: Returns an inspirational quote.

weather_info(city: str): Gives the weather for a given city.

🔧 Agent Instruction:

"You are a helpful assistant. You can tell weather of cities, quote, and greet user."

📌 Example prompt:

Runner.run_sync(agent, 'first greet me then tell me weather of karachi and then tell quote.', run_config=config)
2. user_context_agent.py
This script demonstrates context-aware agents using RunContextWrapper with a UserInfo schema.

get_user_info: Returns the user's name and age.

get_id: Returns the user's ID.

is_user_adult: Checks if the user is an adult (age > 18).

🎯 Uses a UserInfo Pydantic class for structured context input.

📌 Example prompt:

Runner.run_sync(agent, 'is Sana an adult? answer me using is_user_adult tool.', run_config=config, context=user_obj2)
3. structured_weather_agent.py
This script demonstrates structured outputs using Pydantic.

weather_info(city: str, country: str): Returns weather information.

Output is validated against the WeatherAnswer schema.

🏗 WeatherAnswer schema contains:

class WeatherAnswer(BaseModel):
  location: str
  temperature_c: float
  country: str
📌 Example prompt:

Runner.run_sync(agent, 'What is the temperature in Karachi?', run_config=config)
⚠️ Currently returns static data for demo.

💡 Notes
All agents use Gemini via OpenAI-compatible endpoints.

RunConfig and AsyncOpenAI setup is consistent across all scripts.

Use function_tool() decorators to register tool functions.

Use output_type for enforcing structured outputs.

✅ Output Examples
Simple Tools Agent

Hello! I hope you're having a wonderful day! 😊
The weather of Karachi is sunny.
"The only way to do great work is to love what you do." – Steve Jobs
User Context Agent

"The user Sana is an adult."
Structured Weather Agent
json
Copy
Edit
{
  "location": "Karachi",
  "temperature_c": 25.0,
  "country": "Pakistan"
}
🔚 Conclusion
This project gives a strong foundation for building AI-powered agents that are:

Tool-augmented

Context-aware

Structured-output friendly

Great for learning how to build intelligent systems using OpenAI Agents SDK + Gemini!
