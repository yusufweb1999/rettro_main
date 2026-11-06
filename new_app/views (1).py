
# from django.shortcuts import render, redirect
# from new_app. import ApplicationForm


# def application_create(request):
#     if request.method == "POST":
#         form = ApplicationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             return redirect("application_success")

#     else:
#         form = ApplicationForm()

#     return render(
#         request,
#         "applications/application_form.html",
#         {"form": form}
#     )


# def application_success(request):
#     return render(
#         request,
#         "applications/success.html"
#     )