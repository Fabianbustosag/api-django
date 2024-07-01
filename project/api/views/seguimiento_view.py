# views.py
from django.http import JsonResponse
from .. models import Food
from django.db.models import Count
from datetime import datetime, timedelta, date

def get_weekly_summary(request):
    today = date.today()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)

    foods = Food.objects.filter(food_state=1, discard_date__range=[week_start, week_end])
    food_counts = foods.values('discard_date').annotate(count=Count('food_id')).order_by('discard_date')

    weekly_summary = [0] * 7
    for food_count in food_counts:
        day_of_week = (food_count['discard_date'] - week_start).days
        weekly_summary[day_of_week] = food_count['count']

    return JsonResponse({'weekly_summary': weekly_summary})