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
Private Api/Admin 
http://127.0.0.1:8000/register/
<img width="1365" height="484" alt="image" src="https://github.com/user-attachments/assets/2f6d59fe-6e90-4f73-8e64-ad9887c60353" />
http://127.0.0.1:8000/login/
<img width="887" height="425" alt="image" src="https://github.com/user-attachments/assets/6b7d9d25-9b6b-455e-bf6b-b58680643581" />
http://127.0.0.1:8000/dashboard/
<img width="1365" height="523" alt="image" src="https://github.com/user-attachments/assets/271783a1-9e6f-4dc1-98a4-2754b6ce18da" />
http://127.0.0.1:8000/dashboard/jobs/
<img width="1350" height="549" alt="image" src="https://github.com/user-attachments/assets/8149a26c-6ccb-44df-af1b-776b4c0f6d4d" />
http://127.0.0.1:8000/dashboard/jobs/7/edit/
<img width="1029" height="556" alt="image" src="https://github.com/user-attachments/assets/822887e9-dd75-4205-a901-987969c3f992" />
http://127.0.0.1:8000/dashboard/jobs/create/
<img width="970" height="563" alt="image" src="https://github.com/user-attachments/assets/7b035fa6-f457-4e06-9d60-cc8e09ed419e" />
http://127.0.0.1:8000/dashboard/applications/
<img width="1363" height="351" alt="image" src="https://github.com/user-attachments/assets/591f123e-03d4-4703-9066-508874ed81cb" />
http://127.0.0.1:8000/media/resumes/Ashish_1010_3BPIdR8.pdf
<img width="1331" height="551" alt="image" src="https://github.com/user-attachments/assets/56c53051-2ed0-425c-a2fe-ffb860d0c87e" />





Public api
http://127.0.0.1:8000/jobs/
<img width="1333" height="581" alt="image" src="https://github.com/user-attachments/assets/06629542-7faf-4b98-ad5b-d266e4265ccd" />
http://127.0.0.1:8000/jobs/python-developer/
<img width="1310" height="590" alt="image" src="https://github.com/user-attachments/assets/fa4d00f0-bcb3-4d7e-84a5-f11e027d0b70" />
http://127.0.0.1:8000/jobs/python-developer/apply/
<img width="1365" height="598" alt="image" src="https://github.com/user-attachments/assets/3f8fab40-9fac-4e5c-8018-a892939187f0" />




