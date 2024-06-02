from django.shortcuts import render
from django.conf import settings
import os
from .excel_utils import parse_excel_file


def index(request):
    files = os.listdir(settings.EXCEL_DIRECTORY)
    files = [f for f in files if f.endswith('.xlsx')]
    return render(request, 'excelparser/index.html', {'files': files})


def view_file(request, filename):
    file_path = os.path.join(settings.EXCEL_DIRECTORY, filename)
    data = parse_excel_file(file_path)
    sheet_names = list(data.keys())
    first_sheet = sheet_names[0] if sheet_names else None
    return render(request, 'excelparser/view_file.html',
                  {'filename': filename, 'data': data, 'sheet_names': sheet_names, 'current_sheet': first_sheet})


def view_sheet(request, filename, sheet_name):
    file_path = os.path.join(settings.EXCEL_DIRECTORY, filename)
    data = parse_excel_file(file_path)
    sheet_data = data.get(sheet_name, [])
    sheet_names = list(data.keys())
    return render(request, 'excelparser/view_sheet.html', {
        'filename': filename,
        'data': sheet_data,
        'sheet_names': sheet_names,
        'current_sheet': sheet_name,
    })