# dim toggle levels until low and then up again
entities = data.get('dim_lights').replace(' ', '').split(',')
dim_level_entity = data.get('dim_level_entity')
colorloop = data.get('colorloop') or False

step = 75

states = hass.states.get(dim_level_entity)
current_level = states.attributes.get('brightness') or 0

new_level = int(current_level) - step

if new_level < 10:
    new_level = 255

logger.info("dim_level_entity:" + dim_level_entity + " new_level:" + str(new_level) + "entities value:" + str(entities))

for entity in entities:
    data = { 'entity_id' : entity, 'brightness' : 255 }

    effects = hass.states.get(entity).attributes.get('effect_list') or ''
    if colorloop and 'colorloop' in effects:
        data['effect'] = 'colorloop'

    data['brightness'] = new_level
    hass.services.call('light', 'turn_on', data)
