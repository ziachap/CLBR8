from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import loader, Context
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse, Http404
from App.forms import *
from django.conf import settings
from django.db.models import Avg
from django.core.urlresolvers import reverse
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

    # Login form stuff
    if request.method == 'POST':
        return login_inpage(request)
    else:
        t = loader.get_template('App/index.html')
        return HttpResponse(t.render(context))

def feed(request):

    # get current user
    c_user = request.user
    # get all listings about from c_user's, remove hiddens
    # r_listing = Listing.objects.filter(~Q(owner=c_user))
    r_listing = Listing.objects.filter(hidden=False)

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
        print("register: POST");
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            print("register: form valid");
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
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            # Now we save the UserProfile model instance.
            profile.save()
            print("register: new user saved");

            # Update our variable to tell the template registration was successful.
            registered = True

            # Login the new user
            user_login = authenticate(username=user.username, password=user.password)
            if user_login:
                print("register: logging new user in");
                login(request, user_login)

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
    return HttpResponseRedirect(reverse('index'))

def profile(request, username):

    # get all users
    user_list = User.objects.all()
    # get current user
    c_user = request.user

    # get recipient user whose profile is being viewed
    r_user = User.objects.get(username=username)
    # get recipient's recent 3 listings
    r_listing_all = Listing.objects.filter(owner=r_user, hidden=False)
    if r_user == c_user:
        # if your account, get hidden projects too
        r_listing_all = Listing.objects.filter(owner=r_user)
    r_listing = list(reversed(r_listing_all))[:3]
    # get user's recent followers/following
    r_followers_all = Profile.objects.filter(following__in=[r_user])
    r_followers = list(reversed(r_followers_all))[:9]
    r_following_all = r_user.profile.following
    r_following = list(reversed(r_followers_all))[:9]
    # get user's recent 3 reviews
    r_reviews_all = Review.objects.filter(recipient=r_user)
    r_reviews = list(reversed(r_reviews_all))[:3]

    # work out averages
    if r_reviews_all:
        r_rating_1 = r_reviews_all.aggregate(Avg('rating_1'))
        r_rating_2 = r_reviews_all.aggregate(Avg('rating_2'))
        r_rating_3 = r_reviews_all.aggregate(Avg('rating_3'))
        r_rating_all = (r_rating_1['rating_1__avg'] + r_rating_2['rating_2__avg'] + r_rating_3['rating_3__avg'])/3
    else:
        r_rating_all = 0

    t = loader.get_template('App/profile.html')
    c = Context({
            'user_list': user_list,
            'c_user': c_user,
            'r_user': r_user,
            'r_listing_all': r_listing_all,
            'r_listing': r_listing,
            'r_followers_all': r_followers_all,
            'r_followers': r_followers,
            'r_following': r_following,
            'r_following_all': r_following_all,
            'r_reviews_all': r_reviews_all,
            'r_reviews': r_reviews,
            'r_rating_all': r_rating_all,
        })

    return HttpResponse(t.render(c))

def profile_projects(request, username):

    # get all users
    user_list = User.objects.all()
    # get current user
    c_user = request.user

    # get recipient user whose profile is being viewed
    r_user = User.objects.get(username=username)
    # get recipient's recent listings
    r_listing_all = Listing.objects.filter(owner=r_user, hidden=False)
    if r_user == c_user:
        # if your account, get hidden projects too
        r_listing_all = Listing.objects.filter(owner=r_user)
    # get user's recent followers/following
    r_followers_all = Profile.objects.filter(following__in=[r_user])
    r_following_all = r_user.profile.following
    # get user's reviews
    r_reviews_all = Review.objects.filter(recipient=r_user)

    t = loader.get_template('App/profile_projects.html')
    c = Context({
            'user_list': user_list,
            'c_user': c_user,
            'r_user': r_user,
            'r_listing_all': r_listing_all,
            'r_followers_all': r_followers_all,
            'r_following_all': r_following_all,
            'r_reviews_all': r_reviews_all,
        })

    return HttpResponse(t.render(c))

def inbox_default(request):
    # get current user
    c_user = request.user
    # get c_user's first conversation
    c_conversations = Conversation.objects.filter(participants__in=[c_user])
    if c_conversations:
        c_id = list(c_conversations.reverse()[:1])[0].id
    else:
        c_id = 0
    return inbox(request, c_id)

