# Applicant Tracking System (ATS)

A simple job management and application platform built with Django and PostgreSQL. Recruiters post jobs, candidates apply, and admins track everything through a dashboard.

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| Python | Backend |
| Django | Web Framework |
| Django REST Framework | APIs |
| PostgreSQL | Database |
| JWT | Authentication |
| Bootstrap 5 | Frontend |

## ✨ Key Features

### 👤 User Authentication
- User registration
- JWT-based login
- Secure token management

### 💼 Job Management (Recruiters/Admins)
- **Create, Read, Update, Delete** jobs
- Job fields: Title, Description, Salary, Location, Type
- Job status: Draft, Pending, Live, Closed

### 📝 Job Applications (Candidates)
- Browse live jobs
- View job details
- Apply with resume & cover letter
- Track applications

### 📊 Admin Dashboard
- View total jobs (Live, Draft, Pending, Closed)
- Monitor total applications
- Manage all jobs and applications

---

## 🔄 User Flows

### Candidate Flow
```
Browse Jobs → View Details → Apply → Upload Resume → Application Saved
```

### Recruiter Flow
```
Login → Dashboard → Create Job → Publish → Review Applications
```

---

## 📍 API Endpoints

### Public (No Authentication Required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/jobs/` | List all live jobs |
| GET | `/jobs/<slug>/` | View job details |
| GET | `/public/jobs/` | Public jobs API |
| GET | `/public/jobs/<slug>/` | Public job details API |
| POST | `/api/register/` | Register new user |
| POST | `/api/token/` | Login & get JWT token |
| POST | `/api/token/refresh/` | Refresh JWT token |
| POST | `/api/applications/apply/` | Submit job application |

### Private (Authentication Required)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/dashboard/` | Admin dashboard |
| GET | `/dashboard/jobs/` | List all jobs |
| GET | `/dashboard/jobs/create/` | Create job form |
| GET | `/dashboard/jobs/<id>/edit/` | Edit job form |
| GET | `/dashboard/jobs/<id>/delete/` | Delete job |
| GET | `/dashboard/applications/` | View all applications |
| GET | `/admin/` | Django admin panel |

---

## 🚀 Quick Start

1. **Register** as a user: `/register/`
2. **Login** for JWT token: `/login/`
3. **Candidates**: Browse jobs at `/jobs/` and apply
4. **Recruiters**: Access `/dashboard/` to manage jobs
5. **Admins**: Use `/admin/` for full system control

---

## 📝 Job Status Workflow

```
Draft → Pending → Live → Closed
```

- **Draft**: Not yet published
- **Pending**: Awaiting approval
- **Live**: Accepting applications
- **Closed**: No longer accepting applications

---

## 🎯 Quick Reference

| User Type | Main Actions | Access |
|-----------|-------------|--------|
| **Candidate** | Browse, Apply | Public |
| **Recruiter** | Create, Edit, Delete Jobs | Private (Dashboard) |
| **Admin** | Full System Access | Private (Admin) |

---

## ✅ Features at a Glance

✅ JWT Authentication  
✅ Job CRUD Operations  
✅ Application Management  
✅ Admin Dashboard with Stats  
✅ Public Job Portal  
✅ Resume Upload Support  
✅ Responsive UI (Bootstrap 5)
