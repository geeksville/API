# Python highlevel sketch

api = DApi.webConnect(username, password)
api = DApi.gcsConnect(‘localhost’)
api = DApi.vehicleLocalConnect()

# Get all vehicles user has access to (may be capped in the web case)
# includeOffline is an optional param, if true non connected vehicles will be included (for historical purposes)
# if includeLive is true, currently connected vehicles will be included
vehicles = api.getVehicles(includeLive = True)

# Get all vehicles user has access to and within the specified rectangle
vehicles = api.getVehicles(lat1, lon1, lat2, lon2, includeOffline = False)

v = api.createVehicle(vehicleId, vehicleType, notes)

v.delete()

v.getLocation()
v.getAttitude()
v.getAirspeed()
v.getGroundspeed()

# get battery level etc...
v.getBatteryVoltage() 
v.getBatterySOC()

v.getRCChannels()
v.setRCOverride(channel1, channel2, …)

v.getMode()
v.setMode(mode)
v.goto(location)
wpts = v.getWaypoints()
v.setWaypoints(wpts)

# where logId is either a log id or ‘recent’ for most recent log, or ‘current’ for the current live log
# flight logs are streams of annotated mavlink messages.  The flightlog object also includes metadata
# about that flight.
flog = v.getFlightlog(logId)

# Operations for uploading flogs
flog = v.createFlight(‘notes’)
flog.uploadMavlink(timestampedPackets)
flog.endFlight()

# Delete flight log
flog.delete()

# The complete set of mavlink messages (mostly useful in case of historical logs)
packets = flog.getMavlink()
# Callback will be invoked asynchronously for each new mavlink message received
flog.setMavlinkCallback(callback)

locations = flog.getLocations()
flog.setLocationCallback(callback)

modes = flog.getMode

# To send raw mavlink to a vehicle
v.sendMavlink(packet)

# Wait for all previously queued async (reactive) operations to acknowledge)
v.sync()

# For release 2 add GPIO/ADC operations (needs vehicle code)
v.getADC(pin)
v.setDAC(pin)
v.getGPIO(pin)
v.setGPIO(pin, value)

# GCS GUI integration in release 2
gcs = api.getGCS()
buttonId = gcs.addCheckbox(‘mapScreen’, ‘Follow Me’, callback)
