from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from .models import ImageUpload

def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('upload_success')
    else:
        form = ImageUploadForm()
        images = ImageUpload.objects.all()  # 获取所有上传的图片
    return render(request, 'uploader/upload.html', {'form': form, 'images': images})

def upload_success(request):
    return render(request, 'uploader/success.html')
