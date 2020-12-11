import calendar

class DVD:
    from datetime import datetime

    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    def __repr__(self):
        rent = ""
        if self.is_rented:
            rent = "rented"
        else:
            rent = "not rented"

        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction" \
               f" {self.age_restriction}. Status: {rent}"

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        sparsed_dates = cls.datetime.strptime(date, "%d.%m.%Y")

        return cls(name, id, sparsed_dates.year, calendar.month_name[sparsed_dates.month], age_restriction)

