from .user import User, Student, Professor
from .academic import Course, Class, Enrollment, Activity, Attendance
from .gamification import Achievement, StudentAchievement, Quest, StudentQuest

__all__ = [
    'User', 'Student', 'Professor',
    'Course', 'Class', 'Enrollment', 'Activity', 'Attendance',
    'Achievement', 'StudentAchievement', 'Quest', 'StudentQuest'
]