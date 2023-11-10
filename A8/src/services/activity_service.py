import unittest


from unittest import TestCase
from src.domain.activity_domain import Activity
from src.repository.activity_repository import ActivityRepository


class ActivityService:
    def __init__(self, activity_repository):
        self.__activity_repository = activity_repository

    def add_activity(self, activity_id, date, time, description):
        activity = Activity(activity_id, date, time, description)
        self.__activity_repository.add_activity(activity)

    def remove_activity(self, activity_id):
        self.__activity_repository.remove_activity_by_id(activity_id)

    def update_activity(self, activity_id, new_date, new_time, new_description):
        self.__activity_repository.update_activity(activity_id, new_date, new_time, new_description)

    def get_all_activities(self):
        return self.__activity_repository.get_activities()

    def get_activity_by_id(self, activity_id):
        return self.__activity_repository.get_activity_by_id(activity_id)

    def search_activities(self, search: str):
        activities = self.__activity_repository.get_activities()
        activities_found = []
        for activity in activities:
            if search.lower() == activity.date.lower():
                activities_found.append(activity)
            elif search.lower() == activity.time.lower():
                activities_found.append(activity)
            elif search.lower() in activity.description.lower():
                activities_found.append(activity)
        return activities_found

    def add_person_to_activity(self, activity_id, person_id):
        self.__activity_repository.add_person_to_activity(activity_id, person_id)

    def remove_person_from_activity(self, activity_id, person_id):
        self.__activity_repository.remove_person_from_activity(activity_id, person_id)

    def get_activities_by_date(self, date):
        activities = self.__activity_repository.get_activities()
        activities_found = []
        for activity in activities:
            if date.lower() == activity.date.lower():
                activities_found.append(activity)
        return activities_found

    def get_busiest_days(self):
        activities = self.__activity_repository.get_activities()
        dates = []
        for activity in activities:
            dates.append(activity.date)
        dates.sort()
        busiest_days = []
        for date in dates:
            if date not in busiest_days:
                busiest_days.append(date)
        return busiest_days
