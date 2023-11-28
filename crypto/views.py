from django.http import JsonResponse
from crypto.tasks import send_crypto_quote


def add_message(request):
    task_result = send_crypto_quote.delay()
    return JsonResponse({"task_id": task_result})
