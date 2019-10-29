from rest_framework import routers
from factories.viewsets import FactoryViewSet
from employee.viewsets import EmployeeViewSet
from teams.viewsets import TeamsViewSet

router = routers.DefaultRouter()

router.register(r'factories', FactoryViewSet)
router.register(r'employee', EmployeeViewSet)
router.register(r'teams', TeamsViewSet)