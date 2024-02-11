from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
    Responsable class for interacting with HTTP
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        product_code = body["product_code"]

        # Tag Creation Rules
        print("Estou na view")
        # Http Response
        return HttpResponse(status_code=200, body = {"hello": "world"})
    