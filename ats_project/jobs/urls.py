# from rest_framework.routers import DefaultRouter
# from django.urls import path

# from .views import JobViewSet
# from .views import (
#     PublicJobListView,
#     PublicJobDetailView,
#     public_job_page,
#     public_job_detail,
#     dashboard,
# )

# router = DefaultRouter()

# router.register(
#     'jobs',
#     JobViewSet,
#     basename='jobs'
# )

# urlpatterns = router.urls

# urlpatterns += [

#     path(
#         "public/jobs/",
#         PublicJobListView.as_view(),
#         name="public-jobs",
#     ),

#     path(
#         "public/jobs/<slug:slug>/",
#         PublicJobDetailView.as_view(),
#         name="job-detail",
#     ),
#     path(
#     "jobs/",
#     public_job_page,
#     name="jobs-page"
# ),
#     path(
#     "jobs/<slug:slug>/",
#     public_job_detail,
#     name="job-detail-page"
# ),
#     path(
#     "dashboard/",
#     dashboard,
#     name="dashboard"
# )

# ]



from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    JobViewSet,
    PublicJobListView,
    PublicJobDetailView,
    public_job_page,
    public_job_detail,
    dashboard,
    dashboard_jobs,
    create_job,
    edit_job,
    delete_job
)

router = DefaultRouter()

router.register(
    r"api/jobs",
    JobViewSet,
    basename="jobs"
)

urlpatterns = router.urls

urlpatterns += [

    # Dashboard
    path(
        "dashboard/",
        dashboard,
        name="dashboard"
    ),

    # Public Job APIs
    path(
        "api/public/jobs/",
        PublicJobListView.as_view(),
        name="public-jobs"
    ),

    path(
        "api/public/jobs/<slug:slug>/",
        PublicJobDetailView.as_view(),
        name="public-job-detail"
    ),

    # Frontend Pages
    path(
        "jobs/",
        public_job_page,
        name="jobs-page"
    ),

    path(
        "jobs/<slug:slug>/",
        public_job_detail,
        name="job-detail-page"
    ),
    path(
    "dashboard/jobs/",
    dashboard_jobs,
    name="dashboard-jobs"
),

path(
    "dashboard/jobs/create/",
    create_job,
    name="create-job"
),

path(
    "dashboard/jobs/<int:id>/edit/",
    edit_job,
    name="edit-job"
),

path(
    "dashboard/jobs/<int:id>/delete/",
    delete_job,
    name="delete-job"
),
]