from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Job
from .serializers import JobSerializer

from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import Job
from .serializers import PublicJobSerializer
from django.contrib.auth.decorators import login_required


class JobViewSet(viewsets.ModelViewSet):

    queryset = Job.objects.all()

    serializer_class = JobSerializer

    permission_classes = [IsAuthenticated]
    
class PublicJobListView(generics.ListAPIView):

    serializer_class = PublicJobSerializer

    permission_classes = [AllowAny]

    queryset = Job.objects.filter(
        status="live"
    )
    
class PublicJobDetailView(generics.RetrieveAPIView):

    serializer_class = PublicJobSerializer

    permission_classes = [AllowAny]

    lookup_field = "slug"

    queryset = Job.objects.filter(
        status="live"
    )
    
from django.shortcuts import render
def public_job_page(request):

    jobs = Job.objects.filter(
        status="live"
    )

    return render(
        request,
        "jobs/job_list.html",
        {"jobs": jobs},
    )

def public_job_detail(
    request,
    slug
):

    job = Job.objects.get(
        slug=slug,
        status="live"
    )

    return render(
        request,
        "jobs/job_detail.html",
        {"job": job}
    )
from django.contrib.auth.decorators import login_required

from applications.models import Application
from jobs.models import Job
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from django.contrib.auth.decorators import login_required

from .models import Job

@login_required
@login_required
def dashboard(request):

    context = {

        "total_jobs": Job.objects.count(),

        "live_jobs": Job.objects.filter(
            status="live"
        ).count(),

        "total_applications": Application.objects.count(),

        "draft_jobs": Job.objects.filter(
            status="draft"
        ).count(),

        "pending_jobs": Job.objects.filter(
            status="pending"
        ).count(),

        "closed_jobs": Job.objects.filter(
            status="closed"
        ).count(),
    }

    return render(
        request,
        "dashboard/dashboard.html",
        context
    )
@login_required
def dashboard_jobs(request):

    jobs = Job.objects.all().order_by("-id")

    return render(
        request,
        "dashboard/jobs.html",
        {
            "jobs": jobs
        }
    )
    
@login_required
def create_job(request):

    if request.method == "POST":

        Job.objects.create(
            title=request.POST.get("title"),
            description=request.POST.get("description"),
            pay_start=request.POST.get("pay_start"),
            pay_end=request.POST.get("pay_end"),
            location=request.POST.get("location"),
            job_type=request.POST.get("job_type"),
            location_type=request.POST.get("location_type"),
            status=request.POST.get("status"),
            slug=request.POST.get("slug"),
        )

        return redirect(
            "dashboard-jobs"
        )

    return render(
        request,
        "dashboard/create_job.html"
    )
@login_required

def edit_job(request, id):

    job = get_object_or_404(
        Job,
        id=id
    )

    if request.method == "POST":

        job.title = request.POST.get("title")
        job.description = request.POST.get("description")
        job.pay_start = request.POST.get("pay_start")
        job.pay_end = request.POST.get("pay_end")
        job.location = request.POST.get("location")

        # Missing fields
        job.job_type = request.POST.get("job_type")
        job.location_type = request.POST.get("location_type")
        job.status = request.POST.get("status")
        job.slug = request.POST.get("slug")

        # Only if this field exists in model
        if hasattr(job, "cover_letter_required"):
            job.cover_letter_required = (
                request.POST.get("cover_letter_required")
                == "True"
            )

        job.save()

        return redirect(
            "dashboard-jobs"
        )

    return render(
        request,
        "dashboard/edit_job.html",
        {
            "job": job
        }
    )
@login_required
def delete_job(request, id):

    job = get_object_or_404(
        Job,
        id=id
    )

    job.delete()

    return redirect(
        "dashboard-jobs"
    )