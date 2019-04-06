from django.shortcuts import render, redirect
from django.contrib import messages
from users.forms import UserRegisterForm,ProfileUpdateForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from users.models import Profile,Comments

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("/user/login/")
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})





# @login_required
# def profile(request):
#     if request.method == 'POST':
#         u_form = UserUpdateForm(request.POST, instance=request.user)
#         print(request.user.profile)
#         p_form = ProfileUpdateForm(request.POST,
#                                    request.FILES,
#                                    instance=request.user.profile)
#         if u_form.is_valid() and p_form.is_valid():
#         	u_form.save()
#         	p_form.save()
#         	messages.success(request, f'Your account has been updated!')
#         	return redirect("/user/profile/")


#     else:
#         u_form = UserUpdateForm(instance=request.user)
#         p_form = ProfileUpdateForm(instance=request.user.profile)

#     context = {
#         'u_form': u_form,
#         'p_form': p_form,
#     }

#     return render(request, 'user/profile.html', context)



def userlayout(request):
    if request.method == 'GET':
        query = request.GET.get('query', '')
        if query is None:
            users = User.objects.all()
        else:
            users = User.objects.filter(username__contains=query)
    
        users = list(users)
        for i in range(len(users)):
            if users[i] == request.user:
                users.remove(users[i])

        data = []
        for user in users:
            _data = {
                'name': user.username,
                'email': user.email,
                'profile_data': False,
            }
            try:
                profile = Profile.objects.get(user=user)
                _data['image_url'] = profile.image.url
                _data['about_me'] = profile.about_me
                _data['profile_data'] = True
            except Exception as e:
                print(e)

            data.append(_data)
        
        context = {
            'data': data,
        }

        return render(request,'userlayout.html/', context)


def profile(request):
    current_user = request.user

    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST)
        if form.is_valid():
            # form.save()
            contact_no = form.cleaned_data['contact_no']
            about_me = form.cleaned_data['about_me']
            nick_names = form.cleaned_data['nick_names']
            image = form.cleaned_data['image']
            frequently_uttered_words = form.cleaned_data['frequently_uttered_words']
            striking_features = form.cleaned_data['striking_features']

            try:
                profile = Profile.objects.get(user=current_user)

                profile.contact_no=contact_no
                profile.about_me=about_me
                profile.nick_names=nick_names
                profile.image=image
                profile.frequently_uttered_words=frequently_uttered_words
                profile.striking_features=striking_features
                profile.save()
            except Exception as e:
                # profile do not exist
                profile = Profile(
                    user=current_user,
                    contact_no=contact_no,
                    about_me=about_me,
                    nick_names=nick_names,
                    image=image,
                    frequently_uttered_words=frequently_uttered_words,
                    striking_features=striking_features,
                )
                profile.save()
            
            return redirect("/user/searchfriends/")


                # send redirect to respective page
            # If exist update
            # else create

            # return redirect("/user/login/")
    else:
        form = ProfileUpdateForm()

    try:
        profile = Profile.objects.get(user=current_user)

        form.fields['contact_no'].initial = profile.contact_no
        form.fields['about_me'].initial = profile.about_me
        form.fields['nick_names'].initial = profile.nick_names
        form.fields['image'].initial = profile.image
        form.fields['frequently_uttered_words'].initial = profile.frequently_uttered_words
        form.fields['striking_features'].initial = profile.striking_features
        # form.save()
    except Exception as e:
        # do nothing 
        pass
        
    return render(request, 'user/profile.html', {'form': form})


def friendprofile(request, username):
    friend_user = User.objects.get(username=username)
    friend_profile = Profile.objects.get(user=friend_user)

    context = {
        'image_url': friend_profile.image.url,
        'user':friend_profile.user,
        'contact_no':friend_profile.contact_no,
        'nick_names':friend_profile.nick_names,
        'about_me':friend_profile.about_me,
        'frequently_uttered_words':friend_profile.frequently_uttered_words,
    }

    return render(request, 'user/friendprofile.html', context)


def commentpage(request,username):
    print(username)
    friend_user = User.objects.get(username = username)
    friend_profile = Profile.objects.get(user = friend_user)
    print(friend_user)
    print(friend_profile.user)
    print(friend_profile.contact_no)
    current_user = request.user

    if request.method == 'GET':
        print(friend_user)
        form = CommentForm(request.GET)
        if form.is_valid():
            comment= form.cleaned_data['comment']
            comment = Comments(
                            user = friend_user,
                            comment=comment,
                            posted_by = str(current_user)
                        )
            comment.save()
            return redirect("/home/")

        else:
            form = CommentForm()
    print(friend_profile.frequently_uttered_words)

    return render(request,'user/commentpage.html',{'form': form})

def mycommentpage(request):
    current_user = request.user
    mycomments = Comments.objects.filter(user = current_user)
    #print(mycomments.first)

    context = {
        'comment': mycomments,
    }

    return render(request,'user/mycommentpage.html',context)
# friend_comment = Comments.objects(user = username)
    # context = {
    #     'friend':friend_comment
    # }

def searchfriends(request):
    return render(request, 'user/searchfriends.html',{})