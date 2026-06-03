# # from django.shortcuts import render

# # # Create your views here.
# # from rest_framework import generics
# # from rest_framework.permissions import AllowAny

# # from .models import Application
# # from .serializers import ApplicationSerializer


# # class ApplyJobView(
# #     generics.CreateAPIView
# # ):

# #     serializer_class = ApplicationSerializer

# #     permission_classes = [AllowAny]
# # from django.shortcuts import render


# # def apply_page(request):

# #     return render(
# #         request,
# #         "jobs/apply.html"
# #     )
# # from django.shortcuts import render

# # from .models import Application

# # def applications_list(request):

# #     applications = (
# #         Application.objects
# #         .select_related("job")
# #         .all()
# #         .order_by("-created_at")
# #     )

# #     return render(

# #         request,

# #         "applications/list.html",

# #         {
# #             "applications":
# #             applications
# #         }
# #     )


# from django.shortcuts import (
#     render,
#     get_object_or_404
# )

# from rest_framework import generics
# from rest_framework.permissions import AllowAny

# from jobs.models import Job
# from .models import Application
# from .serializers import ApplicationSerializer


# class ApplyJobView(generics.CreateAPIView):

#     serializer_class = ApplicationSerializer
#     permission_classes = [AllowAny]


# def apply_page(request, slug):

#     job = get_object_or_404(
#         Job,
#         slug=slug,
#         status="live"
#     )

#     return render(
#         request,
#         "applications/apply.html",
#         {
#             "job": job
#         }
#     )


# def applications_list(request):

#     applications = (
#         Application.objects
#         .select_related("job")
#         .all()
#         .order_by("-created_at")
#     )

#     return render(
#         request,
#         "applications/list.html",
#         {
#             "applications": applications
#         }
#     )

from django.shortcuts import (
    render,
    get_object_or_404,
)

from rest_framework import generics
from rest_framework.permissions import AllowAny

from jobs.models import Job
from .models import Application
from .serializers import ApplicationSerializer


# -------------------------
# DRF API
# POST /api/applications/apply/
# -------------------------
class ApplyJobView(generics.CreateAPIView):

    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]


# -------------------------
# Frontend Apply Page
# /jobs/<slug>/apply/
# -------------------------
def apply_page(request, slug):

    job = get_object_or_404(
        Job,
        slug=slug,
        status="live"
    )

    if request.method == "POST":

        application = Application.objects.create(
            job=job,
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            resume=request.FILES.get("resume"),
            cover_letter=request.POST.get(
                "cover_letter",
                ""
            )
        )

        return render(
            request,
            "applications/success.html",
            {
                "job": job,
                "application": application
            }
        )

    return render(
        request,
        "applications/apply.html",
        {
            "job": job
        }
    )


# -------------------------
# Dashboard Applications
# /dashboard/applications/
# -------------------------
def applications_list(request):

    applications = (
        Application.objects
        .select_related("job")
        .all()
        .order_by("-created_at")
    )

    return render(
        request,
        "applications/list.html",
        {
            "applications": applications
        }
    )