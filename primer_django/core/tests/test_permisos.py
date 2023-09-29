from django.test import TestCase, RequestFactory
from django.contrib.auth.models import AnonymousUser, User, Permission
from core.views import Permisos
from django.core.exceptions import PermissionDenied


class PermisosTest(TestCase):
    def setUp(self):
        # Cada prueba necesita acceso a la solicitud.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@…', password='top_secret')

    def test_anonymous_user(self):
        # Simula una solicitud GET anónima
        request = self.factory.get('/permisos')
        request.user = AnonymousUser()

        response = Permisos.as_view()(request)

        # Verifica si redirecciona al usuario anónimo al login_url
        self.assertEqual(response.status_code, 302)
        self.assertIn('/admin', response.url)

    def test_logged_in_user_without_permission(self):
        # Simula una solicitud GET del usuario sin permiso
        request = self.factory.get('/permisos')
        request.user = self.user
        with self.assertRaises(PermissionDenied):
            response = Permisos.as_view()(request)

            # Verifica si redirecciona al usuario sin permiso al login_url
            self.assertEqual(response.status_code, 302)
            self.assertIn('/admin', response.url)

    def test_logged_in_user_with_permission(self):
        # Asigna el permiso al usuario
        permission = Permission.objects.get(codename='view_movie')
        self.user.user_permissions.add(permission)

        request = self.factory.get('/permisos')
        request.user = self.user

        response = Permisos.as_view()(request)

        # La respuesta debe ser 200 OK.
        self.assertEqual(response.status_code, 200)
