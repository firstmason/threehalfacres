# Three Half Acres Website - AI Assistant Instructions

## Project Overview
This is a simple static website project consisting of a single HTML page and its associated CSS styling. The website is designed to display a centered image with an email contact below it.

## Project Structure
- `index.html`: Main and only HTML page of the website
- `style.css`: Contains all styling rules for the website

## Key Design Patterns

### Layout Structure
- The page uses a centered flex container layout
- Main content is wrapped in a `.container` div for centering
- Viewport height is set to 100vh for full-screen display

### CSS Conventions
- Reset CSS applied to all elements using universal selector
- Mobile-first responsive design with relative units
- Consistent color scheme using hex values (e.g., `#fafafa` for background)
- Standardized spacing using margin/padding

### Assets
- Images should be placed in the root directory
- Reference images using relative paths
- Default image dimensions: 200px width with 80% max-width constraint
- Images use border-radius: 10px for rounded corners

### Typography
- Font stack: Arial with sans-serif fallback
- Email text size: 1.2em
- Color scheme: #333 for text, #fafafa for background

## Development Workflow
This is a static site that can be served directly from the file system or through any basic HTTP server. No build process or special tooling required.

## Best Practices
1. Maintain semantic HTML structure in `index.html`
2. Keep styles organized by component in `style.css`
3. Use relative units (em, %, vh) for responsive design
4. Ensure image alt tags are descriptive for accessibility