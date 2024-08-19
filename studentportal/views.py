from django.shortcuts import render
from django.http import JsonResponse
from .models import Student, Meals, MealsHistory


# Create your views here.
def pay(request):
    print("REQUEST: ", request.GET)
    mealsHistory = dict(eval(request.GET.get("meals")))  # list of meals

    print("MEALS: ", type(mealsHistory), " ", mealsHistory, "\n")

    card = mealsHistory.get("uid")

    m_copy = mealsHistory
    m_copy.pop("uid")
    food_stuffs = m_copy

    total_amount = 0
    print("DICT:", food_stuffs.items())
    for food_id, food_details in food_stuffs.items():
        print("FD: ", food_details)
        total_amount += food_details.get("price")

    print("STUFF:", food_stuffs, "Total Amount:", total_amount)

    # check if the card has enough balance
    # proceed with the payment
    # update the card balance
    # update the meal count
    # return success message

    # check if the card exists in the system
    try:
        student = Student.objects.get(rfid=card)
    except Student.DoesNotExist:
        student = None

    print("Student:", student)

    if student is None:
        print("Card not found")
        return JsonResponse({"status": "error", "message": "Student not found"})

    if student.balance < total_amount:
        print("Insufficient balance")
        return JsonResponse(
            {
                "status": "warning",
                "message": "Insufficient balance",
                "student_name": student.first_name + " " + student.last_name,
            }
        )
    student.balance -= total_amount
    # MealsHistory.objects.create(student=student, meal=Meals.objects.get(name=meals))
    student.save()

    mealsHistory = MealsHistory.objects.create(student=student, meal=mealsHistory)
    mealsHistory.save()
    print("Meals:", mealsHistory, "Payment successful")
    return JsonResponse(
        {
            "status": "success",
            "message": "Payment successful",
            "student_name": student.first_name + " " + student.last_name,
        }
    )
