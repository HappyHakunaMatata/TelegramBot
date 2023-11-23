"""
Definition of views.
"""


from datetime import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from app.models import DailyMessages, DateTimeMessages, WeeklyMessages, ProgressBarStatus, KickTimeTable
from .forms import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DailyMessagesSerializer, ProgressBarStatusSerializer
import asyncio
from app.telegrambot import Auth, send_message
from django.shortcuts import get_list_or_404
from rest_framework import status
from django.shortcuts import render, redirect
from app.decorators import telethon_login_requierd

#@telethon_login_requierd
def home(request):
    tableDailymessages = DailyMessages.objects.all()
    tableDatetimemessages = DateTimeMessages.objects.all()
    tableWeeklymessages = WeeklyMessages.objects.all()
    PBStatus = ProgressBarStatus.objects.first()
    addDailyMessagesForm = AddDailyMessagesForm()
    editDailyMessagesForm = EditDailyMessagesForm()
    deleteDailyMessagesForm = DeleteDailyMessagesForm()
    addDatetimeMessagesForm = AddDatetimeMessagesForm()
    editDatetimeMessagesForm = EditDatetimeMessagesForm()
    deleteDatetimeMessagesForm = DeleteDatetimeMessagesForm()
    sendMessageForm = SendMessageForm()
    addWeeklyMessagesForm = AddWeeklyMessagesForm()
    editWeeklyMessagesForm = EditWeeklyMessagesForm()
    deleteWeeklyForm = DeleteWeeklyForm()
    
    progressBarStatus = ProgressBarStatusForm()
    kickTimeTableForm = KickTimeTableForm()
    KickTime = KickTimeTable.objects.first()

    message = ''
    if request.method == 'POST':
        if (request.POST.get('form_type') == 'AddDailyMessage'):
            addDailyMessagesForm = AddDailyMessagesForm(request.POST)
            if addDailyMessagesForm.is_valid():
                addDailyMessagesForm.save()
                message = "Сообщение добавлено"
        elif (request.POST.get('form_type') == 'EditDailyMessage'):
            editDailyMessagesForm = EditDailyMessagesForm(request.POST)
            if editDailyMessagesForm.is_valid():
                pk = editDailyMessagesForm.cleaned_data['key']
                daily_message = get_object_or_404(DailyMessages, primaryKey=pk)
                daily_message.text = editDailyMessagesForm.cleaned_data['edittext']
                daily_message.timestamp = editDailyMessagesForm.cleaned_data['edittimestamp']
                daily_message.save()
                message = "Сообщение отредактировано"
        elif (request.POST.get('form_type') == 'DeleteDailyMessage'):
            deleteDailyMessagesForm = DeleteDailyMessagesForm(request.POST)
            if deleteDailyMessagesForm.is_valid():
                pk = deleteDailyMessagesForm.cleaned_data['primaryKey']
                daily_message = get_object_or_404(DailyMessages, primaryKey=pk)
                daily_message.delete()
                message = "Сообщение удалено"
        elif (request.POST.get('form_type') == 'AddDatetimeMessage'):
            addDatetimeMessagesForm = AddDatetimeMessagesForm(request.POST)
            if addDatetimeMessagesForm.is_valid():
                addDatetimeMessagesForm.save()
                message = "Сообщение добавлено"
        
        elif (request.POST.get('form_type') == 'EditDatetimeMessage'):
            editDatetimeMessagesForm = EditDatetimeMessagesForm(request.POST)
            if editDatetimeMessagesForm.is_valid():
                pk = editDatetimeMessagesForm.cleaned_data['idDatetime']
                daily_message = get_object_or_404(DateTimeMessages, primaryKey=pk)
                daily_message.textfield = editDatetimeMessagesForm.cleaned_data['textfield']
                daily_message.timestampfield = editDatetimeMessagesForm.cleaned_data['timestampfield']
                daily_message.datefield = editDatetimeMessagesForm.cleaned_data['editdatefield']
                daily_message.save()
                message = "Сообщение отредактировано"
        elif (request.POST.get('form_type') == 'DeleteDatetimeMessage'):
            deleteDatetimeMessagesForm = DeleteDatetimeMessagesForm(request.POST)
            if deleteDatetimeMessagesForm.is_valid():
                pk = deleteDatetimeMessagesForm.cleaned_data['Pkey']
                daily_message = get_object_or_404(DateTimeMessages, primaryKey=pk)
                daily_message.delete()      
                message = "Сообщение удалено"
        elif (request.POST.get('form_type') == 'SendMessage'):
            sendMessageForm = SendMessageForm(request.POST)
            if sendMessageForm.is_valid():
                message_text = sendMessageForm.cleaned_data['sendMessage']
                asyncio.run(send_message(message_text))
                message = "Сообщение отправлено"

        elif (request.POST.get('form_type') == 'AddWeeklyMessage'):
            addWeeklyMessagesForm = AddWeeklyMessagesForm(request.POST)
            if addWeeklyMessagesForm.is_valid():
                addWeeklyMessagesForm.save()
                message = "Сообщение добавлено"
        elif (request.POST.get('form_type') == 'DeleteWeeklyMessage'):
            deleteWeeklyForm = DeleteWeeklyForm(request.POST)
            if deleteWeeklyForm.is_valid():
                pk = deleteWeeklyForm.cleaned_data['idDeleteWeekly']
                daily_message = get_object_or_404(WeeklyMessages, primaryKey=pk)
                daily_message.delete()      
                message = "Сообщение удалено"  
                
        elif (request.POST.get('form_type') == 'EditWeeklyMessage'):
            editWeeklyMessagesForm = EditWeeklyMessagesForm(request.POST)
            if editWeeklyMessagesForm.is_valid():
                pk = editWeeklyMessagesForm.cleaned_data['idWeekly']
                daily_message = get_object_or_404(WeeklyMessages, primaryKey=pk)
                daily_message.AddWeeklyMessage = editWeeklyMessagesForm.cleaned_data['AddWeeklyMessage']
                daily_message.AddTimestamp = editWeeklyMessagesForm.cleaned_data['AddTimestamp']
                daily_message.AddWeek = editWeeklyMessagesForm.cleaned_data['AddWeek']
                daily_message.save()
                message = "Сообщение отредактировано"
        
        elif (request.POST.get('form_type') == 'KickToggler'):
            progressBarStatus = ProgressBarStatusForm(request.POST)
            if progressBarStatus.is_valid():
                entity = get_object_or_404(ProgressBarStatus, ProgressbarPKey=1)
                entity.ProgressbarStatus = True if progressBarStatus.cleaned_data['ProgressbarStatus'] == 1 else False
                PBStatus = entity
                entity.save()
                message = "Параметр сохранен"
        elif (request.POST.get('form_type') == 'EditToggleTime'):
            form = KickTimeTableForm(request.POST)
            if form.is_valid():
                entity = get_object_or_404(KickTimeTable, PKey=1)
                entity.Time = form.cleaned_data['edittoggletime']
                KickTime = entity
                entity.save()
                message = "Время сохранено"
        else:
            message = "Произошла ошибка"
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
            'addDailyMessagesForm': addDailyMessagesForm,
            'editDailyMessagesForm': editDailyMessagesForm,
            'deleteDailyMessagesForm': deleteDailyMessagesForm,
            'addDatetimeMessagesForm': addDatetimeMessagesForm,
            'editDatetimeMessagesForm': editDatetimeMessagesForm,
            'deleteDatetimeMessagesForm': deleteDatetimeMessagesForm,
            'sendMessageForm': sendMessageForm,
            'tableDailymessages': tableDailymessages,
            'tableDatetimemessages': tableDatetimemessages,
            'progressBarStatus': progressBarStatus,
            'message': message,
            'PBStatus': PBStatus,
            'kickTimeTableForm': kickTimeTableForm,
            'tableWeeklymessages': tableWeeklymessages,
            'addWeeklyMessagesForm': addWeeklyMessagesForm,
            'editWeeklyMessagesForm': editWeeklyMessagesForm,
            'kickTime': KickTime,
        }
    )

