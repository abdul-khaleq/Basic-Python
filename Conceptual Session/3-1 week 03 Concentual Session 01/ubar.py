from abc import ABC, abstractmethod
class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
    def add_rider(self, rider):
        self.riders.append(rider)
    def add_driver(self, driver):
        self.drivers.append(driver)
    def __repr__(self) -> str:
        return f'{self.company_name} has {len(self.riders)} riders and {len(self.drivers)}'

class User(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        self.nid = nid
    @abstractmethod
    def display_profile(self):
        raise NotImplementedError

class Driver(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_location = current_location
    def display_profile(self):
        print(f'Drivers name is {self.name} and email is {self.email}')

class Rider(User):
    def __init__(self, name, email, nid, current_location) -> None:
        super().__init__(name, email, nid)
        self.current_rider = None
        self.current_location = current_location
    def display_profile(self):
        print(f'Riders name is {self.name} and email is {self.email}')
    def ride_request(self, uber, destination):
        print('-----looking for ride--------')
        if not self.current_rider:
            ob = Ride_Matching(uber.drivers)
            res = ob.has_driver(self, destination)
            print(f'Your result is {res}')
            self.current_ride = res
            return True
        else:
            return False


class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
    def start_rider(self):
        pass
    def end_location(self):
        pass
    def __repr__(self) -> str:
        return f'Start from {self.start_location} to {self.end_location}'

class Ride_Matching:
    def __init__(self, drivers) -> None:
        self.drivers = drivers
    def has_driver(self, rider, destination):
        if len(self.drivers) > 0:
            ride = Ride(rider.current_location, destination)
            return ride
        else:
            return 'Driver not found'

uber = Ride_Sharing('UBER')
alice = Driver('Alice', 'alice@gmnail.com', 12345, 'Sherpur')
sakib = Rider('sakib', 'sakib@gmail.com', 1236, 'Bogura n')

uber.add_driver(alice)
uber.add_rider(sakib)

if sakib.ride_request(uber, 'Dhaka'):
    print('-----Travelling--------')
else:
    print('-----No ride found--------')