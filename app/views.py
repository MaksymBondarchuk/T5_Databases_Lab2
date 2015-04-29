from django.shortcuts import render
from django.db import transaction
from server_test import *

# Create your views here.


def home(request):
    return render(request, "/admin/", {})


def server(request):
    return render(request, "server_test_home.html", {"trigger_table": get_data("trigger_test"), "transaction_table": get_data("transaction_test"), "event_table": get_data("event_test")})


def server_trigger_start(request):
    start_trigger()
    return render(request, "server_test_home.html", {"trigger_table": get_data("trigger_test"), "transaction_table": get_data("transaction_test"), "event_table": get_data("event_test")})


def server_trigger_stop(request):
    stop_trigger()
    return render(request, "server_test_home.html", {"trigger_table": get_data("trigger_test"), "transaction_table": get_data("transaction_test"), "event_table": get_data("event_test")})


def server_stored_procedure(request):
    return render(request, "server_test_home.html", {"procedure_table": get_data_proc(request.GET["name"]), "trigger_table": get_data("trigger_test"), "transaction_table": get_data("transaction_test"), "event_table": get_data("event_test")})


def server_execute(request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute(request.GET["code"])
    db.commit()
    return render(request, "server_test_home.html", {"trigger_table": get_data("trigger_test"), "transaction_table": get_data("transaction_test"), "event_table": get_data("event_test")})


def create_event(request):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("CREATE EVENT " + request.GET["name"] + " \
                    ON SCHEDULE " + request.GET["schedule"] + " \
                    DO delete from app_user")
    db.commit()
    return render(request, "server_test_home.html", {"trigger_table": get_data("trigger_test"), "transaction_table": get_data("transaction_test"), "event_table": get_data("event_test")})


# @transaction.atomic
# def trans(request):
#     sid = transaction.savepoint()
#     transaction.savepoint_commit(sid)
#     transaction.savepoint_rollback(sid)