def inbox(request, id):

    # get current user
    c_user = request.user
    # get all c_user conversations
    c_conversations = Conversation.objects.filter(participants__in=[c_user]).reverse()

    t = loader.get_template('App/inbox.html')

    # if inbox blank
    if id == 0:
        blank_inbox = True;
        c = RequestContext(request, {
            'c_user': c_user,
            'blank_inbox': blank_inbox,
        })
        return HttpResponse(t.render(c))

    # get target conversation
    c_conversation = Conversation.objects.get(id=id)

    # raise error if not in conversation
    if Conversation.objects.filter(id=id, participants__in=[c_user]).exists() == False:
        raise Http404("You cannot access this conversation")

    # get messages for target convo
    c_messages = c_conversation.message_set.all

    form = MessageForm(request.POST)
    c = RequestContext(request, {
        'c_user': c_user,
        'c_conversations': c_conversations,
        'c_conversation': c_conversation,
        'c_messages': c_messages,
    })

    print(request.POST)

     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("views: message POST")

        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            print("views: message form valid")
            # set owner and save listing
            l = form.save(commit=False)
            l.sender = c_user.profile
            l.conversation = c_conversation
            l.save();

            # switch request type and redirect to browse map
            request.method = 'GET'
            return inbox(request, id)
        else:
            print form.errors

    return HttpResponse(t.render(c))

def inbox_old(request):

    # get current user
    c_user = request.user
    # get c_user conversations
    c_conversations = Conversation.objects.filter(participants__in=[c_user])

    # work out averages
    t = loader.get_template('App/inbox.html')
    c = Context({
        'c_user': c_user,
        'c_conversations': c_conversations,
    })

    return HttpResponse(t.render(c))

def listing(request, id):

    # get data
    c_user = request.user
    r_listing = Listing.objects.get(id=id)
    r_user = r_listing.owner
    r_offers = Offer.objects.filter(listing=r_listing)

    # check if already applied to this listing
    tmp1 = Offer.objects.filter(listing=r_listing)
    tmp2 = tmp1.filter(user=c_user)
    user_applied = False
    if tmp2:
        user_applied = True

    t = loader.get_template('App/listing.html')
    c = Context({
            'c_user': c_user,
            'r_user': r_user,
            'r_listing': r_listing,
            'r_offers': r_offers,
            'user_applied': user_applied,
        })

    return HttpResponse(t.render(c))

def conversation(request, id):

    # get current user
    c_user = request.user
    c_profile = c_user.profile

    # get c_user conversations
    c_conversation = Conversation.objects.get(id=id)

    # raise error if not in conversation
    if Conversation.objects.filter(id=id, participants__in=[c_user]).exists() == False:
        raise Http404("You cannot access this conversation")

    c_messages = c_conversation.message_set.all

    form = MessageForm(request.POST)

    # work out averages
    t = loader.get_template('App/conversation.html')
    c = RequestContext(request, ({
        'c_user': c_user,
        'c_conversation': c_conversation,
        'c_messages': c_messages,
    }))

    print(request.POST)

     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("views: message POST")

        # create a form instance and populate it with data from the request:
        form = MessageForm(request.POST, request.FILES)

        # check whether it's valid:
        if form.is_valid():
            print("views: message form valid")
            # set owner and save listing
            l = form.save(commit=False)
            l.sender = c_profile
            l.conversation = c_conversation
            l.save();

            # switch request type and redirect to browse map
            request.method = 'GET'
            return conversation(request, id)
        else:
            print form.errors

    return HttpResponse(t.render(c))

def follow(request, username):
    # get current user
    c_user = request.user
    # get r_user
    r_user = User.objects.get(username=username)
    # follow
    c_user.profile.following.add(r_user)
    #return HttpResponse(status=204)
    return profile(request, username)

def unfollow(request, username):
    # get current user
    c_user = request.user
    # get r_user
    r_user = User.objects.get(username=username)
    # unfollow
    c_user.profile.following.remove(r_user)
    return profile(request, username)

def accept_offer(request, id, username):
    print("views: id:" + id + " username:" + username)
    # get current user
    c_user = request.user
    # get r_user
    r_user = User.objects.get(username=username)
    # get listing
    r_listing = Listing.objects.get(id=id)
    # set employee
    r_listing.employee = r_user.profile
    # make hidden
    r_listing.hidden = True
    r_listing.save()

    return listing(request, id)

def new_listing(request):
    print("views: new listing")
    # get current user
    c_user = request.user

    # get form
    form = ListingForm()

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("views: POST")

        # create a form instance and populate it with data from the request:
        form = ListingForm(request.POST, request.FILES)


        # check whether it's valid:
        if form.is_valid():
            print("views: form valid")
            # set owner and save listing
            l = form.save(commit=False)
            l.owner = c_user
            l.save();

            # switch request type and redirect to browse map
            request.method = 'GET'
            return browse_map(request)
        else:
            # get form
            form = ListingForm(request.POST)
            print form.errors



    # get the request's context.
    context = RequestContext(request, {
            'c_user': c_user,
            'form': form,
    })

    # if a GET (or any other method) we'll create a blank form
    t = loader.get_template('App/new_listing.html')
    return HttpResponse(t.render(context))

