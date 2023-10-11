from django.shortcuts import render, redirect
from .forms import UploadFileForm
from django.http import HttpResponse
from django.core.files import File
from PIL import Image  # You may need to install the Pillow library


def index(request):
    context = {
        'welcome_message': 'Welcome to the Upload App!',
        'instructions': 'Please click the "Upload" link in the navigation to upload a file.',
    }
    return render(request, 'index.html', context)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            # Check if the file type is JPEG or PNG
            if not uploaded_file.name.endswith(('.jpg', '.jpeg', '.png')):
                return render(request, 'upload.html', {'form': form, 'error_message': 'Invalid file type. Please upload a JPEG or PNG file.'})
            
            # Handle the file upload here
            # You can save the file to a specific location or process it as needed
            # Example: Saving the file
         #   with open('path_to_save/' + uploaded_file.name, 'wb') as destination:
          #      for chunk in uploaded_file.chunks():
         #           destination.write(chunk)
            
          #  return redirect('success')  # Redirect to a success page
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


