from django.http import HttpResponse

class StripeWH_Handler:
    """
    handles stripe webhooks
    """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        handles the generic and unknown/unexpected webook events
        """

        return HttpsResponse(
            cntent=f'webhook receoved: {event["type"]}',
            status=200)