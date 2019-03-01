# hass-resources
Various home-assistant resources

## Dim toggle
A small python script which cycles between different levels for the lights sent in as entitits

### Installation
Install it by downloading it and copy it to `config/pyhton_scripts`

### Automatiomn
An example automation for it:
```
- alias: Wall-C 2
  trigger:
    platform: event
    event_type: zwave.scene_activated
    event_data:
      entity_id: zwave.z_wave_me_zme_wallc_s_secure_wall_controller_3
      scene_id: 2
      scene_data: 0
  action:
    - service: homeassistant.turn_on
      entity_id: switch.kitchen_taklampa
    - service: python_script.dim_toggle
      data:
        dim_level_entity: light.kitchen_spotlights
        dim_lights: "light.kitchen_spotlights"
        colorloop: "true"

- alias: Wall-C 2 longpress
  trigger:
    platform: event
    event_type: zwave.scene_activated
    event_data:
      entity_id: zwave.z_wave_me_zme_wallc_s_secure_wall_controller_3
      scene_id: 2
      scene_data: 2
  action:
    - service: homeassistant.turn_off
      entity_id:
        - light.kitchen_spotlights
        - switch.kitchen_taklampa
```
