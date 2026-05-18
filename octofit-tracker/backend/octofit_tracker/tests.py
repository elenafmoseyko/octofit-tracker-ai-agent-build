from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(str(team), 'Test Team')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        self.assertEqual(str(user), 'testuser')

    def test_create_activity(self):
        team = Team.objects.create(name='Test Team')
        user = User.objects.create_user(username='testuser', email='test@example.com', password='pass')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, team=team)
        self.assertEqual(str(activity), 'testuser - Run')

    def test_create_leaderboard(self):
        team = Team.objects.create(name='Test Team')
        leaderboard = Leaderboard.objects.create(team=team, points=100)
        self.assertEqual(str(leaderboard), 'Test Team: 100')

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='desc', suggested_for='Test')
        self.assertEqual(str(workout), 'Test Workout')
