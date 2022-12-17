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
  return (datetime.fromtimestamp(DISCORD_EPOCH) + timedelta(milliseconds=milliseconds)).isoformat() + 'Z'

def validate_snowflake(snowflake: str) -> str:
  """Validate snowflake and convert to ISO format date string.
  Args:
      snowflake (str): Snowflake to validate and convert.
  Returns:
      str: ISO format date string in UTC.
  """
  # Check if input is a valid snowflake
  if not snowflake.isdigit():
    return "Error! Snowflakes only contain numbers"
  elif not (0 <= int(snowflake) < 2**64):
    return "Error! Snowflakes are 64-bit integers"
  elif int(snowflake) < DISCORD_EPOCH * 1000:
    return f"Error! Snowflakes are greater than or equal to {DISCORD_EPOCH}"
  else:
    return convert_snowflake(int(snowflake))
