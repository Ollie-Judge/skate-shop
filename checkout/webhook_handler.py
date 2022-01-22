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
            content=f'Unhandled webhook receoved: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        handles the payment_intent_succeeded webhook
        """

        return HttpsResponse(
            content=f'webhook receoved: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        handles the payment_intent_failed webhook
        """

        return HttpsResponse(
            content=f'webhook receoved: {event["type"]}',
            status=200)
