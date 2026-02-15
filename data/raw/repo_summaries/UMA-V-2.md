<!-- Generated: 2026-02-15T03:03:41.012793Z | Model: gpt-4.1-nano -->

# UMA-V-2 Repository Documentation

## Overview
The **UMA-V-2** repository appears to be a comprehensive collection of web-based educational resources focused on anatomy, biology, and chemistry practicals. It includes static web pages, 3D models, multimedia content, and backend PHP scripts for user management and data handling. The repository is intended for students and educators to access interactive lab simulations, practical instructions, and assessment tools within a virtual laboratory environment.

---

## Key Features
- **Interactive Practical Modules:** Web pages linking to anatomy, biology, and chemistry practicals.
- **3D Models & Visualizations:** Use of `.glb` and `.gltf` files for realistic 3D representations of anatomical and chemical models.
- **Multimedia Content:** Videos (`.mp4`) and images to enhance learning.
- **User Management System:** PHP scripts for login, registration, password change, and user roles.
- **Database Integration:** MySQL database with tables for users, student marks, and student names.
- **Responsive Design Elements:** Navigation buttons, modals for user interactions, and styled headers.
- **Simulation Resources:** Embedded resources for chemistry experiments, including HDR images, models, and scripts.

---

## Architecture / How it Works
The repository combines static HTML, PHP backend scripts, and JSON-based configurations:

- **Frontend:** HTML pages styled with embedded CSS, providing navigation, user profile sections, and links to practical modules.
- **Backend:** PHP scripts (`register.php`, `logout.php`, `header.php`, `homepage_d.php`, `add_student.php`, `insert_marks.php`) handle user sessions, registration, data insertion, and updates.
- **Database:** MySQL with tables for users (`users`), student marks (`stud_name`), and student details (`stud_name`).
- **Resources:** Organized into folders such as `Anatomy_pract_templets`, `Biology_Prac_Templates`, and `Chemistry_Prac_Templates`, containing models, images, videos, and HTML/PHP pages.
- **Configuration Files:** `dbconnect.php` manages database connection parameters.

---

## Notable Folders/Files
- **`Anatomy_pract_templets/`**: Contains anatomy practical templates, 3D models (`.glb`, `.gltf`), images, and videos for anatomy labs.
- **`Biology_Prac_Templates/`**: Houses biology practical templates, diagrams, videos, and models.
- **`Chemistry_Prac_Templates/`**: Includes chemistry practical templates, 3D models of lab equipment, experiment resources, and simulation scripts.
- **`header.php`**: PHP code for user profile display, dropdown menu, and styling.
- **`dbconnect.php`**: Database connection configuration.
- **`register.php`**: Handles new user registration.
- **`logout.php`**: Ends user sessions.
- **`insert_marks.php`**: API endpoint for updating or inserting student marks via AJAX.
- **`stud_name.sql`**: Database schema and sample data for student marks and details.
- **`requirements.txt` & `Flask_app/requirements.txt`**: Python dependencies, possibly for auxiliary services or data analysis.

---

## Setup & Run
Based on the provided files:

1. **Database Setup:**
   - Import `stud_name.sql` and `users.sql` into your MySQL server.
   - Ensure the database `virtual_lab_sim` exists and the tables are created with the sample data.

2. **Server Environment:**
   - The PHP scripts require a web server with PHP support (e.g., Apache or Nginx with PHP).
   - The `Dockerfile` indicates a PHP 8.1 environment with Apache and MySQL extensions. To run via Docker:
     ```bash
     docker build -t uma-v2 .
     docker run -d -p 8080:80 uma-v2
     ```
   - Alternatively, set up a local PHP server and point it to the repository directory.

3. **Configuration:**
   - Ensure `dbconnect.php` has correct database credentials matching your MySQL setup.

4. **Access:**
   - Visit `http://localhost:8080/` (or your server URL) to access the homepage.
   - Register new users via `register.php` or through your admin interface.

---

## How to Use
- **User Login:**
  - Access the login page (not explicitly provided but implied).
  - Use credentials stored in the `users` table.
- **Navigation:**
  - Use the homepage to select practical modules for Anatomy, Biology, or Chemistry.
  - Click on practical links to open respective PHP pages with embedded resources.
- **Practicals:**
  - Interact with 3D models, videos, and images for each practical.
  - For chemistry simulations, resources are embedded within the pages, possibly with interactive 3D models.
- **Assessment & Data Entry:**
  - Teachers or authorized users can input student marks via the `insert_marks.php` API.
  - Student data and marks are stored in the database.
- **User Profile & Session:**
  - Access profile options via the dropdown menu.
  - Change password or logout as needed.

---

## Testing / CI
- No explicit testing or CI/CD pipelines are mentioned in the provided files.
- The presence of `requirements.txt` files suggests some Python-based testing or data processing might be integrated externally.

---

## Deployment
- The `Dockerfile` facilitates containerized deployment.
- To deploy:
  - Build the Docker image.
  - Run containers with appropriate port mappings.
  - Ensure the database is accessible and configured correctly.
- Static assets (images, models, videos) are organized within resource folders and should be included in the deployment package.

---

## Contribution Notes
- No specific contribution guidelines are provided.
- To contribute:
  - Fork the repository.
  - Make feature or bug fixes.
  - Submit pull requests.
- Ensure compatibility with existing PHP scripts and resource organization.

---

## Limitations / Inferred TODOs
- **Security:** Passwords are hashed, but session management and input validation details are not fully specified.
- **User Roles:** Role-based access control is implied but not fully detailed.
- **Content Management:** Static organization; dynamic content management or admin panel is not evident.
- **Testing:** No automated tests or CI pipelines are visible.
- **Localization:** The interface contains some Spanish text, indicating potential multilingual support needs.
- **Interactivity:** The extent of interactive simulations depends on embedded 3D models and scripts, which may require further development for full interactivity.

---

**Note:** Some details, such as login pages, detailed user flows, or specific scripts for lab interactions, are not explicitly provided. If further clarification is needed, please specify particular functionalities or files.