def edit_listing(request, id):
    print("views: edit listing")
    # get current user
    c_user = request.user
    # get form
    r_listing = Listing.objects.get(id=id)
    form = ListingForm(instance=r_listing)
    # get offers
    r_offers = Offer.objects.filter(listing=r_listing)

    # get the request's context.
    context = RequestContext(request, {
        'r_listing': r_listing,
        'r_offers': r_offers,
        'c_user': c_user,
        'form': form,
    })

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("views: POST")

        # create a form instance and populate it with data from the request:
        form = ListingForm(request.POST, request.FILES, instance=r_listing)


        # check whether it's valid:
        if form.is_valid():
            print("views: form valid")
            # set owner and save listing
            form.save()

            # switch request type and redirect to browse map
            request.method = 'GET'
            return browse_map(request)
        else:
            print form.errors

    # if a GET (or any other method) we'll create a blank form
    t = loader.get_template('App/edit_listing.html')
    return HttpResponse(t.render(context))

def delete_listing(request, id):
    print("views: delete listing")

    # delete listing's audio_file
    this_listing = Listing.objects.get(id=id)

    # delete listing
    dead = Listing.objects.get(id=id).delete()

    # get current user
    c_user = request.user
    r_listing = Listing.objects.all()

    # get the request's context.
    context = RequestContext(request, {
        'c_user': c_user,
        'r_listing': r_listing,
    })

    # go back to feed
    t = loader.get_template('App/feed.html')
    return HttpResponse(t.render(context))

def new_offer(request, id):
    print("views: new offer")
    # get data
    c_user = request.user
    r_listing = Listing.objects.get(id=id)

    # check if already applied to this listing
    r_offers = Offer.objects.filter(listing=r_listing)
    prev_offers = r_offers.filter(user=c_user)
    user_applied = False
    if prev_offers:
        user_applied = True

    # get form
    form = OfferForm()

    # get the request's context.
    context = RequestContext(request, {
            'c_user': c_user,
            'form': form,
            'r_listing': r_listing,
            'user_applied': user_applied,
    })

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("views: POST")

        # create a form instance and populate it with data from the request:
        form = OfferForm(request.POST, request.FILES)


        # check whether it's valid:
        if form.is_valid():
            print("views: form valid")
            # set owner and save listing
            l = form.save(commit=False)
            l.user = c_user
            l.listing = r_listing
            l.save();

            # switch request type and redirect to feed (for now)
            request.method = 'GET'
            return HttpResponseRedirect('/listing/'+id)
        else:
            print form.errors

    # if a GET (or any other method) we'll create a blank form
    t = loader.get_template('App/new_offer.html')
    return HttpResponse(t.render(context))

def browse_map(request):

    # get all users
    user_list = User.objects.all()
    # get all projects
    project_list = Listing.objects.all()
    # get current user
    c_user = request.user

    # obtain the context for the user's request.
    context = RequestContext(request, {
                'user_list': user_list,
                'project_list': project_list,
                'c_user': c_user,
            })

    # Login form stuff
    if request.method == 'POST':
        return login_inpage(request)
    else:
        t = loader.get_template('App/browse_map.html')
        return HttpResponse(t.render(context))

def login_inpage(request):
    print("POST Request")
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

def settings_user(request):
    # get current user
    c_user = request.user
    # get form
    form = EditUserForm(instance=c_user)

    # obtain the context for the user's request.
    context = RequestContext(request, {
                'c_user': c_user,
                'form': form,
            })

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("views: POST")

        # create a form instance and populate it with data from the request:
        form = EditUserForm(request.POST, request.FILES, instance=c_user)

        # check whether it's valid:
        if form.is_valid():
            print("views: form valid")

            # copy extra info and save user
            form.save();

            # switch request type and refresh
            request.method = 'GET'
            return settings_user(request)
        else:
            print form.errors

    # if a GET (or any other method) we'll create a blank form
    t = loader.get_template('App/settings_user.html')
    return HttpResponse(t.render(context))

def settings_profile(request):
    # get current user
    c_user = request.user
    c_profile = request.user.profile
    # get form
    r_user = Profile.objects.get(user=c_user)
    form = EditUserProfileForm(instance=r_user)

    # obtain the context for the user's request.
    context = RequestContext(request, {
                'c_user': c_user,
                'form': form,
            })

    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("views: POST")

        # create a form instance and populate it with data from the request:
        form = EditUserProfileForm(request.POST, request.FILES, instance=c_profile)

        # check whether it's valid:
        if form.is_valid():
            print("views: form valid")
            # copy extra info and save profile

            form.save();

            # switch request type and refresh
            request.method = 'GET'
            return settings_profile(request)
        else:
            print form.errors

    # if a GET (or any other method) we'll create a blank form
    t = loader.get_template('App/settings_profile.html')
    return HttpResponse(t.render(context))

def about(request):
    # get current user
    c_user = request.user

    # obtain the context for the user's request.
    context = RequestContext(request, {
                'c_user': c_user,
            })

    # Login form stuff
    if request.method == 'POST':
        return login_inpage(request)
    else:
        t = loader.get_template('App/about.html')
        return HttpResponse(t.render(context))