# LIFX-API
A limited python library for communicating with the LIFX API.

Offers the following functionalities:
  * Toggle lights (on/off) with one method call. When toggling on, the lights will intelligently change depending on the time of the day (e.g. energetic in the morning, warm in the evening)
  * Turn off the lights (duh)
  * Turn on night lights, e.g. a preset for dark red colour
  * Breathe lights (turning the light on for less than a minute).

This library works with the LIFX Cloud. Please note that there are other libraries allowing for way more functionalities.
  
# Usage
import lifx

lifx().toggleIntelligent()
