from django.shortcuts import render,get_object_or_404,redirect
from django.db.models import Count,Prefetch,Sum
from django.utils import timezone
from .models import Event,Participant,Category
from .forms import EventForm,ParticipantForm,CategoryForm


#---- Homepage ----#

def home(request):
    today = timezone.now().date()
    previous_events = Event.objects.filter(date__lt=today).select_related('category')
    todays_events = Event.objects.filter(date=today).select_related('category')
    upcoming_events =  Event.objects.filter(date__gt=today).select_related('category')


    context = {
        'previous_events' : previous_events,
        'todays_events' : todays_events,
        'upcoming_events' : upcoming_events,
    }
    
    return render(request,'home.html',context)


#---- dashboard ----#

def dashboard(request):
    today = timezone.now().date()
    total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    previous_events = Event.objects.filter(date__lt=today).select_related('category')
    todays_events = Event.objects.filter(date=today).select_related('category')
    upcoming_events =  Event.objects.filter(date__gt=today).select_related('category')


    context = {
        'total_events' : total_events,
        'total_participants' : total_participants,
        'previous_events' : previous_events,
        'todays_events' : todays_events,
        'upcoming_events' : upcoming_events,
    }
    
    return render(request,'dashboard.html',context)

#---- Event_details ----#

def event_detail(request,pk):
    event = get_object_or_404(
        Event.objects.select_related('category').prefetch_related('participants'),
        pk=pk
    )
    
    return render(request,'event_detail.html',{'event' : event})

    
#---- Event_crud ----#
def event_list(request):
    query = request.GET.get('q')
    events = Event.objects.all().select_related('category').prefetch_related('participants')
    
    
    if query:
        events = events.filter(name__icontains=query) | events.filter(location__icontains=query)
        
        
    return render(request,'event_list.html',{'events' : events})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
        
        
    else:
        form = EventForm()
        
    return render(request,'event_form.html',{'form':form})


def event_update(request,pk):
    event = get_object_or_404(Event,pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST,request.FILES,instance=event)
        if form.is_valid():
            form.save()
            return redirect('event_list')
        
        
    else:
        form = EventForm(instance=event)
        
    return render(request,'event_form.html',{'form':form})


    
def event_delete(request,pk):
    event = get_object_or_404(Event,pk=pk)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')
        
    return render(request,'event_confirm_delete.html',{'event':event})



#---- category crud ----#

def category_list(request):
    categories = Category.objects.all()
    return render(request,'category_list.html',{'categories' : categories})


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        
        
    else:
        form = CategoryForm()
        
    return render(request,'category_form.html',{'form':form})

def category_update(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES,instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
        
        
    else:
        form = CategoryForm(instance=category)
        
    return render(request,'category_form.html',{'form':form})


    
def category_delete(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
        
    return render(request,'category_confirm_delete.html',{'category':category})

#---- participant crud ----#

def participant_list(request):
    participant = Participant.objects.all()
    return render(request,'participant_list.html',{'participants' : participant})



def participant_create(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
        
        
    else:
        form = ParticipantForm()
        
    return render(request,'participant_form.html',{'form':form})

def participant_update(request,pk):
    participant = get_object_or_404(Participant,pk=pk)
    if request.method == 'POST':
        form = ParticipantForm(request.POST,request.FILES,instance=participant)
        if form.is_valid():
            form.save()
            return redirect('participant_list')
        
        
    else:
        form = ParticipantForm(instance=participant)
        
    return render(request,'participant_form.html',{'form':form})


    
def participant_delete(request,pk):
    participant = get_object_or_404(Participant,pk=pk)
    if request.method == 'POST':
        participant.delete()
        return redirect('participant_list.html')
        
    return render(request,'participant_confirm_delete.html',{'participant':participant})


