# 🎯 Applicant Tracking System (ATS)

A modern job management platform where recruiters post opportunities, candidates discover roles, and admins oversee everything in one unified dashboard.

**Tech Stack:** Python • Django • PostgreSQL • Bootstrap 5 • JWT Authentication

---

## ✨ Key Features

| Feature | Capability |
|---------|-----------|
| 🔐 **Secure Authentication** | JWT-based login with token management |
| 💼 **Job Management** | Create, edit, publish, and manage job postings |
| 📋 **Application Tracking** | Submit applications with resume and cover letter |
| 📊 **Admin Dashboard** | Monitor jobs, applications, and system statistics |
| 🌐 **Public Portal** | Browse and apply to live job opportunities |
| 📤 **Resume Upload** | Attach files securely with applications |
| 📱 **Responsive Design** | Optimized for desktop, tablet, and mobile |

---

## 🛠️ Tech Stack

```
Backend          →  Python, Django, Django REST Framework
Database         →  PostgreSQL
Authentication   →  JWT Tokens
Frontend         →  HTML5, Bootstrap 5, CSS3
```

---

## 🔄 User Workflows

### 👨‍💼 Candidate Journey
```
Browse Jobs → View Details → Apply → Upload Resume → Track Status
```

### 👔 Recruiter Workflow
```
Login → Dashboard → Create Job → Publish → Review Applications
```

### 🏢 Admin Management
```
Full System Access → Monitor Metrics → Manage Users & Content
```

---

## 📍 API Endpoints

### 🔓 Public Endpoints (No Authentication)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/jobs/` | Browse all live jobs |
| GET | `/jobs/<slug>/` | View job details |
| GET | `/public/jobs/` | Public jobs API |
| GET | `/public/jobs/<slug>/` | Public job API details |
| POST | `/api/register/` | Create new account |
| POST | `/api/token/` | Login & obtain JWT token |
| POST | `/api/token/refresh/` | Refresh authentication token |
| POST | `/api/applications/apply/` | Submit job application |

### 🔒 Private Endpoints (Authentication Required)

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/dashboard/` | Admin dashboard overview |
| GET | `/dashboard/jobs/` | Manage all job postings |
| GET | `/dashboard/jobs/create/` | Create new job form |
| GET | `/dashboard/jobs/<id>/edit/` | Edit existing job |
| GET | `/dashboard/jobs/<id>/delete/` | Remove job posting |
| GET | `/dashboard/applications/` | View all applications |
| GET | `/admin/` | Django admin panel |

---

## 🚀 Getting Started

1. **Create Account** → Visit `/register/`
2. **Login** → Go to `/login/` to get your JWT token
3. **For Candidates** → Browse jobs at `/jobs/` and submit applications
4. **For Recruiters** → Access `/dashboard/` to manage postings
5. **For Admins** → Use `/admin/` for system administration

---

## 📝 Job Status Lifecycle

```
Draft  →  Pending Review  →  Live  →  Closed
```

- **Draft** — Preparing, not visible to candidates
- **Pending Review** — Awaiting admin approval
- **Live** — Actively accepting applications
- **Closed** — No longer accepting new applications

---

## 👥 User Roles

| Role | Permissions | Access Level |
|------|-----------|---|
| **Candidate** | Browse & Apply | Public |
| **Recruiter** | Create & Manage Jobs | Private Dashboard |
| **Administrator** | Full System Control | Admin Panel |

---

## ✅ Feature Highlights

✔️ User registration and secure JWT authentication  
✔️ Complete CRUD operations for job postings  
✔️ Real-time application tracking system  
✔️ Comprehensive admin dashboard with analytics  
✔️ Public job discovery portal  
✔️ Secure resume upload functionality  
✔️ Mobile-friendly responsive interface  

---

## 📸 Screenshots

### Private Admin & Recruiter Interface

#### Registration Page
`http://127.0.0.1:8000/register/`
<img width="1365" height="484" alt="Registration Page" src="https://github.com/user-attachments/assets/2f6d59fe-6e90-4f73-8e64-ad9887c60353" />

#### Login Page
`http://127.0.0.1:8000/login/`
<img width="887" height="425" alt="Login Page" src="https://github.com/user-attachments/assets/6b7d9d25-9b6b-455e-bf6b-b58680643581" />

#### Admin Dashboard
`http://127.0.0.1:8000/dashboard/`
<img width="1365" height="523" alt="Dashboard Overview" src="https://github.com/user-attachments/assets/271783a1-9e6f-4dc1-98a4-2754b6ce18da" />

#### Jobs Management
`http://127.0.0.1:8000/dashboard/jobs/`
<img width="1350" height="549" alt="Jobs List" src="https://github.com/user-attachments/assets/8149a26c-6ccb-44df-af1b-776b4c0f6d4d" />

#### Edit Job
`http://127.0.0.1:8000/dashboard/jobs/7/edit/`
<img width="1029" height="556" alt="Edit Job Form" src="https://github.com/user-attachments/assets/822887e9-dd75-4205-a901-987969c3f992" />

#### Create Job
`http://127.0.0.1:8000/dashboard/jobs/create/`
<img width="970" height="563" alt="Create Job Form" src="https://github.com/user-attachments/assets/7b035fa6-f457-4e06-9d60-cc8e09ed419e" />

#### Applications Review
`http://127.0.0.1:8000/dashboard/applications/`
<img width="1363" height="351" alt="Applications List" src="https://github.com/user-attachments/assets/591f123e-03d4-4703-9066-508874ed81cb" />

#### Resume Viewer
`http://127.0.0.1:8000/media/resumes/Ashish_1010_3BPIdR8.pdf`
<img width="1331" height="551" alt="Resume Preview" src="https://github.com/user-attachments/assets/56c53051-2ed0-425c-a2fe-ffb860d0c87e" />

---

### Public Candidate Interface

#### Job Portal
`http://127.0.0.1:8000/jobs/`
<img width="1333" height="581" alt="Public Jobs Portal" src="https://github.com/user-attachments/assets/06629542-7faf-4b98-ad5b-d266e4265ccd" />

#### Job Details
`http://127.0.0.1:8000/jobs/python-developer/`
<img width="1310" height="590" alt="Job Details Page" src="https://github.com/user-attachments/assets/fa4d00f0-bcb3-4d7e-84a5-f11e027d0b70" />

#### Application Form
`http://127.0.0.1:8000/jobs/python-developer/apply/`
<img width="1365" height="598" alt="Application Form" src="https://github.com/user-attachments/assets/3f8fab40-9fac-4e5c-8018-a892939187f0" />

---

## 📧 Support

For issues, questions, or feature requests, please open an issue in the repository.

---

**Built with ❤️ | Designed for Efficient Hiring**
