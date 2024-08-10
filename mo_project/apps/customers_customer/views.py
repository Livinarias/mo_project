from django.http.response import HttpResponse
from django.shortcuts import render

from .modules.upload_file import UploadFileForm
from .strategy.context.strategy_context import Context
from .strategy.strategy_csv import ConcreteStrategyCSV
from .strategy.strategy_txt import ConcreteStrategyTXT
from .enums.custumers_enums import ExtensionFiles

from typing import ByteString


# Create your views here.
def upload_file(request) -> HttpResponse:
    """Method recieve file"""
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if validate_file(form, request):
            return render(request, 'customer_success.html', {})
        return render(request, 'error_404.html', {}, status=404)
    else:
        form = UploadFileForm()
        return render(request, 'create_customer.html', {'form': form})

def validate_file(form, request) -> None:
    """Method to validate file"""
    if form.is_valid():
        archivo = request.FILES['archivo']
        extension_file = archivo.name.split('.')[1]
        return validate_extension(extension_file, archivo)

def validate_extension(extension_file: str, archivo: ByteString) -> None:
    """Method validate if extension is csv or txt to use strategy class"""
    context = Context(ConcreteStrategyCSV())
    if extension_file and extension_file == ExtensionFiles.CSV.value:
        print("extension", extension_file)
        context.create_customer(archivo, extension_file)
        return True
    if extension_file and extension_file == ExtensionFiles.TXT.value:
        context.strategy = ConcreteStrategyTXT()
        context.create_customer(archivo, extension_file)
        return False
