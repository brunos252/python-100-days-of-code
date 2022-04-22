# API keys, Authentication, environment variables, sending SMS

# API authentication - for non-free API's

# API key - for them to track how much you use your API,
# and whether you're abusing them

# twilio API - sending SMS, having number in any country...
# - paid, trial credit

# set up python script to run every morning -
# pythonanywhere

# environment variables
# - for convenience, so you do not need to change your codebase
# - security, separate keys from codebase (for instance, online)
# in bash> export OWN_API_KEY=...
#
import os
api_key = os.environ.get("OWM_API_KEY")
