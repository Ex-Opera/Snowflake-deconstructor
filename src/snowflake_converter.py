from datetime import datetime, timedelta

# Discord epoch timestamp in seconds
DISCORD_EPOCH = 1420070400

def convert_snowflake(snowflake: int) -> str:
  """Convert snowflake to ISO format date string.
  Args:
      snowflake (int): Snowflake to convert.
  Returns:
      str: ISO format date string in UTC.
  """
  # Calculate number of milliseconds since Discord epoch
  milliseconds = int(snowflake >> 22)
  # Add milliseconds to Discord epoch and return ISO format date string in UTC
  return (datetime.utcfromtimestamp(DISCORD_EPOCH) + timedelta(milliseconds=milliseconds)).isoformat() + 'Z'

def validate_snowflake() -> str:
  """Validate snowflake and convert to ISO format date string.
  Returns:
      str: ISO format date string in UTC.
  """
  while True:
    try:
      # Snowflake to validate
      snowflake = int(input("Snowflake: "))
      # Check if snowflake is a valid 64-bit integer
      if not (0 <= snowflake < 2**64):
        print("Error! Snowflakes are 64-bit integers")
      # Check if snowflake is greater than or equal to the Discord epoch
      elif snowflake < DISCORD_EPOCH * 1000:
        print(f"Error! Snowflakes are greater than or equal to {DISCORD_EPOCH}")
      else:
        print(convert_snowflake(snowflake))
        break
    except ValueError:
      print("Error! Snowflakes only contain numbers")

validate_snowflake()
