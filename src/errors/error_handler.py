from src.views.http_types.http_response import HttpResponse
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

def handle_errors(error: Exception) -> HttpResponse:
    if isinstance(error, HttpUnprocessableEntityError):

        # If needed, we can apply more changes in here, like report the error on a e-mail, etc.

        return HttpResponse(
            status_code=error.status_code,
            body={
                "errors": [ {
                    "title": error.name,
                    "details": error.message,
                }]
            }
        )

    return HttpResponse(
        status_code=500,
        body={
        "errors": [{
            "title": "Server Error",
            "detail": str(error)
        }]
    })
