class ActivityRepository:
    def __init__(self):
        self.__activities = []

    def add_activity(self, activity):
        self.__activities.append(activity)

    def get_activities(self):
        return self.__activities

    def get_activity_by_id(self, activity_id):
        for activity in self.__activities:
            if activity.get_activity_id() == activity_id:
                return activity

    def remove_activity_by_id(self, activity_id):
        for activity in self.__activities:
            if activity.get_activity_id() == activity_id:
                self.__activities.remove(activity)

    def update_activity(self, activity_id, new_date, new_time, new_description):
        for activity in self.__activities:
            if activity.get_activity_id() == activity_id:
                activity._Activity__date = new_date
                activity._Activity__time = new_time
                activity._Activity__description = new_description

    def add_person_to_activity(self, activity_id, person_id):
        for activity in self.__activities:
            if activity.get_activity_id() == activity_id:
                activity.get_person_id().append(person_id)

    def remove_person_from_activity(self, activity_id, person_id):
        for activity in self.__activities:
            if activity.get_activity_id() == activity_id:
                activity.get_person_id().remove(person_id)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.__activities}"