def login(request):
    message = ''
    if request.method == 'POST':
        form = AuthTelethonForm(data=request.POST)
        if form.is_valid():
            result = asyncio.run(Auth(True))
            if (result == True):
                return redirect('home')
            else:
                message = "Произошла ошибка"   
        else:
            message = form.errors
    else:
        form = AuthTelethonForm()
    return render(
        request, 
        'app/login.html',
        {
            'title': 'Login Page',
            'year': datetime.now().year,
            'form': form, 
            'message': message
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
        
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


@api_view(['GET'])
def get_data(request):
    data = DailyMessages.objects.all()  # Замените на ваш запрос к базе данных
    serializer = DailyMessagesSerializer(data, many=True)
    return Response(serializer.data)


"""
@api_view(['GET'])
def Get_ProgressbarStatus(request):
    data = get_list_or_404(ProgressBarStatus)
    serializer = ProgressBarStatusSerializer(data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def Post_ProgressbarStatus(request):
    if request.method == 'POST':
        serializer = ProgressBarStatusSerializer(data=request.data)
        if serializer.is_valid():
            serialized_data = serializer.data
            progressbar_status = serialized_data.get('ProgressbarStatus')
            progressbar = get_object_or_404(ProgressBarStatus)
            progressbar.ProgressbarStatus = progressbar_status
            progressbar.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """    