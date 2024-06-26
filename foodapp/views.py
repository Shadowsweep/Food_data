import csv
import json
from io import TextIOWrapper
from django.shortcuts import render
from .forms import CSVUploadForm
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import Food
from io import TextIOWrapper

# def upload_csv(request):
#     if request.method == 'POST':
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             csv_file = request.FILES['csv_file']
#             # Assuming UTF-8 encoding, adjust if necessary
#             csv_data = TextIOWrapper(csv_file, encoding='utf-8')
#             reader = csv.DictReader(csv_data)

#             for row in reader:
#                 food = Food(
#                     food_id=row['id'],
#                     food_name=row['name'],
#                     location=row['location'],
#                     items=row['items'],
#                     lat_long=row['lat_long'],
#                     full_details=row['full_details']
#                 )
#                 food.save()

#             return render(request, 'upload_success.html')
#     else:
#         form = CSVUploadForm()

#     return render(request, 'upload_form.html', {'form': form})


def upload_csv(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            try:
                # Save the CSV file to the static/uploads directory
                fs = FileSystemStorage(location='static/uploads')
                filename = fs.save(csv_file.name, csv_file)
                csv_file_path = fs.path(filename)

                # Assuming UTF-8 encoding, adjust if necessary
                with open(csv_file_path, encoding='utf-8') as file:
                    reader = csv.DictReader(file)
                    for row in reader:
                        food = Food(
                            food_id=row['id'],
                            food_name=row['name'],
                            location=row['location'],
                            items=row['items'],
                            lat_long=row['lat_long'],
                            full_details=row['full_details']
                        )
                        food.save()

                return render(request, "upload_form.html", {"message": "Record Submitted Successfully"})
            except Exception as e:
                return render(request, "upload_form.html", {"message": "Failed to submit"})
        else:
            messages.error(request, 'Form is not valid.')
    else:
        form = CSVUploadForm()

    return render(request, 'upload_form.html', {'form': form})


def display_food(request):
    foods = Food.objects.all()  # Fetch all food records from the database\
    for food in foods:
        full_details = json.loads(food.full_details)
        food.cuisines = full_details.get('cuisines', '')
        
    
    context = {
        'foods': foods,
        # ... other context variables ...
    }
    return render(request, 'search_food.html', {'foods': foods})
def view_food(request):
    foods = Food.objects.all()  # Fetch all food records from the database\
    
    return render(request, 'upload_form.html', {'foods': foods})

