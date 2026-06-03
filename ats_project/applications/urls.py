from django.urls import path

from .views import (
    ApplyJobView,
    apply_page,
    applications_list,
)

urlpatterns = [

    # DRF API
    path(
        "api/applications/apply/",
        ApplyJobView.as_view(),
        name="apply-job"
    ),

    # Frontend Apply Page
    path(
        "jobs/<slug:slug>/apply/",
        apply_page,
        name="apply-page"
    ),

    # Dashboard Applications
    path(
        "dashboard/applications/",
        applications_list,
        name="applications-list"
    ),
]
# urlpatterns = [

#     path(
#         "apply/",
#         ApplyJobView.as_view(),
#         name="apply-job"
#     ),
#     path(
#     "jobs/<slug:slug>/apply/",
#     apply_page,
#     name="apply-page"
# ),
#   path(
#     "applications/",
#     applications_list,
#     name="applications-list"
# ),

# ]