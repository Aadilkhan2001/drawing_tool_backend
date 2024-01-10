from rest_framework.renderers import JSONRenderer

class ResponseRenderer(JSONRenderer):
    """
    Custom JSON renderer for consistent API response structure.

    This renderer wraps the actual data in a standardized structure including
    a 'success' flag, the 'data' itself, and an 'error' field when an exception occurs.

    """

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context.get('response')

        if response is not None and (response.exception or response.status_code >= 400):
            response_data = {
                'success': False,
                'data': None,
                'error': {
                    'status_code': response.status_code,
                    'detail': data if data else 'Internal Server Error',
                },
            }
        else:
            response_data = {
                'success': True,
                'data': data,
                'error': None,
            }

        return super().render(response_data, accepted_media_type, renderer_context)