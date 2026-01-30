# Nexus Design System

A modern, sophisticated design language for enterprise applications.

## 🎨 Design Philosophy

**Nexus** combines the clarity of modern design with the sophistication required for enterprise software. It draws inspiration from:
- **Stripe**: Clean, minimal interfaces with perfect typography
- **Linear**: Precise, purposeful design with subtle animations
- **Notion**: Warm, approachable feel with excellent information hierarchy

## 🎯 Core Principles

1. **Clarity First**: Every element serves a purpose
2. **Sophisticated Simplicity**: Complex functionality presented simply
3. **Consistent Interactions**: Predictable behavior across all components
4. **Accessible by Default**: WCAG 2.1 AA compliance built-in
5. **Performance Focused**: Optimized for speed and efficiency

## 🌈 Color Palette

### Primary Colors
- **Nexus Primary**: Purple-blue gradient (`#7c6df2` to `#6d4de6`)
- **Nexus Success**: Emerald green (`#10b981`)
- **Nexus Warning**: Amber (`#f59e0b`)
- **Nexus Error**: Rose pink (`#ec4899`)

### Neutral Grays
- Warm undertones for better readability
- 11 shades from `gray-50` to `gray-950`
- Optimized for both light and dark themes

### Surface Colors
- **Primary**: Pure white (`#ffffff`)
- **Secondary**: Subtle gray (`#fafafa`)
- **Tertiary**: Light gray (`#f5f5f5`)
- **Elevated**: White with enhanced shadows

## 📝 Typography

### Font Stack
- **Primary**: Inter (UI text, body copy)
- **Display**: Cal Sans (headings, hero text)
- **Mono**: JetBrains Mono (code, data, numbers)

### Type Scale
- Carefully crafted scale from `xs` (12px) to `6xl` (60px)
- Optimized line heights for readability
- Letter spacing adjustments for display fonts

### Usage Guidelines
```css
/* Headings */
h1 { @apply text-4xl lg:text-5xl font-display font-bold; }
h2 { @apply text-3xl lg:text-4xl font-display font-semibold; }

/* Body text */
p { @apply text-base font-sans; }

/* UI text */
.ui-text { @apply text-sm font-medium; }

/* Data/numbers */
.data-text { @apply font-mono font-semibold; }
```

## 🧩 Component System

### Buttons
```css
.nexus-btn-primary    /* Primary actions */
.nexus-btn-secondary  /* Secondary actions */
.nexus-btn-ghost      /* Subtle actions */
```

### Cards
```css
.nexus-card           /* Standard card */
.nexus-card-elevated  /* Enhanced shadow */
.nexus-glass          /* Glass morphism effect */
```

### Badges
```css
.nexus-badge-primary  /* Primary status */
.nexus-badge-success  /* Success states */
.nexus-badge-warning  /* Warning states */
.nexus-badge-error    /* Error states */
```

### Inputs
```css
.nexus-input          /* Standard form input */
```

## ✨ Animations & Interactions

### Micro-interactions
- **Hover**: Subtle scale and shadow changes
- **Focus**: Consistent ring styling
- **Active**: Gentle press effect

### Page Transitions
```css
.animate-fade-in      /* Gentle fade entrance */
.animate-slide-up     /* Slide from bottom */
.animate-slide-down   /* Slide from top */
.animate-scale-in     /* Scale entrance */
```

### Loading States
```css
.shimmer              /* Loading shimmer effect */
.animate-pulse-slow   /* Slow pulse for badges */
```

## 🎭 Shadows & Depth

### Shadow Scale
- `shadow-nexus-sm`: Subtle elevation
- `shadow-nexus`: Standard elevation
- `shadow-nexus-md`: Medium elevation
- `shadow-nexus-lg`: High elevation
- `shadow-nexus-xl`: Maximum elevation
- `shadow-nexus-glow`: Colored glow effect

### Usage Guidelines
- Use shadows to establish hierarchy
- Combine with subtle borders for definition
- Animate shadow changes for interactions

## 🎨 Sidebar Design

### Visual Features
- **Gradient Background**: Dark gradient with subtle color hints
- **Glass Effects**: Backdrop blur for modern feel
- **Smart Animations**: Smooth expand/collapse with stagger
- **Active States**: Gradient highlights for current page
- **Icon Scaling**: Subtle hover animations

### Interaction Patterns
- **Collapsible**: Toggle between full and icon-only
- **Smart Expansion**: Remember user preferences
- **Keyboard Navigation**: Full accessibility support
- **Tooltip Support**: Context in collapsed mode

## 📱 Responsive Design

### Breakpoints
- `sm`: 640px (Mobile landscape)
- `md`: 768px (Tablet)
- `lg`: 1024px (Desktop)
- `xl`: 1280px (Large desktop)
- `2xl`: 1536px (Extra large)

### Mobile-First Approach
- Start with mobile design
- Progressive enhancement for larger screens
- Touch-friendly interactions
- Optimized sidebar for mobile

## ♿ Accessibility

### Built-in Features
- **Focus Management**: Visible focus indicators
- **Color Contrast**: WCAG AA compliant ratios
- **Screen Readers**: Semantic HTML and ARIA labels
- **Keyboard Navigation**: Full keyboard support
- **Reduced Motion**: Respects user preferences

### Testing Guidelines
- Test with screen readers
- Verify keyboard navigation
- Check color contrast ratios
- Test with reduced motion settings

## 🚀 Performance

### Optimization Strategies
- **CSS-in-JS**: Minimal runtime overhead
- **Tree Shaking**: Only load used components
- **Critical CSS**: Above-fold styles inlined
- **Font Loading**: Optimized web font delivery

### Best Practices
- Use CSS transforms for animations
- Minimize layout thrashing
- Optimize images and icons
- Lazy load non-critical components

## 🔧 Implementation

### Getting Started
1. Import the design system CSS
2. Use Tailwind utility classes
3. Follow component patterns
4. Test accessibility

### Code Examples
```tsx
// Button component
<button className="nexus-btn-primary">
  <Icon className="w-4 h-4 mr-2" />
  Primary Action
</button>

// Card component
<div className="nexus-card-elevated">
  <h3 className="text-xl font-display font-bold">Card Title</h3>
  <p className="text-nexus-gray-600 mt-2">Card content...</p>
</div>

// Badge component
<span className="nexus-badge-success">Active</span>
```

## 🎯 Future Enhancements

### Planned Features
- **Dark Mode**: Complete dark theme support
- **Theme Customization**: Brand color overrides
- **Component Library**: Standalone component package
- **Design Tokens**: JSON-based design system
- **Figma Integration**: Design-to-code workflow

### Roadmap
- Q1: Dark mode implementation
- Q2: Advanced animations
- Q3: Component library extraction
- Q4: Design token system

---

*The Nexus Design System is continuously evolving. For questions or contributions, please refer to the development team.*