class AuthMiddleware:
    def __call__(self, request):
    # TODO: validate JWT signature and expiry
    # TODO: support API-key fallback auth
        return request
