# hass-resources
Various home-assistant resources

## Pushbullet SMS script
See https://github.com/fondberg/hass_pushbullet_sms

## Battery checker
Script to check all batteries in the system. This adds a sensor called `sensor.battery_checker` with an integer as value which represents the number of devices has lower battery level than the `threshold`(default 40). If there were any devices with lower battery they will be added as attributes with their level to the state object.
### Installation
Install it by downloading it and copy it to `config/python_scripts/battery_checker.py`

### Automation
An example automation for it:
```
- alias: Check batteries every evening
  trigger:
    platform: time
    at: '18:00:00'
  action:
    - service: python_script.battery_checker
      data:
        threshold: 30
```

## Dim toggle
A small python script which cycles between different levels for the lights sent in as entitits

### Installation
Install it by downloading it and copy it to `config/python_scripts/dim_toggle.py`

### Automation
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
