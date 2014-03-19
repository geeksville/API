# Drone API (DApi) module

def webConnect(username, password):
    return APIConnection()

def localConnect():
    return APIConnection()

class Mission(object):
    """PLACEHOLDER
    
    Access to historical missions will not be included in the release 1 python API, they will only be accessible
    from the REST API.  (This is based on the most likely use-cases wanting a REST interface)"""
    pass

class Parameters(object):
    """The set of named parameters for the vehicle"""
    
    def __getattr__(self, name):
        pass
    
    def __setattr__(self, name, value):
        pass

class Waypoint(object):
    pass

class Waypoints(object):
    def __init__(self):
        self._next = None
    
    @property
    def next(self):
        """Currently active waypoint number"""
        return self._next

    @property.setter
    def _set_next(self, value):
        """Tell vehicle to change next waypoint"""
        pass

class Vehicle(object):
    def __init__(self):
        self.waypoints = Waypoints()
        self.parameters = Parameters()
        
    def delete(self):
        """Delete this vehicle object
        This requests deletion of the object on the server, this operation may throw an exception on failure (i.e. for
        local connections or insufficient user permissions)"""
        pass
    
    def get_mission(self):
        """PLACEHOLDER
        
        Access to historical missions will not be included in the release 1 python API, they will only be accessible
        from the REST API.  (This is based on the most likely use-cases wanting a REST interface)"""        
        return Mission()
    
    def flush(self):
        """It is important to understand that setting attributes/changing vehicle state may occur over a slow link.
        It is _not_ guaranteed that the effects of previous commands will be visible from reading vehicle attributes unless
        flush() is called first.  After the return from flush any writes are guaranteed to have completed (or thrown an
        exception) and future reads will see their effects."""
        pass
    
    def __getattr__(self, name):
        """
        Particular autopilots/vehicles may define different attributes from this standard list (extra batteries, GPIOs, etc...)
        However if a standard attribute is defined it must follow the rules specified below.
        
        To prevent name clashes the following naming convention should be used:
        ap_<name> - For autopilot specific parameters (apm 2.5, pixhawk etc...).  Example: 
        user_<name> - For user specific parameters
        
        Standard attributes & types:
        location: (latitude, longitude, altitude-msl)
        waypoint_home: Waypoint
        attitude: (pitch, yaw, roll)
        mode: string
        battery_0_soc: double
        battery_0_volt: double
        rc_overrides: [ integers ]
        rc_channels: [ integers ] (read only)
        
        ap_pin5_mode: string (adc, dout, din)
        ap_pin5_value: double (0, 1, 2.3 etc...)
        
        FIXME - address the units issue?
        FIXME - is there any benefit of using lists rather than tuples for these attributes
        """
        try:
            return self.__dict[name]
        except KeyError:
            msg = "'{0}' object has no attribute '{1}'"
            raise AttributeError(msg.format(type(self).__name__, name))
    
    def __setattr__(self, name, value):
        """Note: Exceptions due to loss of communications, missing attributes or insufficient permissions are not guaranteed
        to be thrown from inside this method.  Most failures will not be seen until flush() is called.  If you require immediate
        notification of failure set autoflush."""
        pass
    
class APIConnection(object):
    def get_vehicles(self, fixme):
        return [ Vehicle(), Vehicle() ]
    
    