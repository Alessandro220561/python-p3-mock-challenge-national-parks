class NationalPark:

    def __init__(self, name):
        self._name = None
        self.name = name

    @property   
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if self._name is None:
            if isinstance(name, str) and len(name) >= 3:
                self._name = name
            else:
                raise Exception
        else:
            raise ValueError("Name cannot be changed after intialization")
  
    def trips(self):
        return [trip for trip in Trip.all if isinstance(trip, Trip) and trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips() if isinstance(trip, Trip)})
    
    def total_visits(self):
        total_visits = 0
        for trip in Trip.all:
            if trip.national_park == self:
                total_visits += 1
        return total_visits
    
    def best_visitor(self):
        best_visitor = None
        best_visits = 0
        visitor_counts = {}

        for trip in Trip.all:
            if trip.national_park == self:
                visitor = trip.visitor
                if visitor in visitor_counts:
                    visitor_counts[visitor] += 1
                else:
                    visitor_counts[visitor] = 1

                if visitor_counts[visitor] > best_visits:
                    best_visitor = visitor
                    best_visits = visitor_counts[visitor]
        
        return best_visitor


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        if isinstance(visitor, Visitor):
            self.visitor = visitor
        if isinstance(national_park, NationalPark):
            self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        import re
        pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(st|nd|rd|th)$"
        if not isinstance(start_date, str):
            raise Exception
        if not len(start_date) >= 7:
            raise Exception
        if not re.match(pattern, start_date):
            raise Exception
        else:
            self._start_date = start_date

    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        import re
        pattern = r"^(January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}(st|nd|rd|th)$"
        if not isinstance(end_date, str):
            raise Exception
        if not len(end_date) >= 7:
            raise Exception
        if not re.match(pattern, end_date):
            raise Exception
        else:
            self._end_date = end_date



class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and 1 <= len(name) <= 15:
            self._name = name
        else:   
            raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if isinstance(trip, Trip) and trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips() if isinstance(trip.national_park, NationalPark)})
    
    def total_visits_at_park(self, park):
        total_visits = 0

        for trip in Trip.all():
            if trip.national_park == park and trip.visitor == self:
                total_visits += 1

        return total_visits