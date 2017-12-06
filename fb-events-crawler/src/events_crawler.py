import facebook_bot
import json

results = facebook_bot.get_events_by_location(45.464211, 9.191383, '*', 5000, 500, "2017-12-01")

for result in results:
    print(json.dumps(result))
