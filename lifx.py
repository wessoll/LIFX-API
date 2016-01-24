import requests
import datetime
import time

# Config
lifx_usertoken = "your_lifx_api_token_goes_here"

# LIFX Endpoints
lifx_breathe_url = "https://api.lifx.com/v1/lights/all/effects/breathe"
lifx_state_url = "https://api.lifx.com/v1/lights/all/state"
lifx_toggle_url = "https://api.lifx.com/v1/lights/all/toggle"

class lifx:
        # Breathe the lights (turning it on for less than a minute)
        def breatheLights(self):
                params = {"color": "white",
                        "period": "45",
                        "persist": "false",
                        "power_on": "true",
                        "peak": "0.1"}

                response = requests.post(lifx_breathe_url, json = params, headers = {"Authorization": "Bearer " + lifx_usertoken})

        # Sets the lights to a dark red colour
        def nightLights(self):
                params = {"color": "red saturation:1.0 brightness:0.3",
                           "power": "on"}

                response = requests.put(lifx_state_url, json = params, headers = {"Authorization": "Bearer " + lifx_usertoken})

        # Turns on or off the lights. If the lights are turned on, a colour is been set matching the hour of the day. E.g. in the morning a very energetic colour, in the evening a warm though bright colour and at night a warm though dark colour.
        def toggleIntelligent(self):
                response = requests.post(lifx_toggle_url, headers = {"Authorization": "Bearer " + lifx_usertoken})

                # select appropriate colour
                now = int(datetime.datetime.now().strftime("%H"))
                now+= 1 # compensate for timezone (very bad coding)
                params = None

                if now >= 5 and now <= 17: # Very cold and bright
                        params = {"color": "kelvin:9000 brightness:1.0"}
                elif now > 17 and now <= 20: # Warm and bright
                        params = {"color": "kelvin:2500 brightness:1.0"}
                else: # Warm and a little darker
                        params = {"color": "kelvin:2500 brightness:0.5"}

                response = requests.put(lifx_state_url, json = params, headers = {"Authorization": "Bearer " + lifx_usertoken})


        # Turn on or off lights
        def power(self, isOn):
                params = {"color": "white saturation:0.5",
                           "power": "on" if isOn else "off"}

                response = requests.put(lifx_state_url, json = params, headers = {"Authorization": "Bearer " + lifx_usertoken})
                                        
