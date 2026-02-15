<!-- Generated: 2026-02-15T03:03:22.568460Z | Model: gpt-4.1-nano -->

# upratham/chem_sim

## Overview
`chem_sim` is a JavaScript-based interactive chemistry simulation repository designed primarily for educational purposes. It provides 3D visualizations and interactive experiments related to various chemistry concepts such as flame tests, precipitation reactions, Archimedes principle, and more. The project is built using React and Three.js, making it suitable for students, educators, and developers interested in creating or customizing chemistry simulations.

## Key Features
- Interactive 3D models of chemical apparatus and experiments.
- Visualizations of flame tests with customizable colors.
- Simulation of water displacement and volume measurement.
- Demonstrations of chemical reactions like precipitation, decomposition, and displacement.
- User interaction through drag-and-drop, click, and hover events.
- Dynamic water level adjustment based on object displacement.
- Modular architecture allowing easy addition of new experiments.

## Architecture / How it Works
The repository is structured around React components that leverage Three.js for 3D rendering. Core functionalities include:
- Loading 3D models (`.glb`) using `GLTFLoader`.
- Managing scene, camera, and lighting setups.
- Handling user interactions such as dragging objects and clicking.
- Simulating physical phenomena like buoyancy, collision detection, and particle effects.
- Dynamic updates to models and environment based on user actions.

Key files and their roles:
- `src/index.js`: Entry point, sets up routing and renders the main components.
- `src/Components/`: Contains React components for each experiment and core functionalities.
- `src/getBunsenFlame.js` & `src/getParticleSystem.js`: Utility functions for creating flame and particle effects.
- `src/Components/Water.js`: Manages water simulation, displacement, and volume calculations.
- `public/Resources/`: Contains 3D models, textures, and resources used in experiments.

## Notable Folders/Files
- `src/Components/`: React components for different experiments and scene management.
- `src/getBunsenFlame.js`: Provides shader-based particle system for flame visualization.
- `src/Components/Water.js`: Implements water physics, buoyancy, and volume adjustments.
- `public/Resources/`: Stores all static assets like models (`.glb`), textures, and images.
- `index.js`: Sets up routing for different experiment pages, linking to components like `MainHomePage`, `FlameTestComponent`, etc.

## Setup & Run
1. Clone the repository:
```bash
git clone https://github.com/upratham/chem_sim.git
cd chem_sim
```
2. Install dependencies:
```bash
npm install
```
3. Run the development server:
```bash
npm start
```
This will start the app at `http://localhost:3000`.

## How to Use
- Access the homepage to see a list of experiments.
- Click on an experiment card to navigate to its interactive simulation.
- Use mouse controls to rotate, zoom, and interact with 3D models.
- Drag objects to simulate placement or reactions.
- Adjust sliders or input fields (if available) to modify parameters like water height.
- Observe visual effects such as flames, bubbling, or precipitate formation.

## Testing / CI
- The repository includes scripts for testing via `react-scripts test`.
- No explicit CI/CD configurations are provided in the current data.
- To run tests:
```bash
npm test
```

## Deployment
- The project uses `react-scripts build` for production builds.
- To build for deployment:
```bash
npm run build
```
- Deployment instructions are standard for React apps; host the contents of the `build` folder on a web server.

## Contribution Notes
- No specific contribution guidelines are provided.
- Contributions can be made by forking the repository, creating feature branches, and submitting pull requests.

## Limitations / TODOs (Inferred)
- License information is not specified.
- No explicit documentation on adding new experiments or models.
- The current setup may require additional configuration for advanced features or custom resources.
- Potential improvements include adding unit tests, CI/CD pipelines, and detailed contribution guidelines.

---

*Note:* Some details are inferred based on the provided code snippets and file structure. For precise instructions or features, refer to the actual codebase or contact the repository maintainer.
