<!-- Generated: 2026-02-15T03:03:04.638892Z | Model: gpt-4.1-nano -->

# prathamesh-portfolio-static

## Overview
This repository contains the source code for a personal portfolio website designed to showcase AI and machine learning projects, research, and professional experience. Built with TypeScript and React, it aims to serve developers, researchers, and AI enthusiasts who want a modern, visually appealing online presence. The project is structured to facilitate easy customization and deployment.

## Key Features
- **Responsive Design:** Fully responsive layout optimized for desktop and mobile devices.
- **Component-Based Architecture:** Modular React components for easy maintenance and scalability.
- **UI Components:** Custom UI elements such as cards, buttons, badges, and forms for consistent styling.
- **Interactive Navigation:** Sticky header with smooth scrolling to sections.
- **Hero Section:** Engaging introduction with profile image, animated scroll indicator, and call-to-action buttons.
- **About Section:** Skills overview with categorized badges and professional summary.
- **Projects Showcase:** Featured projects with images, tags, impact, and tech stack.
- **Experience Timeline:** Detailed professional experience with achievements and skills.
- **Publications & Research:** List of publications with details and impact metrics.
- **Contact & Footer:** Contact information, social links, and call-to-action for collaboration.

## Architecture / How it Works
The project is structured as a React application using TypeScript, styled primarily with Tailwind CSS. It leverages Radix UI components for accessible UI elements and Lucide icons for visual cues. The main application flow is managed in `src/App.tsx`, which composes various sections like Hero, About, Projects, Experience, Publications, and Contact.

Key configuration files:
- `vite.config.ts`: Configures Vite build tool with path aliases and plugins.
- `package.json`: Manages dependencies, scripts, and project metadata.
- `index.html`: Entry point for the web app.

## Notable Folders/Files
- `src/`: Contains all React components, assets, styles, and configuration files.
  - `components/`: Modular React components for each section and UI element.
  - `components/ui/`: Reusable UI primitives like Card, Button, Badge, and form controls.
  - `assets/`: Static assets including images used in the site.
  - `styles/`: Global CSS files.
  - `App.tsx`: Main app component that assembles all sections.
  - `main.tsx`: Entry point that renders the React app.
- `vite.config.ts`: Vite configuration for development and build.
- `package.json`: Dependencies and scripts for project setup.

## Setup & Run
1. Clone the repository:
```bash
git clone https://github.com/upratham/prathamesh-portfolio-static.git
```
2. Navigate into the project directory:
```bash
cd prathamesh-portfolio-static
```
3. Install dependencies:
```bash
npm install
```
4. Start the development server:
```bash
npm run dev
```
The app will be available at `http://localhost:3000` in your browser.

## How to Use
- **Customizing Content:** Edit the React components (`Hero.tsx`, `About.tsx`, `Projects.tsx`, etc.) to update texts, images, and project details.
- **Adding Projects/Publications:** Append new objects to the respective arrays in `Projects.tsx` and `Publications.tsx`.
- **Changing Styles:** Modify Tailwind CSS classes in components or update `globals.css` for global styles.
- **Deployment:** Use `vite build` to generate production build:
```bash
npm run build
```
Deploy the contents of the `build/` directory to your hosting provider.

## Testing / CI
No explicit testing or CI configurations are present in the provided files. Implementing testing frameworks or CI pipelines can be added as needed.

## Deployment
The project includes a `vercel.json` configuration, indicating readiness for deployment on Vercel. To deploy:
- Push the code to a GitHub repository.
- Connect the repository to Vercel.
- Vercel will automatically build and deploy the site based on the `build` script.

## Contribution Notes
No contribution guidelines are included in the current repository. For contributions:
- Fork the repository.
- Create feature branches.
- Submit pull requests with clear descriptions.

## Limitations / TODOs (Inferred)
- **No License Specified:** Licensing information is absent; consider adding a license file.
- **Accessibility & Internationalization:** Not explicitly addressed; may need enhancements.
- **Testing & CI/CD:** Not implemented; adding tests and CI pipelines could improve robustness.
- **Content Management:** Content is hardcoded within components; integrating a CMS or markdown files could facilitate easier updates.
- **Performance Optimization:** Lazy loading images and code splitting are not evident; could be optimized for faster load times.
- **Analytics & SEO:** Not present; adding Google Analytics or SEO meta tags could improve discoverability.

---

*Note:* If specific details about deployment, contribution, or additional features are required, please provide further information.
