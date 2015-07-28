from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader, Context
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from App.forms import UserForm, UserProfileForm
from django.conf import settings
from django.db.models import Q
from App.models import *

# Create your views here.

def index(request):
    # Redirect to feed if logged in
    if request.user.is_authenticated():
        return HttpResponseRedirect('feed/')

    print(settings.MEDIA_ROOT)
    print(settings.MEDIA_URL)
    # get all users
    user_list = User.objects.all()
    # get current user
    c_user = request.user

    # obtain the context for the user's request.
    context = RequestContext(request, {
                'user_list': user_list,
                'c_user': c_user,
            })

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        print("POST method")

        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('feed/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        t = loader.get_template('App/index.html')
        return HttpResponse(t.render(context))

def feed(request):

    # get current user
    c_user = request.user
    # get all listings about from c_user's
    r_listing = Listing.objects.filter(~Q(owner=c_user))

    t = loader.get_template('App/feed.html')
    c = Context({
            'c_user': c_user,
            'r_listing': r_listing,
        })

    return HttpResponse(t.render(c))

def register(request):
    # Like before, get the request's context.
    context = RequestContext(request)

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render_to_response(
            'App/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def profile(request, username):

    # get all users
    user_list = User.objects.all()
    # get current user
    c_user = request.user

    # get recipient user whose profile is being viewed
    r_user = User.objects.get(username=username)
    # get recipient's listings
    r_listing = Listing.objects.filter(owner=r_user)

    t = loader.get_template('App/profile.html')
    c = Context({
            'user_list': user_list,
            'c_user': c_user,
            'r_user': r_user,
            'r_listing': r_listing,
        })

    return HttpResponse(t.render(c))

def listing(request, id):

    # get current user
    c_user = request.user
    # get recipient user whose profile is being viewed
    r_listing = Listing.objects.get(id=id)
    r_user = r_listing.owner

    t = loader.get_template('App/listing.html')
    c = Context({
            'c_user': c_user,
            'r_user': r_user,
            'r_listing': r_listing,
        })

    return HttpResponse(t.render(c))

def new_listing(request):

    # get current user
    c_user = request.user

    t = loader.get_template('App/new_listing.html')
    c = Context({
            'c_user': c_user,
        })

    return HttpResponse(t.render(c))

def browse_map(request):

    # get all users
    user_list = User.objects.all()

    # get all projects
    project_list = Listing.objects.all()

    # get current user
    c_user = request.user

    t = loader.get_template('App/browse_map.html')
    c = Context({
            'user_list': user_list,
            'project_list': project_list,
            'c_user': c_user,
        })

    return HttpResponse(t.render(c))