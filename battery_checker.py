# check level for all batteries
threshold = data.get('threshold') or 40
threshold = int(threshold)

logger.info("battery_checker: threshold: " + str(threshold))

low_battery_entitites = {}

for state in hass.states.all():
    
    level = state.attributes.get('battery_level') or None
    #logger.info("Got state: %s = %s", state.entity_id, level)
    if level is not None and int(level) <= threshold:
        logger.info("battery checker: %s %s", state.entity_id, level)
        low_battery_entitites[state.entity_id] = level
logger.info("battery_checker: setting state: %s", low_battery_entitites)
hass.states.set("sensor.battery_checker", len(low_battery_entitites), low_battery_entitites)
