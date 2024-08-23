import os
import sys  # type: ignore
import json  # type: ignore

from propulsionai import PropulsionAI

client = PropulsionAI(
    # This is the default and can be omitted
    bearer_token=os.environ.get("PROPULSIONAI_BEARER_TOKEN"),
)

# Here we define the tool function, its parameters and examples (optional)
def get_current_weather(location: str, format: str) -> str:
    """
    Retrieves the current weather for a specified location.

    This function fetches the current weather data for the given location
    and returns it in the specified format.

    Parameters:
    -----------
    location : str
        The name of the location (city, country, etc.) to get weather for.
    format : str
        The desired output format. Accepted values are 'celsius', 'fahrenheit',
        or 'kelvin' for temperature units.

    Examples:
    ---------
    >>> get_current_weather("New York", "celsius")
    'Current weather in New York: 22°C, Partly Cloudy'

    >>> get_current_weather("London", "fahrenheit")
    'Current weather in London: 59°F, Rainy'
    """
    # print(f"Function Log: Getting weather for {location} in {format} format...")
    return f'{{"temperature": 22, "description": "Partly Cloudy", "location": "{location}", "units": "{format}"}}'


def sync_main() -> None:
    response = client.chat.completions.run_tools(
        deployment="pgl-b-mistral-03",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant.",
            },
            {
                "role": "user",
                "content": "What is the weather in SF and NY?",
            },
        ],
        tools=[get_current_weather],
        stream=True,
        tool_debug=False,
        max_tokens=1000,
    )
    # print(response.to_json())
    # first = next(response)
    # print(f"got response data: {first.to_json()}")

    for data in response:
      if data:
          chunk = data.to_json()
          chunk_json = json.loads(chunk)
          
          if chunk_json["choices"] and chunk_json["choices"][0]["delta"] is not None:
              delta = chunk_json["choices"][0]["delta"]
              
              # Print the entire delta for debugging
              # print("Delta:", delta)
              
              # Check if 'content' exists in delta and is not None
              if "content" in delta and delta["content"] is not None:
                  sys.stdout.write(delta["content"])
                  sys.stdout.flush()  # Ensure content is displayed immediately
              
              # Check for tool calls
              # if "tool_calls" in delta:
                  # print("Tool call detected:", delta["tool_calls"])
              
              # Check for finish reason
              # if "finish_reason" in chunk_json["choices"][0] and chunk_json["choices"][0]["finish_reason"] == "stop":
              #     print("\nGeneration complete.")



sync_main()
